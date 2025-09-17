#!/usr/bin/env python
# coding: utf-8

# # Polynomial regression

# ## Goals of this lecture
#  
# - Non-linear relationships: why do we care?  
# - Accommodating non-linear relationships in the **linear regression equation**.  
# - Challenges with polynomial regression:
#    - Over-fitting.  
#    - Bias-variance trade-off.

# In[ ]:





# In[ ]:





# In[1]:


mod_poly = smf.ols(data = df_housing,
                     formula = "median_house_value ~ housing_median_age + I(housing_median_age**2) + I(housing_median_age**3)").fit()


# In[1]:


### Explanation: https://stackoverflow.com/questions/32484244/reciprocals-in-patsy/36539093#36539093


# See chapter 7 of ISLR.

# Other problems (ISLR, pg. 93):
# 
# 1. Non-linearity
# 2. Correlation of error terms
# 3. Heteroscedasticity
# 4. Outliers
# 5. High-leverage points
# 6. Collinearity

# In[ ]:




