import numpy as np
#with an american call option, it doesn't make sense doing early exercise because you are paying a premium today without receving the
#risk free rate of return on that premium
#we need to specify that this isn't always the case, since we may have negative interest rates, but given that this is a very rare situation
#and that usually doesn't apply to retails, we will discard it
#morover we are considering here stocks without any dividend (like in the european case), so this shouldn't affect our decisions
#conversely, for an american put option might make sense to do early exercise if the discounted expected value makes it worth it
#despite these considerations, we are implementing both call and put type of american options
#the main difference between this case and the european one is that here we compute the value of the option at each node
def Binomial_tree_US (S0,K,T,r,sigma,t,N):
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
    #up to this point is the same as binomial tree for european options, so the main difference is in the backward process
    for i in np.arange(N-1,-1,-1):
        S= S0*d**(np.arange(i,-1,-1))*u**(np.arange(0,i+1,1)) #at each node we repeat the calculation at the line 20
        P[:i+1]=disc*(p*P[1:i+2]+(1-p)*P[0:i+1]) #we cannot simply calculate P, we use slicing in order to take the first i components
        P=P[:-1] #since in the line below we compare 2 vectors, they should have the same length
        if t == 'C': #at each node we compute the value of the option
            P = np.maximum(P, S-K) 
        else:
            P = np.maximum(P, K-S)
    return P[0]
        
print(Binomial_tree_US(100, 100, 1, 0.06, 0.1650820739,'P',3))
        
        
        
        
    