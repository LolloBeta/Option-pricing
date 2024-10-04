import numpy as np
#Here we have a Binomial Option Pricing Model for European Options without dividend
#We compute the value at the end and then we work backwards
#we define each possible value as a paired couple (i,j) with i being the i-th step and j being the power of u:
#so each possible value is S0*u**j*d**(i-j)
#The main assumptions are: finite number of steps (discrete time), known volatility, which is equal at each step,
#risk neutral valuation
def Binomial_tree_V1 (S0,K,T,r,sigma,t,N):
    #T=expiration time, S=stock price, K=strike price, r=interest rate, sigma=volatility,
    #n=height of the binomial tree, t=type of option (0 call, 1 put)
    deltaT=T/N
    u=np.exp(sigma*np.sqrt(deltaT))
    d=1/u
    disc = np.exp(-r*deltaT)
    p=(np.exp(r*deltaT)-d)/(u-d)
    
    #price of the stock at the end
    S=[]
    S += [S0*d**N]
    for j in range(1,N+1):
        S += [S[j-1]*u/d] 
        
    P = np.zeros(N+1) #values of the contract at the end
    for j in range(0,N+1):
        if(t=='C'):
            P[j] = max(0, S[j]-K) #it's a call
        else:
            P[j] = max(0, K-S[j]) #it's a put
    
    for i in np.arange(N,0,-1): #we use arange because for large vectorised computations is faster
        for j in range(0,i):
            P[j] = disc * ( p*P[j+1] + (1-p)*P[j] ) #since we are in a arbitrage free world, we discount back with rate r

    return P[0] #the initial price

def Binomial_tree_V2 (S0,K,T,r,sigma,t,N):
    #T=expiration time, S=stock price, K=strike price, r=interest rate, sigma=volatility,
    #n=height of the binomial tree, t=type of option (0 call, 1 put)
    deltaT=T/N
    u=np.exp(sigma*np.sqrt(deltaT))
    d=1/u
    disc = np.exp(-r*deltaT)
    p=(np.exp(r*deltaT)-d)/(u-d)
    
    #price of the stock at the end
    S= S0*d**(np.arange(N,-1,-1))*u**(np.arange(0,N+1,1))
        
    if(t=='C'):
        P = np.maximum(S-K,np.zeros(N+1))
    else:
        P = np.maximum(K-S,np.zeros(N+1))
    
    for i in np.arange(N,0,-1): #we use arange because for large vectorised computations is faster
        P=disc*(p*P[1:i+1]+(1-p)*P[0:i])
    return P[0] #the initial price
        
print(Binomial_tree_V1 (100,100,1,0.06,1.1,'C',1000))
print(Binomial_tree_V2 (100,100,1,0.06,1.1,'C',1000))
