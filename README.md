# sghmcmc-
===========
sghmcmc
===========

sghmc has hmc, sghmc_jit, naive_sghmc 

c1 = naive_sghmc(lnp,lnp_grad,initialguess,data=None,usedata = False, M = None)

c2 = hmc(lnp,lnp_grad,initialguess, data = None, usedata = False, M = None)

c3 = sghmc_jit(lnp,lnp_grad,initialguess,C,data = None, usedata = False,B=None,M=None,logpri=None)

To start sample:

cx.sampling(iterations, epsilon, length, size)

source files are located in sghmcmc, examples notebook.ipynb may take a while to run 
