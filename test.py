#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sghmcmc
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


# In[4]:


#test using example in paper
def ut(theta):
    theta = np.array(theta)
    return 2 * (theta ** 2) - (theta ** 4)
def gut(theta):
    theta = np.array(theta)
    return 4 * theta - 4 * (theta ** 3)
def gutnoise(theta):
    theta = np.array(theta)
    return 4 * theta - 4 * (theta ** 3) + np.random.normal(0, 2)


# In[5]:


C = 0
sghmc = sghmcmc.sghmc_jit(ut,gut,[0.0],C)
sghmc.sampling(20000,0.1,50,200)


# In[7]:


hmc = sghmcmc.hmc(ut, gutnoise, [2.0])
hmc.sampling(20000, 0.1, 50)


# In[9]:


#plot the result
densitysghmc = stats.kde.gaussian_kde(np.array([x[0][0] for x in sghmc.res[1:]]))
densityhmc = stats.kde.gaussian_kde(np.array([x[0][0] for x in hmc.res[1:]]))
x = np.linspace(-3,3,100)
plt.figure(figsize=(7,5))
plt.plot(x, densitysghmc(x), '--',label = "SGHMC")
plt.plot(x, densityhmc(x), '-.', label = "HMC")
plt.plot(x, np.exp(ut(x))/5.361, ':',label = "True Distribution")
plt.legend()
plt.title("Test Performance of Algorithms");

