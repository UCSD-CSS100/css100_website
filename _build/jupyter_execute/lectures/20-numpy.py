#!/usr/bin/env python
# coding: utf-8

# # Vector operations with `numpy`

# ## Goals of this lecture
# 
# Today we're going to discuss using the `numpy` package in Python. `numpy` can be used for efficient **vector operations**, which is very useful for statistics and data analysis––and more broadly, **computational social science**.
# 
# Broadly, this will involve:
# 
# - What kinds of tools are involved in **computational social science**? How is this similar and different to what we've discussed already?
# - An introduction to `numpy` specifically.  
# - Working with **vectors**.

# ## Computational social science in Python
# 
# Python hosts a number of tools (packages) to enable **scientific computing**, including computational social science:
# 
# - Packages to perform *vector operations* (e.g., `numpy`). 
# - Packages to represent *data tables* (e.g., `pandas`).
# - Packages to make *visualizations* (e.g., `matplotlib`). 
# - Packages to perform *statistical analyses* (e.g., `scipy`).  
# 
# These packages form part of an **ecosystem**.

# ### Is this different from what we've been doing?
# 
# Yes and no.
# 
# So far, we've focused on **Python fundamentals**: 
# 
# - E.g., variables, loops, functions, and more.  
# - These fundamentals are critical––think of them as the **foundation** for everything that comes next.  
# 
# But **scientific computing** will involve a heavier focus on:
#  - Thinking about *data structures*. 
#  - Thinking about *relationships between data*.  
#   

# ### Illustrative example
# 
# - Previously, we've relied on *loops* while working with `list` objects.
# - E.g., if we wanted to add every *i*th item in one `list` to every *i*th item in another `list`, we have to iterate through each loop item-by-item.  
# - However, `numpy` is a tool for **vector-wise arithmetic**: 
#   - Can add/multiply/divide/etc. entire *vectors* together, rather than having to loop through each item.
#   
# Onto `numpy`!
# 

# ## What is `numpy`?
# 
# > [**`numpy`**](https://numpy.org/doc/) is a *package* for scientific computing; specifically, it enables fast computation with *vectors* and *matrices*, along with a number of important mathematical operations.
# 
# Because `numpy` is a package, it must be *imported*.

# In[1]:


# Import statement
import numpy as np


# ### What can I use `numpy` for?
# 
# - `numpy` allows you to work with **homogenous** arrays.
#   - A [**homogenous array**](https://numpy.org/doc/stable/user/quickstart.html) is an array with objects all of the same `type`.  
#   - E.g., all `int`, or all `bool`, etc.
# - The benefit of this is that you can do **computations** very **efficiently**.
#   - No more need to *loop*!
# - Enables more advanced mathematical operations.
# 
# **Note**: `numpy` is a key part of many *advanced machine learning* packages!
# 

# ### Creating a `numpy.ndarray`
# 
# The basic data type of `numpy` is an `ndarray`.
# 
# - `ndarray` = **N-dimensional array**.  
# 
# A simple way to create an `ndarray` is `np.arange` ("a range").

# In[2]:


# Works similar to range(N)
np.arange(1, 4)


# #### `np.arange` in detail
# 
# - By default, `np.arange(start, stop)` returns an array of integers from `start` to `stop`. 
# - The `step` parameter allows you to determine the **granularity** of how you "step" between `start` and `stop`.

# In[3]:


## step size = 2
np.arange(1, 4, step = 2)


# In[4]:


## step size = .5
np.arange(1, 4, step = .5)


# #### Check-in
# 
# How would you create an array ranging from `1` to `20`, incrementing with a step size of `.5`? How long would this array be?

# In[5]:


### Your code here


# #### Solution

# In[6]:


np_range = np.arange(1, 20, step = .5)
len(np_range)


# ### Turning a `list` into a `ndarray`
# 
# Another way to create an `ndarray` is to pass a `list` into the `np.array(...)` function.

# In[7]:


og_list = [1, 2, 3]
type(og_list)


# In[8]:


np_array = np.array(og_list)
print(type(np_array))


# In[9]:


np_array


# #### Check-in
# 
# How would you create a `numpy` array with the elements `[5, 6, 7]`?

# In[10]:


### Your code here


# #### Solution

# In[11]:


np_array = np.array([5, 6, 7])
np_array


# #### Check-in
# 
# Why is this code throwing an error?

# In[12]:


test_array = np.array(1, 2, 3)


# #### Solution
# 
# Make sure you **wrap** the input array in `[]`.

# In[78]:


test_array = np.array([1, 2, 3])
test_array


# ### Indexing into a one-dimensional array
# 
# Indexing works just like it does for `list`s.

# In[79]:


np_array[0]


# In[80]:


np_array[1]


# In[81]:


np_array[2]


# ### Multi-dimensional arrays
# 
# - So far, we've just been looking at 1-dimensional arrays.
# - But `numpy` is excellent at storing **multi-dimensional arrays**.
# 

# ### Checking *attributes* of an array
# 
# The `shape` attribute tells you the dimensions of an array.

# #### Check-in
# 
# What is the **dimensionality** of `md_array`?

# In[85]:


### What is dimensionality
md_array


# #### Solution
# 
# You can check this using `md_array.shape`.

# In[86]:


md_array.shape


# #### Check-in
# 
# What about `md_array2`?

# In[87]:


## 2x3 array
md_array2 = np.array([[1, 2, 3], [4, 5, 6]])
md_array2.shape


# #### Solution
# 
# You can check this using `md_array.shape`.

# In[88]:


md_array2.shape


# ### Checking *attributes* of an array (pt. 2)
# 
# The `dtype` attribute tells you the *type* of data in the array.

# In[89]:


md_array2.dtype


# ### Homogenous data
# 
# As noted earlier, an array is meant to store **homogenous elements**.
# 
# - This means that `np.array` will try to **convert** any heterogenous elements to a common `type`.

# In[90]:


## Note what happens to 5 and 7!
arr3 = np.array(["a", 5, 7])
arr3


# In[91]:


arr3.dtype


# ### Interim summary
# 
# - `numpy` is a package that forms the foundation of scientific computing.  
# - `numpy` arrays are the cornerstone of `numpy`.
# - A `numpy` array is like a `list`, with a couple differences:
#   - Requires **homogenous elements**.  
#   - Better at representing **multi-dimensional arrays**.
#   - Can be used for **vector operations** (coming up!). 
# 

# ## Working with vectors (intro)
# 
# - `numpy` vectors make it easier to do all sorts of operations, such as **arithmetic** operations.
# - No more need to use `for` loops––can do vector arithmetic the same way we multiply individual numbers.

# ### The old way: arithmetic with `for` loops and `list`s
# 
# Adding one `list` to another requires using a `for` loop. 

# In[108]:


list1 = [1, 2, 3]
list2 = [2, 3, 4]


# In[111]:


## The "+" operator just combines them
list1 + list2


# In[113]:


## To add them, we must use a for loop
sum_list = []
for index, item in enumerate(list1):
    sum_list.append(item + list2[index])
sum_list


# ### The new way: arithmetic with `numpy`
# 
# `numpy` makes it *much* easier to do arithmetic operations with vectors.

# In[114]:


## First, define some vectors
arr1 = np.array([list1])
arr2 = np.array([list2])


# In[115]:


## Can just use "+"!
arr1 + arr2


# #### Other arithmetic operations

# In[117]:


arr1 -  arr2


# In[118]:


arr1 *  arr2


# In[116]:


arr1 / arr2


# #### Vectors vs. scalars
# 
# - A **vector** is a list of numbers; a **scalar** is a single number.
# - We can multiply (or add, subtract, etc.) an entire *vector* by a single number.

# In[123]:


arr1


# In[125]:


## Multiply all elements by 100
arr1 * 100


# #### Check-in
# 
# What would multiplying the two arrays below return?
# 
# ```python
# a = np.array([2, 4, 5])
# b = np.array([2, 2, 3])
# a * b
# ```

# In[126]:


### Your code here


# #### Solution

# In[128]:


a = np.array([2, 4, 5])
b = np.array([2, 2, 3])
a * b


# #### Check-in
# 
# What would happen if we ran the code below?
# 
# ```python
# a = np.array([2, 4, 5])
# b = np.array([2, 2])
# a * b
# ```

# In[126]:


### Your code here


# #### Solution
# 
# Vectors/matrices must have *compatible shapes*.

# In[130]:


a = np.array([2, 4, 5])
b = np.array([2, 2])
a * b


# ### Thinking with vectors
# 
# - Using `numpy` for vector arithmetic can sometimes involve a "cognitive shift".  
# - We're used to multiplying *individual elements*; now we have to transition to thinking about multiplying *entire vectors*.
# - But it's much more efficient!

# ## Conclusion
# 
# This was a brief introduction to `numpy`.
# 
# - `numpy` is a powerful package used in scientific computing.  
# - The cornerstone of `numpy` is `numpy.ndarray`.  
# - `numpy` arrays can be used for efficient **vector computations**.
# 
# Next time, we'll dive deeper into more advanced `numpy` operations.
