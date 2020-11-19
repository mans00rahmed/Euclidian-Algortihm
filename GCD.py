#!/usr/bin/env python
# coding: utf-8

# # To find GCD of two numbers using eucledian algorithm

# In[28]:


def gcd(a,b):
    if b==0:
        print (a)
    else:
        gcd(b,a%b)
    
#driver code
gcd(36,10)


# In[ ]:




