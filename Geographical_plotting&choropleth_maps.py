#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install chart-studio


# In[4]:


pip install --upgrade numpy chart-studio


# In[43]:


import chart_studio.plotly as py
import plotly.graph_objs as go


# In[44]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[45]:


init_notebook_mode(connected=True)


# In[46]:


data =  dict(type='choropleth', locations=['AZ','CA','NY'], locationmode ='USA-states', colorscale='Portland',
            text=['shrava','ni','thall'],
            z= [1.0, 2.0, 3.0],
            colorbar = {'title':'colorbar title goes here'})


# In[47]:


data


# In[48]:


layout = dict(geo={'scope':'usa'})


# In[49]:


choromap = go.Figure(data=[data], layout=layout)


# In[50]:


iplot(choromap)


# In[51]:


data =  dict(type='choropleth',
             locations=['AZ','CA','NY'],
             locationmode ='USA-states', 
             colorscale='Greens',
             text=['shrava','ni','thall'],
             z= [1.0, 2.0, 3.0],
             colorbar = {'title':'colorbar title goes here'})


# In[52]:


layout = dict(geo={'scope':'usa'})
choromap = go.Figure(data=[data], layout=layout)
iplot(choromap)


# In[53]:


import pandas as pd
df=pd.read_csv('2011_US_AGRI_Exports')


# In[54]:


df.head()


# In[61]:


import plotly.graph_objs as go

# Define the layout using go.Layout
layout = go.Layout(
    title='2011 US Agriculture Exports by States',  # Set the title
    geo=dict(
        scope='usa',           # Focus on the USA
        showlakes=True,        # Display lakes
        lakecolor='rgb(85, 173, 240)'  # Set the color of the lakes
    )
)

# Example data for the choropleth
data = dict(
    type='choropleth',
    colorscale='YlOrRd',  # Correct colorscale
    locations=df['code'],  # State codes
    locationmode='USA-states',  # Location mode for USA states
    z=df['total exports'],  # Data to map
    text=df['text'],  # Text to display on hover
    marker=dict(
        line=dict(
            color='rgb(12,12,12)',  # Marker line color
            width= 4  # Marker line width
        )
    ),
    colorbar={'title': 'Millions USD'}  # Colorbar title
)

# Create the figure using the data and layout
choromap = go.Figure(data=[data], layout=layout)

# Display the figure
choromap.show()


# International maps
# 

# In[63]:


df = pd.read_csv('2014_World_GDP')


# In[64]:


df.head()


# In[75]:





import plotly.graph_objs as go

# Define the data using go.Choropleth
data = go.Choropleth(
    colorscale='YlOrRd',  # Correct colorscale
    locations=df['CODE'],  # State codes
    locationmode='USA-states',  # Location mode for USA states
    z=df['GDP (BILLIONS)'],  # Data to map
    text=df['COUNTRY'],  # Text to display on hover
    marker=dict(
        line=dict(
            color='rgb(12,12,12)',  # Marker line color
            width=4  # Marker line width
        )
    ),
    colorbar=dict(title='GDP (Billions USD)')  # Colorbar title
)

# Define the layout using go.Layout
layout = go.Layout(
    title='2014 GDP by State',  # Set the title
    geo=dict(
        scope='usa',             # Focus on the USA
        showframe=False,         # Hide the frame around the map
        projection=dict(type='mercator')  # Correct projection type
    )
)

# Create the figure using the data and layout
choromap3 = go.Figure(data=[data], layout=layout)

# Display the figure
choromap3.show()


# In[76]:


iplot(choromap3)


# In[ ]:




