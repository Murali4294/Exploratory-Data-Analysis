# #1 what is EDA: eda is data exploration technique to understand the various aspects of the data
# 
# #2 objective of eda: it is basically used to filter the data from redundacnies.
# 
# #3 steps involved in eda : it follows a systematic set of explore the data in the most efficient way possible 1)understand the data
# 2)clean the data 3) analysis of relationship between variables

# In[50]:


import pandas as pd
import numpy as np
import seaborn as sns


#  load the data

# In[51]:


data = pd.read_csv("D:/Muralidhar nagar/amazon_sales_data 2025.csv")


# In[6]:


#1 understand the data


# In[52]:


data.head()


# In[53]:


data.tail()


# In[54]:


data.shape # data.shape representing the dimensions of the DataFrame. It tells you:(number of rows, number of columns)


# In[55]:


data.describe() # When you call data.describe() on a DataFrame it summarizes the statistics of the data


# In[56]:


data.columns #  containing all the column names of your DataFrame.


# In[57]:


data.nunique() # data.nunique() counts the number of unique (distinct) values in each column of your DataFrame.


# In[58]:


data['Product'].unique() # It returns an array of all the unique values present in the indivisual column.


# In[59]:


data['Customer Location'].unique()


# In[ ]:


#2 cleaning the data


# In[60]:


data.isnull().sum()


# In[ ]:


# axis=0 is like "move down" (rows) axis=1 is like "move across" (columns)


# In[61]:


Amazon = data.drop(['Customer Location','Payment Method'],axis = 1)


# In[62]:


Amazon


# In[63]:


Amazon.head()


# In[ ]:


# 3 Relationship analysis


# In[64]:


corelation = Amazon.corr()


# In[65]:


sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns,annot = True)


# In[38]:


sns.pairplot(Amazon) 


# In[41]:


sns.relplot(x='Price',y='Total Sales',hue = 'Status',data = Amazon)


# In[49]:


sns.distplot(Amazon['Total Sales'],bins = 5)


# In[69]:


sns.catplot(x='Price',kind = 'box',data= Amazon)

