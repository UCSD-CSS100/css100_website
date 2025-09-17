#!/usr/bin/env python
# coding: utf-8

# # Calculating the *standard error* of our coefficients

# **Very important**:
# 
# The correct formula for calculating standard error of our coefficient is:
# 
# $\Large SE(\beta_1) = \frac{S_{Y|X}}{\sqrt{SS_X}} = \sqrt{\frac{\frac{1}{n-2}RSS}{SS_X}}$

# In[1]:


np.sqrt(mod.scale) / np.sqrt(ss_x)


# In[ ]:




