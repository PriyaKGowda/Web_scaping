#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[11]:


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995#.YNlyjOgzZPY')
soup = BeautifulSoup(page.content,'html.parser')
print(soup)


# In[12]:


week = soup.find(id="seven-day-forecast-body")
print(week)


# In[19]:


items = week.find_all(class_='tombstone-container')
print(items[0])


# In[22]:


print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())


# In[24]:


period_names = [item.find(class_='period-name').get_text() for item in items]
print(period_names)


# In[28]:


short_description = [item.find(class_='short-desc').get_text() for item in items]
print(short_description)


# In[29]:


temperature = [item.find(class_='temp').get_text() for item in items]
print(temperature)


# In[37]:


weather_stuff = pd.DataFrame({
                              'period':period_names, 
                              'short_description':short_description,
                              'temperature':temperature,})
print(weather_stuff)


# In[38]:


weather_stuff.to_csv('weather.csv')


# In[ ]:




