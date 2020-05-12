#!/usr/bin/env python
# coding: utf-8

# In[3]:


import string
import time
from selenium import webdriver
driver = webdriver.Chrome()
url="http://google.com/?#q="
term=input("Enter the song name:")
lyrics=" lyrics"
driver.get(url+term+lyrics)
msg = driver.find_element_by_class_name("Oh5wg").text


# In[4]:


driver.get("https://web.whatsapp.com/")

name = input('Enter the name of user or group : ')

data= msg.splitlines()

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp')
g= len(data)
print (g)
for i in range (g):
    msg_box.send_keys(data[i])
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
    time.sleep(1)


# In[ ]:




