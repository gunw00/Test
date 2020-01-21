#!/usr/bin/env python
# coding: utf-8

# In[1]:


#positive.py
def positive(l) :
    result=[]
    for i in l:
        if i>0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))


# In[ ]:




