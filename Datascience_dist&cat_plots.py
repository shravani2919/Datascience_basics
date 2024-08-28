#!/usr/bin/env python
# coding: utf-8

# In[3]:



get_ipython().system('pip install --upgrade numpy')


# In[4]:


get_ipython().system('pip install seaborn')


# In[5]:


get_ipython().system('pip install --upgrade numpy scipy')


# In[6]:


import seaborn as sns


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


tips = sns.load_dataset('tips')


# In[9]:


tips.head()


# In[10]:


sns.distplot(tips['total_bill'], kde = False, bins =100)


# In[11]:


sns.jointplot(x='total_bill',y='tip',data=tips)


# In[12]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind = 'hex')


# In[13]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind = 'reg')


# In[14]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind = 'kde')


# In[15]:


sns.pairplot(tips)


# In[16]:


sns.pairplot(tips, hue = 'sex')


# In[17]:


sns.pairplot(tips, hue = 'sex',palette = 'coolwarm')


# In[18]:


sns.rugplot(tips['total_bill'])


# In[19]:


sns.distplot(tips['total_bill'], kde = False) 
#kernal distination plot kde


# # Categorical plots
# 

# In[20]:


tips = sns.load_dataset('tips')
tips.head()


# In[21]:


sns.barplot(x= 'sex', y ='total_bill', data = tips)


# In[22]:


import numpy as np


# In[23]:


sns.barplot(x= 'sex', y ='total_bill', data = tips,estimator =  np.std )


# In[24]:


sns.countplot(x ='sex', data = tips)


# In[25]:


sns.boxplot(x ='day', y='total_bill', data = tips)


# In[26]:


sns.boxplot(x ='day', y='total_bill', data = tips)


# In[27]:


sns.violinplot(x ='day', y='total_bill', data = tips)


# In[28]:


sns.violinplot(x ='day', y='total_bill', data = tips,hue='sex')


# In[29]:


sns.violinplot(x ='day', y='total_bill', data = tips,hue='sex',split=True)



# In[30]:


sns.stripplot(x ='day', y='total_bill', data = tips)


# In[31]:


sns.stripplot(x ='day', y='total_bill', data = tips, jitter = True,hue = 'sex',dodge=True)
# jitter is used to separate the points sticked on one other
# dodge is something like split


# In[32]:


sns.swarmplot(x ='day', y='total_bill', data = tips)
# combination of scatter plot vloin plot and box plot


# In[33]:


sns.violinplot(x ='day', y='total_bill', data = tips)
sns.swarmplot(x ='day', y='total_bill', data = tips, color ='black')


# In[34]:


sns.factorplot(x ='day', y='total_bill', data = tip,kind='bar')
#gemeral form all the data


# In[63]:


sns.catplot(x='day', y='total_bill', data=tips, kind='bar')
# above code is not working so use cat plot


# # Matrix plots

# In[35]:


tips=sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()


# In[36]:


flights.head()


# # heat maps

# heat maps to work data always should be in  matrixs from
# 

# In[37]:


tips.corr()


# In[39]:


numeric_df = tips.select_dtypes(include=[np.number])
tc = numeric_df.corr()
tc
# above case is not executed because non numeric values are preset so they shouls br eleminated


# In[40]:


sns.heatmap(tc) 
#for heat map we need to use array


# In[41]:


sns.heatmap(tc,annot=True) 


# In[42]:


sns.heatmap(tc,annot=True,cmap='coolwarm') 


# # pivot table

# In[43]:


flights.pivot_table(index = 'month',columns='year',values='passengers')


# In[50]:


#lets create a heat map
ht = flights.pivot_table(index = 'month',columns='year',values='passengers')
sns.heatmap(ht,cmap='magma',linecolor='white',linewidths=5)


# In[51]:


sns.heatmap(ht,cmap='coolwarm',linecolor='white',linewidths=5)


# In[54]:


sns.clustermap(ht,cmap='coolwarm',standard_scale=1)


# 

# In[55]:


iris = sns.load_dataset('iris')
iris.head()


# In[56]:


iris


# In[57]:


iris['species'].unique()
# to check what are the species present
# three types of species are present


# # grid
# 

# In[59]:


sns.pairplot(iris)


# # pair grid

# In[66]:


g=sns.PairGrid(iris)
g.map_diag(sns.displot)
# g.map_upper(plt.scatter) # this code maynot work
g.map_lower(sns.kdeplot)
# don't flow this codes are correct but plots are not correct


# In[67]:


tips.head()


# In[70]:


g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(sns.displot,'total_bill')
# iam not sure what happening but plots should be in the grid


# # Regression plot(lm plots)

# In[85]:


sns.lmplot(x='total_bill', y='tip',data= tips,hue='sex', markers=['v','o'],
              scatter_kws= {'s':100})
#scatter_kws changes the size of the markers


# In[87]:


sns.lmplot(x='total_bill', y='tip',data= tips,col='sex', row='time')
# separated by column


# In[89]:


sns.lmplot(x='total_bill', y='tip',data= tips,col='day', row='time',hue='sex')
# separated by column


# In[90]:


sns.lmplot(x='total_bill', y='tip',data= tips,col='day',hue='sex')


# In[94]:


sns.lmplot(x='total_bill', y='tip',data= tips,col='day',hue='sex',
          aspect= 0.6)
#change the ration


#  Style and color (where we learn how to colour and style the graph)

# In[95]:


sns.set_style('ticks')
sns.countplot(x ='sex',data=tips)
#plt.figure(figsize=(12,4)) right now this command is not working used to change the size of the figure


# In[97]:


# remove the outliners
sns.set_style('ticks')
sns.countplot(x ='sex',data=tips)
sns.despine(left=True,bottom=True)


# In[101]:


sns.set_context('poster') # compare to the above size it chamges it changes to th poster size
sns.countplot(x ='sex',data=tips)


# In[103]:


sns.set_context('poster', font_scale=2) #size of the poster changes
sns.countplot(x ='sex',data=tips)


# In[104]:


sns.set_context('notebook') 
sns.countplot(x ='sex',data=tips)


# In[106]:


sns.lmplot(x='total_bill', y='tip',data= tips,hue='sex',palette='coolwarm')


# In[107]:


sns.lmplot(x='total_bill', y='tip',data= tips,hue='sex',palette='seismic')


# In[ ]:




