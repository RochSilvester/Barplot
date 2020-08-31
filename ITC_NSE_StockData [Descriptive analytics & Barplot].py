#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[127]:


xl_file = pd.ExcelFile('C:/Users/SILVESTER/Desktop/BABI-Descriptive Analytics-WorkBook.xlsx')

ITC_NSE_StockData.head()


# # since there are problem occuring while importing objects with space so I removed and merged them in excel sheet
# 
# ## imported sheet name as dataframe [ITC_NSE_StockData]

# In[128]:


ITC_NSE_StockData.columns


# In[129]:


ITC_NSE_StockData.info()


# # calculating mean , median , mode for data set using command as 'describe'

# In[130]:


ITC_NSE_StockData.PrevClose.describe()


# In[102]:


ITC_NSE_StockData.OpenPrice.describe()


# In[103]:


ITC_NSE_StockData.HighPrice.describe()


# In[104]:


ITC_NSE_StockData.LowPrice.describe()


# In[105]:


ITC_NSE_StockData.LastPrice.describe()


# In[106]:


ITC_NSE_StockData.ClosePrice.describe()


# In[107]:


ITC_NSE_StockData.AveragePrice.describe()


# In[108]:


ITC_NSE_StockData.TotalTradedQuantity.describe()


# In[109]:


ITC_NSE_StockData.Turnover.describe()


# # importing boxplot
# 
# ## i have used 'showmeans = True' in order to show seperately mean and median 

# In[131]:


plt.boxplot(ITC_NSE_StockData['PrevClose'],showmeans=True);


# In[132]:


plt.boxplot(ITC_NSE_StockData['OpenPrice'],showmeans=True);


# In[133]:


plt.boxplot(ITC_NSE_StockData['HighPrice'],showmeans=True);


# In[134]:


plt.boxplot(ITC_NSE_StockData['LowPrice'],showmeans=True);


# In[135]:


plt.boxplot(ITC_NSE_StockData['LastPrice'],showmeans=True);


# In[136]:


plt.boxplot(ITC_NSE_StockData['ClosePrice'],showmeans=True);


# In[137]:


plt.boxplot(ITC_NSE_StockData['AveragePrice'],showmeans=True);


# In[144]:


plt.boxplot(ITC_NSE_StockData['TotalTradedQuantity'],showmeans=True);


# # In order to remove the outlayers 
# ### i have used '  'sym=' ' (none) to see it clearly

# In[141]:


plt.boxplot(ITC_NSE_StockData['TotalTradedQuantity'],showmeans=True,sym='');


# In[142]:


plt.boxplot(ITC_NSE_StockData['Turnover'],showmeans=True,sym='');


# In[143]:


plt.boxplot(ITC_NSE_StockData['NoofTrades'],showmeans=True,sym='');


# # End code

# In[ ]:




