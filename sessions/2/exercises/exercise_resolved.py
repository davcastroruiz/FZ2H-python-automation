#!/usr/bin/env python
# coding: utf-8

# In[2]:


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[3]:


driver = webdriver.Chrome()


# In[7]:


driver.get('http://localhost:8080/')


# In[8]:


redirect = driver.find_element(by=By.ID, value='redirect-me')


# In[9]:


redirect.click()


# In[ ]:




