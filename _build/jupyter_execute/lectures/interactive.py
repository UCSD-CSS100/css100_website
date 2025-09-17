#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Import statement: pandas is a "package"
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import statsmodels.formula.api as smf


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# In[3]:


df_spam = pd.read_csv("data/models/classification/email.csv")
df_spam.head(3)


# In[4]:


mod = smf.logit(data = df_spam, formula = "spam ~ num_char").fit()


# In[5]:


mod.params


# In[6]:


y_pred = mod.predict()


# In[7]:


plt.scatter(df_spam['num_char'], mod.predict())


# In[8]:


df_spam['spam'].value_counts() / len(df_spam)


# In[9]:


## Fit a model
mod_spam = smf.logit(data = df_spam, formula = "spam ~ winner + num_char + re_subj").fit()
## Get predictions
y_pred = mod_spam.predict()
y_pred[0:5]


# In[10]:


## Visualize predicted probabilities
sns.histplot(x = y_pred, alpha = .5)
plt.axvline(x = .5, linestyle = "dotted")


# In[11]:


labels_t5 = y_pred > .5
print("Proportion classified as spam: {x}".format(x = round(labels_t5.mean(), 4)))
print("Proportion actual spam: {x}".format(x = round(df_spam['spam'].mean(), 4)))
print("Accuracy: {x}".format(x = round(accuracy_score(labels_t5, df_spam['spam']), 2)))


# In[28]:


results = []
for t in np.arange(0, 1, .01):
    labels = y_pred > t
    accuracy = accuracy_score(labels, df_spam['spam'])
    results.append({'accuracy': accuracy, 't': t, 'pred_spam': labels.mean()})
df_results = pd.DataFrame(results)
sns.lineplot(data = df_results, x = "t", y = "accuracy", label = "Accuracy")
sns.lineplot(data = df_results, x = "t", y = "pred_spam", label = "Predicted proportion of spam")


# In[29]:


## Demo: true data
true_labels = np.array([1, 0, 0, 1, 0, 0])
## Demo: predicted labels
predicted_labels = np.array([1, 0, 1, 1, 0, 1])


# In[30]:


N = len(true_labels[true_labels==0])
print(N)


# In[31]:


FP = len(predicted_labels[(predicted_labels==1) & (true_labels == 0)])


# In[34]:


FP / N


# In[35]:


## Number of true negatives
P = len(true_labels[true_labels==1])
## Number of FP
FN = len(predicted_labels[(predicted_labels==0) & (true_labels == 1)])


# In[36]:


FN / P


# In[ ]:




