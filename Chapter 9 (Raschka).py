#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pickle


# In[20]:


import os


# In[21]:


dest = os.path.join('movieclassifier', 'pkl_objects')


# In[22]:


if not os.path.exists(dest):
    os.makedirs(dest)


# In[28]:


pickle.dump('stop', open(os.path.join(dest, 'stopwords.pkl'), 'wb'), protocol = 4)


# In[29]:


pickle.dump('clf', open(os.path.join(dest, 'classifier.pkl'), 'wb'), protocol = 4)


# In[31]:


from vectorizer import vect


# In[ ]:




