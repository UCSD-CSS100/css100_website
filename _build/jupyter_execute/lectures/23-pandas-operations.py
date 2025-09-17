#!/usr/bin/env python
# coding: utf-8

# # Basic operations with `pandas`

# ## Goals of this lecture
# 
# Previously, we discussed why [`pandas.DataFrame`](22-pandas) is so useful for representing data.
# 
# In today's lecture, we'll cover:
# 
# - How to **read in** a `.csv` file as a `DataFrame` using `pandas.read_csv`. 
# - Sorting a `DataFrame` with `sort_values`.
# - Basic **descriptive statistics** with `pandas` (`mean()`, etc.)
# - Creating a new **column** of a `DataFrame`. 
# 

# In[1]:


### Always remember to import the package!
import pandas as pd


# ## Review: What is tabular data?
# 
# > [Tabular data](https://www.statology.org/tabular-data/) is data organized in a **table** with *rows* and *columns*.
# 
# - This kind of data is **two-dimensional**.  
# - Typically, each **row** represents an "observation".
#   - A person.
#   - A country.  
#   - An experimental trial.
# - Typicallly, each **column** represents an *attribute*.  
#   - `height`
#   - `gdp` or `population`
#   - `reaction_time` or `experimental_condition`
# 

# ### Example: test scores
# 
# **Check-in**: What are the **columns** of this table?
# 
# | Participant | Score |
# | ------- | ----- |
# | 1  | 85| 
# | 2  | 92| 
# | 3  | 78| 
# | 4  | 98| 
# | 5  | 76| 

# ## Reading in a `.csv` file
# 
# > A `.csv` file is a **comma-separated values** file.
# 
# Tabular data is often represented in a `.csv` file.
# 
# - The values of each column are separated by a comma (`1,85`). 
# - Each row is represented by a new line.
# 
# A `.csv` file can also be opened in Excel or Google Sheets.

# ### Review: file paths
# 
# [Previously, we've discussed how a **file path** represents the "location" of a file on your computer](17-reading-text).
# 
# - An **absolute** file path specifies the location of a file relative to some **root** directory.
# - A **relative** file path specifies the location of a file relative to the **current** directory (i.e., the one you're in right now). 
# 
# We already know how to read in `.txt` and `.json` files, but `.csv` files are new.

# ### A sample `.csv` file 
# 
# The `data` directory contains a file called `scores_sample.csv`. 
# 
# For a series of made-up research participants, this file contains:
# 
# - The student number.
# - Their score on a reading comprehension task.
# 
# Now we need to read this file in!

# #### Check-in
# 
# If we're currently in `lectures`, and the file is in `lectures/data/scores_sample.csv`, what would the relative file path be?

# #### Solution
# 
# The filepath would be: `data/scores_sample.csv`

# ### Using `read_csv`
# 
# `pandas.read_csv` takes in a **filepath** as an argument, and returns a `DataFrame`.

# In[2]:


## Pass the filepath into pd.read_csv
df_scores = pd.read_csv("data/scores_sample.csv")


# In[3]:


## Let's inspect the first couple of rows
df_scores.head(2)


# #### Check-in
# 
# What are the **column names** of this `DataFrame`? What does each **row** represent?

# In[4]:


df_scores.head(5)


# #### Check-in
# 
# How would we figure out how many rows and columns this `DataFrame` has?

# In[5]:


### Your code here


# #### Solution

# In[6]:


## First number = number of rows
## Second number = number of columns
df_scores.shape


# #### Check-in
# 
# Now let's try to read in a **new** `.csv` file. This one is also located in `data`, and it's called `housing.csv`. 
# 
# - The original data can be found on [Kaggle, a website for data science competitions](https://www.kaggle.com/datasets/camnugent/california-housing-prices?resource=download)).
# - It aggregates across houses on a **block**.
# 
# Call the new `DataFrame` `df_housing`.

# In[7]:


### Your code here


# #### Solution

# In[8]:


df_housing = pd.read_csv("data/housing.csv")
df_housing.head(2)


# In[9]:


df_housing.shape


# ## Sorting a `DataFrame`
# 
# Often, we might find it useful to **sort** a `DataFrame` according to the values in a particular column.

# ### `sort_values`
# 
# - By default, `sort_values` will sort from *lowest* to *highest*.

# In[10]:


df_scores.sort_values("Score").head(2)


# In[11]:


df_scores.sort_values("Score").tail(2)


# ### `ascending = False`
# 
# We can change that with the `ascending` parameter.

# In[12]:


df_scores.sort_values("Score", ascending = False).head(2)


# ### Check-in
# 
# Use `sort_values` to find the block with the *lowest* `median_house_value`. Then, answer the following questions:
# 
# - What is the `ocean_proximity` of this block?  
# - What is the `median_income` of this block?  
# - How many `households` are on this block?

# In[13]:


### Your code here


# ### Solution

# In[14]:


df_housing.sort_values("median_house_value").head(1)


# ### Check-in
# 
# Use `sort_values` to find the block with the *highest* `median_house_value`. Then, answer the following questions:
# 
# - What is the `ocean_proximity` of this block?  
# - What is the `median_income` of this block?  
# - How many `households` are on this block?

# In[15]:


### Your code here


# ### Solution

# In[16]:


df_housing.sort_values("median_house_value", ascending = False).head(1)


# ## Basic descriptive statistics in `pandas`
# 
# > **Descriptive statistics** are ways to summarize and organize data.
# 
# - We've already covered [using `numpy` to calculate **descriptive statistics**](21-numpy-advanced).  
# - But we can also use `pandas` in a very similar way!
#    - (A *column* of a `DataFrame` is roughly analogous to a `numpy.ndarray`.)

# ### `sum`
# 
# > The **sum** of a set of numbers is simply the result of adding each number together.
# 
# The `sum` of a column can be calculated by calling:
# 
# ```python
# df_name[column_name].sum()
# ```

# In[17]:


df_scores['Score'].sum()


# ### `mean`
# 
# > The **mean** of a set of scores is the *sum* of those scores divided by the number of the observations.
# 
# The `mean` of a column can be calculated by calling:
# 
# ```python
# df_name[column_name].mean()
# ```

# In[18]:


df_scores['Score'].mean()


# ### `describe`
# 
# The `describe` function gives you a bunch of handy descriptive statistics in a single call.

# In[19]:


df_scores['Score'].describe()


# ### Check-in
# 
# What is the mean number of `households` per block in our housing dataset? What about the minimum and maximum?

# In[20]:


### Your code here


# ### Solution

# In[21]:


print(df_housing['households'].mean())
print(df_housing['households'].max())
print(df_housing['households'].min())


# ### Check-in
# 
# What is the mean `median_income` per block in our housing dataset? What about the minimum and maximum?

# In[22]:


### Your code here


# ### Solution

# In[23]:


print(df_housing['median_income'].mean())
print(df_housing['median_income'].max())
print(df_housing['median_income'].min())


# ### Check-in
# 
# Could we calculate the `mean` of the `ocean_proximity` variable? Why or why not?

# In[24]:


### Your code here


# ### Solution
# 
# No, because `ocean_proximity` is a **qualitative** variable. We can only count how many of each *category* there are.

# In[25]:


df_housing['ocean_proximity'].value_counts()


# ## Creating a new column
# 
# `pandas` also makes it relatively easy to make a new column.
# 
# Syntax:
# 
# ```python
# dataframe_name[new_column_name] = ...
# ```

# In[26]:


### Setting the column to a single value 
### just duplicates that value throughout the column
df_scores['Researcher'] = 'Bergen'


# In[27]:


df_scores.head(2)


# ### Using an existing column to make a new column
# 
# You can also use values in an **existing** column to make a new column.
# 
# - Example: a new column called `Pass` that encodes whether a score is `>= 70`.

# In[28]:


df_scores['Pass'] = df_scores['Score'] >= 70


# In[29]:


df_scores.head(2)


# ### Check-in
# 
# Create a new column of `df_housing` that calculates the **ratio** between the `population` of a block and the number of `households` on that block.

# In[30]:


### Your code here


# ### Solution

# In[31]:


df_housing['pop_per_household'] = df_housing['population'] / df_housing['households']
df_housing.head(2)


# ## Conclusion
# 
# This concludes our second lecture on `pandas`. Now you know:
# 
# - How to read in a `.csv` file with `read_csv`.  
# - How to calculate basic descriptive statistics with `pandas`.  
# - How to sort a `DataFrame` and create a new column.
