from Black_Scholes import blackscholes
from Binomial_tree import Binomial_tree_V2 as bt

S=100
K=100
T=2
r=0.05
sigma=0.10
t='C'
nodes=10
difference=[]
bs=blackscholes(S,K,T,r,sigma,t)
for i in range(5):
    difference+=[round(bs-bt(S,K,T,r,sigma,t,nodes),3)]
    print(difference[i])
    nodes=nodes*10
