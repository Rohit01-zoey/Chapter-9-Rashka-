#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route('/')
def index():
    return render_template('/home/rohit/1st_flask_app_1/templates/first_app')


# In[ ]:


if __name__ == '__main__':
    app.run()


# In[ ]:




