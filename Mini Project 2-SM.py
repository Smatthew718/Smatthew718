#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[28]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[41]:


df = pd.read_csv('https://raw.githubusercontent.com/niteen11/DataAnalyticsAcademy/master/Python/dataset_diabetes/diabetic_data.csv')


# In[42]:


df


# In[5]:


#Check data size


# In[6]:


df.shape


# In[7]:


df.describe()


# In[8]:


# Review data types in data set


# In[9]:


df.dtypes


# In[10]:


#Check for null values


# In[11]:


df.isnull().sum()


# In[12]:


#Count by patient number to see if a patient would have more than encounters


# In[13]:


df.groupby(['patient_nbr']).count()


# In[14]:


#Count to see which gender


# In[15]:


df.groupby(['race'])['num_procedures'].sum()


# In[ ]:


# Data shows the race "Other" on average have more prodecures but overall Causasians #1


# In[66]:


sns.barplot(x="race", y="num_procedures", data=df)


# In[32]:


sns.pairplot(data=df2)


# In[ ]:





# In[ ]:


#created custom database df2


# In[17]:


df2= df[['patient_nbr','race','gender','age','time_in_hospital','insulin']]


# In[18]:


df2


# In[ ]:


#Grouped by race and time in hosiptal. Data show on average African Americans spend more time in hospitals


# In[64]:


df2.groupby(['gender'])['time_in_hospital'].mean()


# In[63]:


sns.plot(x="gender", y="time_in_hospital", data=df2)


# In[21]:


#Grouped by race and time in hospital. Data shows overall Caucasins spend the most time in the hospital and Asians the least.


# In[22]:


df2.groupby(['race'])['time_in_hospital'].count()


# In[23]:


#Barplot shows on average African Americans have a slightly higher average stay in the hospital overall than all other races


# In[24]:


sns.barplot(x="race", y="time_in_hospital", data=df2)


# In[43]:


df


# In[ ]:


#Data based created to display only African Americans race


# In[44]:


df3=df[df['race'].str.contains('AfricanAmerican')]


# In[45]:


df3


# In[ ]:


#Grouped by gender displaying number of procedures between African American men and women. Women show they have far more lab procedure done.


# In[60]:


df3.groupby(['gender'])['num_lab_procedures'].count().plot(kind="bar")


# In[ ]:





# In[ ]:




