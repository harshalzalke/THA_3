
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[11]:


aid_data = pd.read_csv("C:/Users/harsh/Desktop/Courses/LBJ_Spring19/Database Management/THA3/US_aid_pakistan.csv")


# In[30]:


ter_pak = pd.read_csv("C:/Users/harsh/Desktop/Courses/LBJ_Spring19/Database Management/THA3/terrorist_incidents_pakistan.csv")


# In[31]:


merge = ter_pak.merge(aid_data, on="Year", how="inner")
print(merge)


# In[32]:


merge.to_csv("C:/Users/harsh/Desktop/Courses/LBJ_Spring19/Database Management/THA3/complied_dataset.csv", index=False)

