#!/usr/bin/env python
# coding: utf-8

# # 05-Review (Working with Data)

# ## Goals of this lecture
# 
# This lecture will review tools useful for **working with data** in Python. 
# 
# - Focus: **tabular data** in `.csv` files.
# - Intro to `pandas`.  
# - Basic manipulation and analysis using `pandas`.

# ## What is a file?
# 
# > A **file** is a set of *bytes* used to store some kind of data.
# 
# The **format** of this data depends on what you're using it for, but at some level, it is translated into *binary bits* (`1`s and `0`s). 
# 
# The file format is usually specified in the **file extension**.  
# 
# - `.csv`: comma separated values.  
# - `.txt`: a plain text file.  
# - `.py`: an executable Python file.  
# - `.png`: a portable network graphic file (i.e., an image).

# ## What is tabular data?
# 
# > [Tabular data](https://www.statology.org/tabular-data/) is data organized in a **table** with *rows* and *columns*.
# 
# - This kind of data is **two-dimensional**.  
# - Typically, each **row** represents an "observation".
# - Typicallly, each **column** represents an *attribute*.  
# 
# Often stored in `.csv` files.
# 
# - `.csv` = "comma-separated values"
# 

# ### Example: Countries
# 
# **Check-in**: What does each *row* represent? What about each *column*?
# 
# | Country | Population (million) | GDP (Trillions) |
# | ------- | ---------- | --- | 
# | USA     | 329.5         | 20.94 |
# | UK     | 76.22        | 2.7 |
# | China     | 1402       | 14.72 |
# 

# ## Introducing `pandas`
# 
# > [**`pandas`**](https://pandas.pydata.org/) is a package that enables **fluid** and **efficient** storage, manipulation, and analysis of data.

# In[1]:


## Import statement: pandas is a "package"
import pandas as pd


# ### `pandas.read_csv`
# 
# Tabular data is often stored in `.csv` files. 
# 
# - `pandas.read_csv` can be used to **read in** a `.csv` file.  
# - This is represented as a `pandas.DataFrame`.
# 
# ```python
# pd.read_csv("path/to/file.csv") ### replace with actual filepath!
# ```

# In[2]:


### .csv file with data about different Pokemon
df_pokemon = pd.read_csv("data/pokemon.csv")


# ### `read_csv` with a URL
# 
# You can also pass a URL that points to a `.csv` file into `read_csv`. 
# 
# - This is a dataset from [*Brand et al. (2019)*](https://www.cambridge.org/core/journals/evolutionary-human-sciences/article/cultural-evolution-of-emotional-expression-in-50-years-of-song-lyrics/E6E64C02BDB0480DB13B8B6BB7DFF598), which quantified changes in the positivity and negativity in song lyrics over time.
# - We'll be working more with that dataset soon!

# In[3]:


df_lyrics = pd.read_csv("https://raw.githubusercontent.com/lottybrand/song_lyrics/master/data/billboard_analysis.csv")


# In[4]:


df_lyrics.head(2)


# ### Using a `DataFrame`
# 
# - Now that we have a `DataFrame` object, we want to be able to *use* that `DataFrame`.
# - This includes:
#    - Get basic information about `DataFrame` (e.g., its *shape*).
#    - Accessing specific *columns*.  
#    - Accessing specific *rows*.  

# #### Using `shape`
# 
# `df.shape` tells us how many **rows** and **columns** are in the `DataFrame`.

# In[5]:


## (#rows, #columns)
df_pokemon.shape


# #### Using `head` and `tail`
# 
# - The `head(x)` function displays the top `x` rows of the `DataFrame`. 
# - Similarly, `tail(x)` displays the last `x` rows.

# In[6]:


df_pokemon.head(2)


# In[7]:


df_pokemon.tail(2)


# #### Accessing columns
# 
# - A **column** can be accessed using `dataframe_name['column_name']`.

# In[8]:


### What does this bracket syntax (["column_name"]) remind you of?
df_pokemon['Speed'].head(5)


# ## Useful *operations* with `pandas`
# 
# `DataFrame`s enable all sorts of useful **operations**, including:
# 
# - `sort`ing a `DataFrame` by a particular column.
# - Calculating **descriptive statistics** (e.g., `mean`, `median`, etc.).
# - **Filtering** a `DataFrame`.  
# - Aggregating across levels of a variable using `groupby`. 
# 
# Note that we'll also cover these topics more in-depth in Week 4!

# ### `sort_values`

# In[9]:


### By default, will sort from lowest to highest
df_pokemon.sort_values("HP").head(2)


# In[10]:


### Show the highest HP
df_pokemon.sort_values("HP", ascending = False).head(2)


# #### Check-in
# 
# What is the `Speed` of the Pokemon with the highest `Attack`?

# In[11]:


### Your code here


# #### Solution

# In[12]:


### Pokemon with highest Attack
df_pokemon.sort_values("Attack", ascending = False).head(1)


# ### Descriptive statistics
# 
# Columns of a `DataFrame` can also be **summarized**:
# 
# - `mean`: average value (for numeric variables) 
# - `median`: "middle" value (for numeric variables)
# - `mode`: most frequent value

# In[13]:


df_pokemon['Attack'].mean()


# In[14]:


df_pokemon['Attack'].median()


# In[15]:


df_pokemon['Attack'].mode()


# ### Filtering a `DataFrame`
# 
# - Often, we want to **filter** a `DataFrame` so we only see observations that meet certain **conditions**.
# - Ultimately, this is similar to using a **conditional statement**––just with different syntax.

# #### Example 1: filtering on a categorical variable
# 
# - The `legendary` column is a *categorical* variable, meaning there are several discrete categories.  

# In[16]:


## How many legendary pokemon?
df_pokemon[df_pokemon['Legendary']==True].head(5)


# #### Example 2: filtering on a continuous variable
# 
# - The `HP` column is a *continuous* variable.
# - Let's show only the rows for Pokemon with a `HP > 150`.

# In[17]:


df_pokemon[df_pokemon['HP'] > 150].head(3)


# ### Using `groupby`
# 
# > The [`groupby` function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) allows you to **split data** (i.e., along different categories) then **apply** some function to each split of that data (e.g., `mean`).
# 
# The syntax is as follows:
# 
# ```python
# df_name.groupby("column_to_group_by").mean() ## or median, etc.
# ```

# #### Example: mean `Attack` by `Legendary`
# 
# Here, the `[[...]]` syntax just limits the columns in the `DataFrame` to the columns we directly care about.

# In[18]:


df_pokemon[['Legendary', 'Attack']].groupby("Legendary").mean()


# #### Check-in:
# 
# How would you calculate the `median` `Defense` by `Legendary` status?

# In[19]:


### Your code here


# #### Solution 

# In[20]:


df_pokemon[['Legendary', 'Defense']].groupby("Legendary").median()


# #### Check-in:
# 
# How would you calculate the `mean` `HP` by `Type 1`?

# In[21]:


### Your code here


# #### Solution

# In[22]:


df_pokemon[['Type 1', 'HP']].groupby("Type 1").mean()


# ## Conclusion
# 
# This concludes our unit on interacting with **data**.
# 
# - Reading in `.csv` files with `pandas`.
# - Summarizing and working with **tabular data**.
# 
# We'll also spend *much* more time on tabular data in Week 4, particularly as it regards "**cleaning**" data.
