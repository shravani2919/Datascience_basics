#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install numpy')


# In[3]:


import pandas as pd
import numpy as np


# In[11]:


import seaborn as sns


# In[24]:


df1 = pd.read_csv('df1',index_col = 0)


# In[25]:


df1.head()


# In[26]:


df2 = pd.read_csv('df2')


# In[27]:


df2.head()


# In[28]:


df1['A'].hist()


# In[29]:


df1['A'].hist(bins=50)


# In[30]:


df1['A'].plot(kind='hist',bins=50) # 
# similar to above graph but diff code


# In[31]:


df1['A'].plot.hist()


# In[32]:


df2.plot.area()# area plot


# In[33]:


df2.plot.area(alpha=0.4)
# changes the transparance


# In[34]:


df2.plot.bar(alpha=0.4)


# In[35]:


df2.plot.bar(alpha=0.4,stacked=True)


# In[41]:


df1.plot.line(y='B', figsize=(12, 3),lw=1)



# In[42]:


df1.plot.scatter(x='A',y='B')


# In[45]:


df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm')


# In[50]:


df1.plot.scatter(x='A',y='B',s=df1['C']*50)
# gives as vth respective size


# In[51]:


df1.plot.box()


# In[52]:


df = pd.DataFrame(np.random.randn(1000, 2),columns=['a', 'b'])


# In[58]:


df.plot.hexbin(x='a',y='b',gridsize=10,cmap='coolwarm')


# In[60]:


# kernel density estimation plots
df2['a'].plot.kde()


# In[61]:


df2['a'].plot.density() # both codes are same


# In[62]:


df2.plot.density()


# # Exercise
# 

# In[63]:


df3 = pd.read_csv('df3')
df3.head()


# In[64]:


df3.info()


# In[71]:


df3.plot.scatter(x='a',y='b', color ='r',s=50,figsize=(12,3))


# In[76]:


df3['a'].hist()


# In[78]:


df3['a'].hist(bins=100)


# In[84]:


import matplotlib.pyplot as plt
plt.style.use('ggplot')
df3['a'].hist(bins=100 ,alpha=0.5)


# In[ ]:




