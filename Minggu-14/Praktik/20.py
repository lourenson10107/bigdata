#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


movie_count = movie.groupby('title_year')['budget'].count()
movie_count.tail()


# In[ ]:




