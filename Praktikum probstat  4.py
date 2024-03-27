#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def n_choose_k(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def binomial_probability(n, k, p):
    return n_choose_k(n, k) * (p ** k) * ((1 - p) ** (n - k))

n = 10
p = 0.5
k = 3

prob_binomial = binomial_probability(n, k, p)
print("Probabilitas P(X=k) untuk distribusi binomial:", prob_binomial)


# In[2]:


from scipy.stats import binom

n = 10
p = 0.5
k = 3

prob_binomial + binom.pmf(k, n, p)
print("Probabilitas P(X=k) untuk distribusi binomial:", prob_binomial)


# In[3]:


import math 

def poisson_probability(lambd, k):
    return (lambd ** k) * math.exp(-lambd) / math.factorial(k)

lambd = 3
k = 3

prob_poisson = poisson_probability(lambd, k)
print("Probabilitas P(X=k) untuk distribusi Poisson", prob_poisson)


# In[4]:


from scipy.stats import poisson

lambd = 3
k = 2

prob_poisson = poisson.pmf(k, lambd)
print("Probabilitas P(X=k) untuk distribusi Poisson:", prob_poisson)


# In[ ]:





# In[5]:


from scipy import stats
X = stats.binom(15, 0.1)
print(X.pmf(3))


# In[6]:


print(X.cdf(2))


# In[7]:


print(X.pmf(6)+X.pmf(7))


# In[8]:


from scipy import stats
Y = stats.poisson(5)
print(Y.pmf(4))


# In[9]:


from scipy import stats 

X = stats.binom(20, 0.7)

pmf_15 = X.pmf(15)

print(pmf_15)


# In[10]:


from scipy import stats
Y = stats.poisson(2)

print(Y.pmf(3))


# In[11]:


from scipy import stats
X = stats.binom(15, 0.3)
print(X.pmf(5))


# In[ ]:




