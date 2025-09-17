#!/usr/bin/env python
# coding: utf-8

# # Data Structures with `pandas`

# ## Goals of this lecture
# 
# In this lecture, we'll introduce the `pandas` package, a really useful way to represent **tabular data** in Python.
# 
# Topics will include:
# 
# - What is **data**? 
# - What is **tabular data**?  
# - Why not use a `list`, a `dict`, or `numpy`? 
# - Introducing **`pandas`**: an efficient way to store data tables.  
# - Basics of **`pandas.DataFrame`**: creating and indexing `DataFrame`s. 

# ## What is data?
# 
# > **Data** is a collection of *values* conveying information. This includes quantitative values (e.g., `height`, `income`, etc.) and qualitative values (e.g., `major`, `favorite food`, etc.). 
# 
# All empirical sciences rely on *data* of some kind. Can you think of examples of **data** from your own field?

# ### Data across social science disciplines
# 
# - **Linguistics**: conversation transcripts, text corpora, audio recordings, etc.
# - **Psychology**: reaction time, fMRI recordings, etc.
# - **Political Science**: opinion polls, voting records, etc.
# - **Economics**: GDP, unemployment rate, labor surveys, etc.
# - **Sociology**: immigration statistics, wealth distribution, etc.
# 
# And lots more!

# ### Representing data
# 
# - Importantly, data must be **represented** somehow: how to do this?  
# - Further, we often have **multiple sources of data**.
#    - Example: `population` and `GPD` are two different measures we can calculate for each country.
#    - Can't just represent with a single vector: it's at least **two-dimensional**.
#    - We need a way to represent this **N-dimensional** data.

# ## What is tabular data?
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

# ### Example 1: Economic connectedness
# 
# In lecture 1, we looked at this figure showing the relationship between **Economic Connectedness** and **Predicted Income Rank** across counties.
# 
# ![title](img/chetty_2022.png)

# ### Example 1 as tabular data
# 
# To run this analysis (and plot the figure), the authors had to **represent** these data.
# 
# For example, [their data](https://opportunityinsights.org/) includes *at least*:
# 
# | County | Connectedness | Population | Predicted Income Rank |
# | ------- | ---------- | --- | ---- |
# | San Francisco, California     | 1.31       | 870044 | 51 |
# | New York, New York   | 0.83  | 1632480 | 42 | 

# ### Example 2: Countries
# 
# **Check-in**: What does each *row* represent? What about each *column*?
# 
# | Country | Population (million) | GDP (Trillions) |
# | ------- | ---------- | --- | 
# | USA     | 329.5         | 20.94 |
# | UK     | 76.22        | 2.7 |
# | China     | 1402       | 14.72 |
# 

# ### Example 3: Experimental psychology
# 
# **Check-in**: What does each *row* represent? What about each *column*?
# 
# | Subject ID | Condition | Reaction Time (ms) |
# | ---------- | --------- | ------------- |
# | 1          | Congruent | 100 |
# | 2          | Incongruent | 150 |
# | 3          | Congruent | 110 |
# | 4          | Incongruent | 145 |
# 

# ### Tabular data: interim summary
# 
# - **2-dimensional data** consisting of **rows** and **columns**.  
# - Can be represented using an **Excel spreadsheet** (or [Google Sheet](https://www.google.com/sheets/about/)).  
# - One of the most common **data structures**, especially in social science.
# 
# This brings us to: how do we represent tabular data in Python?
# 

# ## Tabular data in Python *without* `pandas`
# 
# - Ultimately, we'll learn about representing tabular data with `pandas`.  
# - But before that, let's consider the *alternatives*.  
# - So far, we've learned about a couple potentially helpful data types:
#    - `list`.  
#    - `dict`.  
# - Let's consider each of these types in turn.

# ### Tabular data with `list`s
# 
# - Tabular data consists of **rows** and **columns**.
#    - Typically, each *column* corresponds to an *attribute* of an individual (e.g., a person). 
# - One option is to use a separate `list` for each column.

# #### Example: economic connectedness
# 
# - One `list` representing county names.
# - Another `list` representing population.
# - Another `list` representing economic connectedness.

# In[1]:


county = ['SF', 'New York', 'Salt Lake']
population = [870044, 1632480, 200133]
economic_connectedness = [1.31, 0.83, 0.96]


# Using this method, we can track each **observation** (i.e., each **row**) using the **index**.

# In[2]:


print(county[0])
print(population[0])
print(economic_connectedness[0])


# #### Discussion
# 
# What is a potential issue using this approach?

# #### Discussion (continued)
# 
# - Kind of awkward.  
# - Need to remember which `list` corresponds to which **attribute**.
#   - Very important to name our `list` variables carefully.
# - Also kind of annoying to have to **index** into each `list` separately.

# ### Tabular data with `dict`s
# 
# - A "level up" would be to represent this data using a `dict`.
# - Each **key** corresponds to a **column** name (i.e., attribute).
# - Each **value** corresponds to a `list` of those attribute values.

# In[3]:


ec_data = {'county': ['SF', 'New York', 'Salt Lake'],
          'population': [870044, 1632480, 200133],
          'economic_connectedness': [1.31, 0.83, 0.96]}


# In[4]:


## Now each attribute is clearly named
ec_data['county']


# In[5]:


## But we still have to be careful about our indexing
ec_data['county'][0]


# #### Discussion
# 
# What is a potential issue using this approach?

# #### Discussion
# 
# - Better, but still kind of awkward.  
# - Still hard to do several things:
#    - What if we wanted **each attribute** for a given observation (`county`, `population`, and `economic_connectedness`)?
#    - What if we wanted to `filter` the data according to some value (i.e., `population > 1000000`)?

# In[6]:


## To get attributes for given observation, must rely on indexing
sf = (ec_data['county'][0], ec_data['population'][0],
     ec_data['economic_connectedness'][0])
sf


# In[7]:


## Filtering is even harder...
## Would need many more lines of code to show!


# ### Interim summary
# 
# - We know we need to represent **tabular data**.  
#    - Need a way to represent *rows* and *columns*.
# - A `dict` is a good start: helps us track *column names*.  
# - But ideally, we'd have a better way of ensuring **each observation in each column can be accessed in tandem**.

# ## Introducing `pandas`
# 
# > [**`pandas`**](https://pandas.pydata.org/) is a package that enables **fluid** and **efficient** storage, manipulation, and analysis of data.

# In[8]:


## Import statement
import pandas as pd


# ### `pandas.DataFrame`
# 
# - The heart of `pandas` is the `DataFrame` class. 
# - This is a way of representing **tabular data**.
# - `pd.DataFrame(...)` can be used to turn a `dict` into a `DataFrame`!
# 

# In[9]:


## This was the dictionary we created
ec_data


# In[10]:


## Turning this into a dataframe
df_ec = pd.DataFrame(ec_data)
df_ec


# #### Check-in
# 
# Suppose we have several `list`s representing attributes, like `height` and `eye_color`. How would we turn these `list`s into a `DataFrame`?

# In[11]:


height = [70, 65, 72, 64, 65, 68, 71]
eye_color = ['blue', 'brown', 'brown', 'green', 'blue', 'brown', 'green'] 


# In[12]:


### Your code here


# #### Solution

# In[13]:


df_info = pd.DataFrame({
    'height': height,
    'eye_color': eye_color
})
df_info


# ## Working with a `DataFrame`
# 
# - Now that we have a `DataFrame` object, we want to be able to *use* that `DataFrame`.
# - This includes:
#    - Get basic information about `DataFrame` (e.g., its *shape*).
#    - Accessing specific *columns*.  
#    - Accessing specific *rows*.  

# ### Retrieving information about a `DataFrame`
# 
# - Given a `DataFrame`, we might want to know things like:
#    - What is the **shape** of this `DataFrame`?
#    - What are the names of each column?
#    - What are the first `2` rows of this `DataFrame`?

# #### Retrieving *shape*
# 
# The `shape` attribute tells us `(number_of_rows, number_of_columns`).

# In[14]:


df_info.shape


# #### Retrieving column names

# In[15]:


df_info.columns


# #### Using `head` and `tail`
# 
# - The `head(x)` function displays the top `x` rows of the `DataFrame`. 
# - Similarly, `tail(x)` displays the last `x` rows.

# In[16]:


df_info.head(2)


# In[17]:


df_info.tail(2)


# ### Accessing a column/attribute
# 
# - A **column** can be accessed using `dataframe_name['column_name']`.

# In[18]:


## What does this syntax remind you of?
df_info['height']


# #### Check-in
# 
# Consider the `df_ec` `DataFrame` below. How would we access the `county` column?

# In[19]:


df_ec


# #### Solution (1)

# In[20]:


df_ec['county']


# #### Solution (2)
# 
# A column can also be accessed using the `.column_name` syntax.

# In[21]:


df_ec.county


# #### Check-in
# 
# Consider the `df_ec` `DataFrame` below. How could we access *multiple columns* at once, e.g., `county` and `population`?

# In[22]:


df_ec


# #### Solution
# 
# We can use the `[['col_1', 'col_2']]` syntax.

# In[23]:


df_ec[['county', 'population']]


# ### Accessing a row/observation
# 
# - To access an individual row by its *index*, we can use the `.iloc` method.
#    - (Later, we'll discuss accessing rows by their **values** using `filter`.)

# In[24]:


## Gets first row
df_ec.iloc[0]


# In[25]:


## Gets second and third row
df_ec.iloc[1:3]


# ## Conclusion
# 
# This concludes our introduction to `pandas`. Key takeaways were:
# 
# - **Tabular data** consists of *rows* and *columns*.  
# - `pandas` is a Python package for representing tabular data.  
# - `pandas.DataFrame` is what enables this representation format.
# 
# Next time, we'll discuss more of what we can do with a `DataFrame`.
