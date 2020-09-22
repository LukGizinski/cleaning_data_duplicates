#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[ ]:


df = pd.read_csv(xyz.csv)


# In[ ]:


#Duplicates
#to check how many duplicated ther is
sum(df.duplicated())

