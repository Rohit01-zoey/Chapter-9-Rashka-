#!/usr/bin/env python
# coding: utf-8

# In[8]:


from sklearn.feature_extraction.text import HashingVectorizer


# In[9]:


import re
import os
import pickle


# In[10]:


cur_dir = os.path.dirname(__file__)


# In[11]:


stop = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'stopwords.pkl'), 'rb'))


# In[12]:


def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized


# In[13]:


vect = HashingVectorizer(decode_error = 'ignore', n_features = 2**21, preprocessor = None, tokenizer = tokenizer)


# In[ ]:




