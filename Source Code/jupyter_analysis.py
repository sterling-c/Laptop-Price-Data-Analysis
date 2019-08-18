#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


pwd


# In[3]:


laptop_data = pd.read_csv("C:/Users/sclark18/Documents/Data Projects/Project 1/Data/laptops.csv", encoding='latin-1')
laptop_data.head()


# In[4]:


list(laptop_data.columns)


# In[5]:


laptop_data = laptop_data.drop(columns="Unnamed: 0")
laptop_data.tail()


# In[6]:


laptop_data = laptop_data.rename(columns={"Ram": "RAM(in GB)", "TypeName": "Product Type", "Inches": "Length(in inches)", "Weight": "Weight(in kg)", "Price_euros": "Price(in euros)"})
laptop_data.tail()


# In[7]:


laptop_data = laptop_data.rename(columns={"Ram": "RAM (in GB)", "Inches": "Length (in inches)", "Weight": "Weight (in kg)", "Price_euros": "Price (in euros)"})
laptop_data.tail()


# In[8]:


laptop_data = laptop_data.rename(columns={"Memory": "Storage Memory"})


# In[9]:


laptop_data.tail()


# In[10]:


laptop_data['Weight(in kg)'] = laptop_data['Weight(in kg)'].str.strip('kg')


# In[11]:


laptop_data['Price(in euros)'] = laptop_data['Price(in euros)'].round(2)
laptop_data.head()


# In[12]:


laptop_data.head()


# In[13]:


# This was an attempt to reformat some of the data within panda dataframe for clarification and consistency.
# We will write a new CSV file using the current format of the dataframe, then move on with the actual analysis. 


# In[32]:


laptop_data.to_csv("C:/Users/sclark18/Documents/Data Projects/Project 1/Data/laptops_clean.csv")


# In[14]:


# Now we will compare each company's average price.


# In[15]:


company_list = laptop_data['Company'].unique().tolist()


# In[16]:


print(company_list)


# In[17]:


average_price = []


# In[18]:


avg_dict = {}
for company in company_list:
    product_count = 0
    price_sum = 0
    for index, row in laptop_data.iterrows():
        if(row['Company'] == company):
            product_count = product_count + 1
            price_sum = price_sum + row['Price(in euros)']
    avg_price = format(price_sum/product_count, '.2f')
    avg_dict[company] = avg_price


# In[19]:


print(avg_dict)


# In[20]:


company_price_compare = pd.DataFrame.from_dict(avg_dict, orient='index')


# In[21]:


company_price_compare


# In[31]:


list(company_price_compare.columns)


# In[30]:


company_price_compare = company_price_compare.rename(columns={0: "Price (in euros)"})


# In[32]:


company_price_compare


# In[40]:


import matplotlib.pyplot as plt
df=company_price_compare.astype(float)
ax = df[['Price (in euros)']].plot.bar()
ax.set_xlabel("Companies", fontsize=12)
ax.set_ylabel("Price(in euros)", fontsize=12)
plt.show()


# In[ ]:




