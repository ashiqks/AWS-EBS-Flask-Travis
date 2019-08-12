#!/usr/bin/env python
# coding: utf-8

# In[8]:


from flask import Flask
application = Flask(__name__)


@application.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    application.run()

