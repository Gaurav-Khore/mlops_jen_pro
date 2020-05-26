#!/usr/bin/env python
# coding: utf-8

# In[3]:


import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
server.login("28gauravkhore@gmail.com", "gauravkhore28")
server.sendmail("28gauravkhore@gmail.com"
                ,"akshaypatidar5@gmail.com"
                ,"akshay to call karna")
server.quit()


# In[ ]:




