#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[37]:


top10 = movie.sort_values('budget', ascending=False)              .groupby('title_year')['budget']              .apply(lambda x: x.iloc[:10].median() / 1e6)
        
top10_roll = top10.rolling(5, min_periods=1).mean()
top10_roll.tail()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




