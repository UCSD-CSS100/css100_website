#!/usr/bin/env python
# coding: utf-8

# # Lists in Python (advanced)

# ## Review: `list`s
# 
# > A **list** is a collection of ordered items, which can have various `type`s. 
# 
# Basics:
# 
# - A `list` is created using square brackets, i.e., `[]`.  
# - You can **index** into a list using the syntax: `list_name[0]`. 
# - Like with a `str`, you can **loop** through a `list` using `for` and `while` loops.  
# - List **comprehensions** are an efficient way to apply some operation throughout a `list`.

# ## Goals of today's lecture
# 
# Today, we'll cover several more **advanced** operations we can perform with a `list`, including:
# 
# - Combining lists using the `+` operator.  
# - Adding items to a `list` using `append`.
# - Removing items from a list using `remove` and `pop`.  
# - Locating the **index** of a particular value or item in a `list` using `index`.  
# - `sort`ing the elements in a list.  
# 
# We'll also cover some related topics in the domain of `lists`:
# 
# - Nested lists. 
# - Tuples vs. lists.
# 
# Note that some of these operations will mirror similar operations we discussed with strings. That makes sense, because both are **sequences**!

# ## Combining lists
# 
# Two or more lists can be combined using the `+` operator.

# In[1]:


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 + list2


# These lists do *not* have to have the same `type` or number of objects.

# In[2]:


list3 = ["a", "b"]
list1 + list3


# ### Check-in
# 
# Use the `+` operator to combine the lists below, then use `join` to join the words into a complete sentence (with each word separated by a `" "`).

# In[3]:


l1 = ['CSS', '1']
l2 = ['is', 'fun']
### Your code here


# ## Adding items to a `list`
# 
# In addition to using the `+` operator, you can add individual *items* to a list using the `append` function.
# 
# - Note that this modifies the list "in place", i.e., it doesn't *return* a value, but rather it mutates the existing `list` object.

# In[4]:


fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)


# ### Filling up an empty `list`
# 
# The `append` function is often used to **fill up** a `list` with items, such as during a `for` loop.
# 
# For example, you might:
# 
# - Initialize an *empty* list.  
# - Loop through numbers between `1` and `100`.
# - Add those numbers to the empty list if they're odd.

# In[5]:


new_list = [] ### Initialize empty list
for num in range(1, 101): ### Loop through range
    if num % 2 == 1: ### If number is odd...
        new_list.append(num) ### Append it to list
new_list[0:3] ### Get the first three elements of new list


# ### Check-in
# 
# Add the number `4` to the list below using `append`.

# In[6]:


sample_list = [1, 2, 3]
### Your code here


# ### Check-in
# 
# The code cell below contains two lists: one contains a list of foods, the other contains a list of words with the letter "a". 
# 
# Using `append` and a `for` loop, add the items from `foods` to `a_words` if:
# 
# - they contain the letter "a".
# - they don't already appear in `a_words`. 

# In[7]:


foods = ['apple', 'banana', 'orange', 'kiwi', 'strawberry', 'mango', 'pineapple', 'berry']
a_words = ['board', 'table', 'apple', 'human']
### Your code here


# ### Using `insert`
# 
# - The `append` function always adds items to the **end** of a list.  
# - Instead, you can use `insert` to insert items at a specific location, such as the start.
# - Syntax: `list_name.insert(position, item)`

# In[8]:


sample_list = [2, 3, 4]
sample_list.insert(0, 1) ### insert a 1 at the zero-th position
print(sample_list)


# ## Removing items from a `list`
# 
# There are two primary ways to **remove** an item from a list.
# 
# - `pop`: this removes the item at a given index (by default, this is the *last* item), and also **returns** that item. 
# - `remove`: this removes the first occurrence of a particular *value* from a `list`.
# 
# So, roughly:
# 
# - `pop` removes by *position*.  
# - `remove` removes by *value*.  

# ### `pop`ping in action
# 
# The syntax for `pop` is straightforward: `list_name.pop()`

# In[9]:


sample_list = [1, 2, 5, 7]
sample_list.pop() ### by default, returns final element


# Now, if we look back at `sample_list`, we see that the final element has indeed been removed.

# In[10]:


sample_list


# ### Check-in
# 
# What do you think would happen if we `pop` from an empty list?

# In[11]:


empty_list = []
### what would happen if we call empty_list.pop()


# ### `remov`ing in action
# 
# The syntax for `remove` is also straightforward: `list_name.remove(value)`
# 
# - Where `value` is the value that you want to remove.  
# - Note that unlike `pop`, `remove` does *not* return a particular value, but it does modify the list in place.

# In[12]:


sample_list = [1, 2, 5, 7]
sample_list.remove(5)
print(sample_list)


# ### Check-in
# 
# What would happen to `test_list` if we call `test_list.remove("apple")`?
# 
# 1. `['bread', 'apple', 'cheese', 'apple']`
# 2. `['bread', 'cheese', 'apple']`
# 3. `['bread', 'cheese']`

# In[13]:


test_list = ['bread', 'apple', 'cheese', 'apple']
### Your code/response here


# ## Finding the index of a particular value
# 
# The `index` function allows you to return the index corresponding to the *first occurrence* of a particular value.
# 
# **Basic syntax**: `list_name.index(value)`
# 
# - Note that you can also (optionally) parameterize the `start` and `end` of this search: 
#    - `list_name.index(value, start, end)`

# In[14]:


test_list = ['bread', 'apple', 'cheese', 'apple']
test_list.index("bread")


# In[15]:


### Returns *first* occurrence of "apple"
test_list.index("apple")


# In[16]:


### Returns first occurrence of "apple", *after* index = 2
test_list.index("apple", 2)


# ### Check-in
# 
# Use the `index` function to retrieve the index of the first occurrence of the number `10` in the list below.

# In[17]:


number_list = [1, 10, 15, 20, 10, 55]
### Your code here


# ### Check-in
# 
# Use the `index` function to retrieve the index of the first occurrence of the number `10` between the indices `2` and `5` in the list below.

# In[18]:


number_list = [1, 10, 15, 20, 10, 55]
### Your code here


# ## `sort`ing a list
# 
# > **Sorting** a `list` means rearranging its elements according to some measure of "least" and "greatest".
# 
# There are many different [**algorithms** for sorting a list](https://en.wikipedia.org/wiki/Sorting_algorithm), which we won't cover in detail here.
# 
# However, in Python, there are two main *functions*:
# 
# - `sorted(list)`: returns a sorted version of a `list`.  
# - `list.sort()`: sorts a particular `list` **in place**. 

# In[19]:


number_list = [2, 1, 9, 5, 3, 4]
sorted_list = sorted(number_list)
sorted_list


# In[20]:


number_list = [2, 1, 9, 5, 3, 4]
number_list.sort()
number_list


# ### Ascending vs. descending?
# 
# - By default, `sorted` will sort a list in **ascending** order.
# - The `reverse` key allows you to instead sort that list in **descending** order (i.e., largest elements first).
# 
# 

# In[21]:


number_list = [2, 1, 9, 5, 3, 4]
sorted_list = sorted(number_list, reverse = True)
sorted_list


# ### Check-in
# 
# The list `names` below is unsorted. Use the `sorted` function to return a new list with the names sorted, in **descending** order.

# In[22]:


names = ['Sean', 'Nikolay', 'Pulkit', 'Simran', 'Purva']


# ## Nested lists
# 
# A `list` can contain many different `type`s of objects: `str`, `int`, and even other `list`s!
# 
# - Each **nested list** can contain further nested lists, or other types of objects.  
# - Nested lists do not have to be the same length.

# In[23]:


nested_list = [[1, 2, 3],
              ['css', 'cogs', 'econ'],
              ['tea', 'coffee']]


# ### Check-in
# 
# What would `len(nested_list)` return?

# In[24]:


nested_list = [[1, 2, 3],
              ['css', 'cogs', 'econ'],
              ['tea', 'coffee']]
### len(nested_list)


# ### Check-in
# 
# Write a `for` loop that iterates through each item in `nested_list`, and prints its length.

# In[25]:


nested_list = [[1, 2, 3],
              ['css', 'cogs', 'econ'],
              ['tea', 'coffee']]
### Your code here


# ### Check-in
# 
# Write a `for` loop that iterates through each item in `nested_list`, and prints its length.

# ## Lists vs. tuples
# 
# So far, we've focused on **lists**.
# 
# A **tuple** is another type of ordered sequence. They share several similarities with lists:
# 
# - You can index into both a **tuple** and a **list**.  
# - You can loop through both a **tuple** and a **list**. 
# 
# However, there are also a couple key differences:
# 
# - Tuples are declared using `()`, not `[]`.  
# - Unlike `list`s, a `tuple` is not mutable (i.e., it can't be changed in place).

# In[26]:


example_tuple = (1, 2, 3)
example_tuple


# ### Tuples (continued)
# 
# - We won't focus *too much* on tuples for now.  
# - However, I wanted to highlight some of those similarities and differences. 
# - It's likely that at some point in your journey with Python, you'll end up using or encountering tuples.

# In[27]:


for i in example_tuple:
    print(i)


# ## Conclusion
# 
# In Python, `list`s are very powerful objects. Regardless of what you use Python for, it's important to understand the basics of how `list`s work, as well as some of the common operations we apply to `list`s.
