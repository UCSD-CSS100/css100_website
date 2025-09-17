#!/usr/bin/env python
# coding: utf-8

# # Advanced operations with `numpy`

# ## Goals of this lecture
# 
# This lecture will continue our discussion of the `numpy` package. We'll discuss:
# 
# - More practice with **vector operations**.  
# - **Descriptive statistics** with vectors.
# - Working with **matrices** (multi-dimensional arrays).
# - Other useful functions.

# In[1]:


import numpy as np


# ## Practice with vectors
# 
# - `numpy` vectors make it easier to do all sorts of operations, such as **arithmetic** operations.
# - No more need to use `for` loops––can do vector arithmetic the same way we multiply individual numbers. 
#    - `numpy` calculations are also much faster and more efficient!

# ### Practice problems

# #### Check-in
# 
# Consider the two arrays below. How would you calculate the *difference* between each item in `a` and each item in `b`?

# In[2]:


a = np.array([2, 8, 9, 10])
b = np.array([3, 7, 6, 10])
## Your code here


# #### Solution

# In[3]:


a - b


# #### Check-in
# 
# Consider the same two arrays as before. How would you:
# 
# - Calculate the **product** of these arrays?  
# - Calculate the **sum** of the elements in this new "product" array?
# 
# Note that this is also called the [dot product](https://en.wikipedia.org/wiki/Dot_product).

# In[4]:


### Your code here


# #### Solution
# 
# This is also called the [dot product](https://en.wikipedia.org/wiki/Dot_product).

# In[5]:


## First, calculate the product
product = a * b
product


# In[6]:


## Then, calculate the sum of this array
product.sum()


# ## Descriptive statistics with `numpy`
# 
# > **Descriptive statistics** are ways to summarize and organize data.
# 
# A big advantage of `numpy` is that it has **built-in functions** to calculate various descriptive statistics:
# 
# - The `sum` of a set of numbers.  
# - The `mean` (or "average") of a set of numbers.  
# - The `median` (or "middle value") of a set of numbers.
# 

# ### `sum`
# 
# > The **sum** of a set of numbers is simply the result of adding each number together.
# 
# The `numpy` package has a `sum` function built in, which makes it easier to calculate the sum of a vector.

# In[7]:


## First, create an array with some numbers
v = np.array([5, 9, 10])
v


# In[8]:


## Now calculate the sum
v.sum()


# ### `mean`
# 
# > The **mean** of a set of scores is the *sum* of those scores divided by the number of the observations.
# 
# The `numpy` package also has a `mean` function built in. Two options:
# 
# - `array_name.mean()`
# - `np.mean(array_name)`

# In[9]:


## First, create an array with some numbers
v = np.array([5, 9, 10])
v


# In[10]:


## Now calculate the mean
v.mean()


# In[11]:


## Or do it with numpy.mean
np.mean(v)


# #### Check-in
# 
# What would happen if we ran the following code?
# 
# ```python
# v = np.array([1, 5, 9])
# np.mean(v)
# ```

# In[12]:


### Your code here


# #### Solution
# 
# This will also calculate the `mean`. 

# In[13]:


v = np.array([1, 5, 9])
np.mean(v)


# #### Check-in
# 
# What would happen if we ran the following code?
# 
# ```python
# v = np.array(["a", "b", "a"])
# v.mean()
# ```

# In[14]:


### Your code here


# #### Solution
# 
# It will throw an **error**. 
# 
# - You cannot calculate the `mean` of a vector of `str` types.
# - The `mean` can only be calculated for **interval/ratio data**.  

# ### `median`
# 
# > The **median** of a set of scores is the *middle* score when those scores are arranged from least to greatest.
# 
# The `numpy` package also has a `mean` function built in.
# 
# - Syntax: `np.median(array_name)`. 
# - Unlike `mean`, **cannot use** `array_name.median()`

# In[15]:


## First, create an array with some numbers
v = np.array([5, 9, 10, 1, 20])
v


# In[16]:


## Now calculate the median
np.median(v)


# #### Check-in
# 
# What would be the **median** of the following vector?
# 
# ```python
# v = np.array([1, 2, 5, 8])
# ```

# In[17]:


### Your code here


# #### Solution
# 
# If the vector has an *even* number of elements, the **median** is the *mean* of the middle two elements.

# In[18]:


## First, create an array with some numbers
v = np.array([1, 2, 5, 8])
v


# In[19]:


## Use np.median
np.median(v)


# In[20]:


## Equivalent to *mean* of 2 and 5
(2 + 5) / 2


# ### Interim summary
# 
# - **Descriptive statistics** are a really useful way to *summarize* data.  
# - Very valuable for both basic and applied research (e.g., in industry).  
#    - Examples: `median` salary, `mean` sales per fiscal quarter, `mean` reaction time on a psychophysics task, etc.
# - `numpy` makes this much easier.
#    - Later, we'll discuss how `pandas` (a way to represent data tables) uses these same functions.

# ## Working with matrices
# 
# > A **matrix** is a rectangular array of data (i.e., a **multi-dimensional array**).
# 
# `numpy` is *designed* for **representing** and **performing calculations** with matrices.
# 
# - A "vector" is just a one-dimensional matrix.
# - Many of the same operations we've discussed also apply to working with matrices.

# ### Creating a matrix
# 
# - Matrices can be created just like vectors.  
# - The key difference is that they contain **nested lists**.

# In[21]:


md_array = np.array([[1, 2, 5], [3, 4, 7]])
md_array


# In[22]:


## This is a 2 by 3 matrix
md_array.shape


# ### Indexing into a matrix
# 
# - You can **index** into a matrix, just like with a vector.  
# - A key difference is that you use *multiple indices*, for each dimension.
#    - `matrix_name[D1_index, D2_index, ...]`

# In[23]:


# This just returns the first *row*
md_array[0]


# In[24]:


# This returns the second element of the first row
md_array[0, 1]


# #### Check-in
# 
# How would you return the *first element* of the *second row* of `md_array`?
# 
# ```python
# md_array = np.array([[1, 2, 5], [3, 4, 7]])
# md_array
# ```

# In[25]:


### Your code here


# #### Solution

# In[26]:


# Can use [1] to get second row
md_array[1]


# In[27]:


# Use [1, 0] to get first element of second row
md_array[1, 0]


# #### Check-in
# 
# A more challenging problem: how would you return the second **column** of `md_array`? How many observations should it have?
# 
# ```python
# md_array = np.array([[1, 2, 5], [3, 4, 7]])
# md_array
# ```

# In[28]:


### Your code here


# #### Solution
# 
# Retrieving a **column** uses the `[:,column_index]` syntax.

# In[29]:


## column 1
md_array[:, 0]


# In[30]:


## column 2
md_array[:, 1]


# In[31]:


## column 3
md_array[:, 2]


# #### Check-in
# 
# How would you retrieve the *second* and *third* element of the second row?
# 
# ```python
# md_array = np.array([[1, 2, 5], [3, 4, 7]])
# md_array
# ```

# In[32]:


### Your code here


# #### Solution

# In[33]:


## First, get second row with md_array[1]
md_array[1]


# In[34]:


## First, get second/third elements with slicing
## I.e., [1:3] syntax
md_array[1, 1:3]


# ### Summary statistics with matrices
# 
# - When you call `np.sum` (or `mean`, etc.), you can specify which **axis** to calculate that statistic from.  
# - `axis = 0`: calculate `sum` (or `mean`, etc.) of each **column**.
# - `axis = 1`: calculate `sum` (or `mean`, etc.) of each **row**.

# In[35]:


## Calcaulate mean of each column
md_array.sum(axis = 0)


# In[36]:


## Calcaulate mean of each row
md_array.sum(axis = 1)


# #### Check-in
# 
# How would you calculate the `mean` of each **row** of the following matrix?

# In[37]:


m = np.array([[5, 10, 2],
            [20, 5, 100]])
### your code here


# #### Solution

# In[38]:


m.mean(axis = 1)


# In[39]:


m.mean(axis = 1).shape


# #### Check-in
# 
# Suppose you have a 5x6 matrix (5 rows, 6 columns). If you calculated the `mean` of each **column**, what would the `shape` be of the resulting vector?

# #### Solution
# 
# The vector would have a `shape` of `(6,)`, i.e., **six observations**.
# 
# - There are six columns, so calculating the mean of each column would result in *six observations*.

# ### Side note: arithmetic with matrices
# 
# - You can also perform arithmetic with matrices (e.g., **addition**, **multiplication**, etc.).
# - However, note that matrices must have compatible dimensions.  
#    - More discussion of this in a [Linear Algebra class](https://en.wikipedia.org/wiki/Linear_algebra).

# ## Identifying the location of an item
# 
# Often, you'll need to **search** a vector or matrix for items that meet a certain conditions.
# 
# - All `scores == 100`.
# - All `building_heights` above a certain threshold.  
# - All `reaction_times` above a certain cutoff.
# 
# You can think of this as **applying a conditional statement** to *search* a vector.

# ### Identifying the location of an item
# 
# Often, you'll need to **search** a vector or matrix for items that meet a certain conditions.
# 
# - All `scores == 100`.
# - All `building_heights` above a certain threshold.  
# - All `reaction_times` above a certain cutoff.
# 
# You can think of this as **applying a conditional statement** to *search* a vector.

# ### Using `==`
# 
# This will return a vector of `True` or `False`, indicating whether each index/element matches the condition.

# In[40]:


## Scores
scores = np.array([100, 95, 100, 85])


# In[41]:


## Which scores == 100?
scores == 100


# In[42]:


## Select only scores == 100
scores[scores == 100]


# ### Using `np.where`
# 
# By default, this will return the **indices** in the initial array corresponding to the condition.

# In[43]:


## Get indices
np.where(scores == 100)


# In[44]:


## Applying indices to vector
scores[np.where(scores == 100)]


# ### Check-in
# 
# Consider the following array of `building_heights`. How would you find out which buildings are taller than 50 feet?

# In[45]:


building_heights = np.array([25, 45, 10, 60, 10, 85, 100])
### Your code here


# ### Solution using `==`

# In[46]:


building_heights > 50


# In[47]:


building_heights[building_heights > 50]


# ### Solution using `np.where`

# In[48]:


## Get indices
np.where(building_heights > 50)


# In[49]:


## Apply indices
building_heights[np.where(building_heights > 50)]


# ## Other useful functions
# 
# `numpy` also has a host of other useful functions. For now, we'll focus on:
# 
# - **Generating an array** with either random numbers or `ones` or `zeros`.
# - **Reshaping an array** with `reshape.

# ### Initializing a random array
# 
# `numpy.random.rand(d1, ...)` can be used to initialize an array with **random numbers** and dimensionality `(d1, ...)`.

# In[50]:


## Generates a 1-D vector with 10 elements
np.random.rand(10)


# In[51]:


## Generates a 2-D vector with shape (2, 2)
np.random.rand(2, 2)


# #### Check-in
# 
# Generate a random array with shape (3, 2), then calculate the `mean` of each column.

# In[52]:


### Your code here


# #### Solution

# In[53]:


r = np.random.rand(3, 2)
r


# In[54]:


r.mean(axis = 0)


# ### Initializing an array of `ones` or `zeros`
# 
# This is like `np.random.rand`, but each element is either a `1` or `0`.

# In[55]:


np.ones((2, 2))


# In[56]:


np.zeros((2, 2))


# ### Using `numpy.reshape`
# 
# Sometimes, a matrix or vector isn't the right **shape** to perform a computation.
# 
# - E.g., multiplying by another vector.  
# - E.g., using for regression in a regression equation.
# 
# We can use `np.reshape` to reshape that array.

# #### Example: turning a vector into a matrix

# In[57]:


# Create a (10, ) vector
og_array = np.ones(10)
og_array


# In[58]:


# Reshape to (2, 5)
og_array.reshape((2, 5))


# In[59]:


# Reshape to (5, 2)
og_array.reshape((5, 2))


# #### Dimensions must be compatible
# 
# If you try to `reshape` into a `shape` that's not compatible with the original `size` (i.e., not **divisible** by `size`), you'll get an error.

# In[60]:


# Reshape to (5, 2)
og_array.reshape((4, 4))


# ## Conclusion
# 
# This concludes our brief foray into `numpy`.  
# 
# Now, you'll be more familiar with:
# 
# - Using `numpy` for vector arithmetic.  
# - Basic summary statistics with `numpy`.  
# - Working with **multi-dimensional arrays**.
# 
# Eventually, this will form the foundation for more advanced work in **statistics**, **machine learning**, and more.
