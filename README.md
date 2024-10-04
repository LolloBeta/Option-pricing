These are some option pricing methods <br> 
The main assumptions are explained in the comments inside the code <br>
For the Binomial option model for Eu options I've used the original Cox, Ross e Rubinstein formulation of the 1979 paper "Option Pricing: A Simplified Approach" and I've built 2 versions: the first one is definitely slower but more intuitive, while the second one is much more efficient but it needs some numpy vectorisation tools in order to work <br>
For the Binomial option model for US options I've used the same assumptions of the former one but I have implemented only the fast version because the rationale is the same <br>
For the Black-Scholes I've used the Merton assumption, which led to a portfolio of options and stocks and thus having a risk free rate of return (the original assumption of Black-Scholes was based on CAPM) <br>
I have included here the comparision between Black-Scholes and Binomial tree to show that as the number of nodes approaches infinity, the two methods converge, which is mathematically provable 
