#!/usr/bin/env python
# coding: utf-8

# In[27]:


import string
import time
from selenium import webdriver
driver = webdriver.Chrome()
url="http://google.com/?#q="
term=input("Enter the song name:")
lyrics=" lyrics"
driver.get(url+term+lyrics)


user = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div').click()
time.sleep(1)
msg = driver.find_element_by_class_name("uHNKed").text
print(msg)


# In[ ]:




driver.get("https://web.whatsapp.com/")

name = input('Enter the name of user or group : ')

data= msg.splitlines()
while ("" in data) :
    data.remove("")

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/span'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp')
print(data)

g= len(data)
print (g)
for i in range (g):
    msg_box.send_keys(data[i])
    time.sleep(1)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
    time.sleep(1)


# In[ ]:




