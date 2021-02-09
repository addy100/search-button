#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time


# In[2]:


def search_result():
    bot = webdriver.GoogleChrome()
    bot.get("https://www.google.com/")
    time.sleep(7)
    window.quit()
    result = bot.find_element_name('q')
    result.clear()
    result.send_keys(entry1.get())
    result.send_keys(Keys.RETURN)
    
def facebook():
    print(" ")


# In[3]:


window = Tk()
window.geometry('500x300')
search = Label(window,text = "Hey! How are you?", font = 'times 16')
search.place(x=10, y=20)
entry1 = Entry(window)
entry1.place(x = 250, y = 200)

b1 = Button(window,trxt = "search", command = search_results, width = 14, bg = 'gray')
b1.place(x=140, y=60)

b2.Button(window, text='Facebok' command = facebook, width = 14, bg ='grey'
b2.place(x = 150, y=70)

window.mainloop()