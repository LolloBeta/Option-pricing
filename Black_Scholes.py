#we develop the model using the Merton assumption, so we build a portfolio with the option and the underlying and
#we argue that the return over a short period of time should be the risk free rate
#we assume that the variation of price in a short time period must be normally distribute

import numpy as np
from scipy.stats import norm

def blackscholes (S,K,T,r,sigma,CP):
    stddev=(sigma*np.sqrt(T)) #we explicitely wrote down standard deviation
    d1=(np.log(S/K)+(r+sigma**2/2)*T)/stddev
    d2=d1-stddev
    if CP=='C': #we have a call option
        price=S*norm.cdf(d1,0,1)-K*np.exp(-r*T)*norm.cdf(d2,0,1)
    else: #we are assuming the correctness of the input CP
        price=K*np.exp(-r*T)*norm.cdf(-d2,0,1)-S*norm.cdf(-d1,0,1)
    return price