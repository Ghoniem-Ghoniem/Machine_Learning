#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pickle
pkl_filename = "pickle_model.pkl"

# Load from file
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)
    
Ypredict = pickle_model.predict([[2010,200,3]])
Ypredict

