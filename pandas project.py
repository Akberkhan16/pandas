#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


import pandas as pd


# In[4]:


# Assign it to a variable called users and use the 'user_id' as index

users = pd.read_csv(r'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep ='|', index_col = 0)
users.head()


# In[5]:


# See the first 10 
users.head(10)


# In[6]:


# and last 10 entries
users.tail(10)


# In[7]:


# What is the number of observations in the dataset?
len(users)


# In[8]:


# What is the number of columns in the dataset?
print(users.shape[1])


# In[9]:


# Print the name of all the columns.
print(users.columns)


# In[11]:


# How is the dataset indexed
print(users.index)


# In[12]:


# What is the data type of each column?
users.dtypes


# In[13]:


# Print only the occupation column
users['occupation']


# In[14]:


# How many different occupations are in this dataset?
users['occupation'].nunique()


# In[15]:


# What is the most frequent occupation?
users['occupation'].mode()


# In[16]:


# DataFrame Info.
users.info()


# In[17]:


# Describe all the columns
users.describe()


# In[18]:


# Summarize only the occupation column
users['occupation'].value_counts()


# In[19]:


# What is the mean age of users
users['age'].mean()


# In[20]:


# What is the age with least occurrence?
users['age'].min()


# In[ ]:




