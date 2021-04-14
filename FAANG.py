#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as plt


# In[5]:


pd.read_excel('FAANG stock.xlsx')


# In[7]:


df=pd.read_excel('FAANG stock.xlsx')
df.head()


# In[8]:


df.shape


# In[9]:


import plotly.express as px


# In[10]:


fig=px.box(df,y=['GOOG', 'NFLX', 'FB', 'AMZN', 'AAPL'])
fig.show()


# In[ ]:




