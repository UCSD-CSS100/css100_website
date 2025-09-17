#!/usr/bin/env python
# coding: utf-8

# # Lists in Python

# ## Goals of this lecture
# 
# The primary goal of today's lecture is to give you a basic familiarity with **lists** in Python. This includes:
# 
# - A high-level understanding of what a `list` is and how it fits into the broader ecosystem of Python **collections**. 
# - How do you create a `list`?
# - Indexing into `list`s.  
# - Looping through `list`s.  
# - List comprehension.
# - Checking if an item is `in` a `list`. 

# ## What a `list`?
# 
# > A **list** is a mutable collection of ordered items, which can have various `type`s. 
# 
# Let's break this down:
# 
# - **Mutable**: a `list` object can be changed.
# - **Collection**: i.e., a `list` can contain multiple items (unlike, say, an `int`).  
# - **Ordered**: these items have a particular *order*, i.e., it's a **sequence**. (We'll later discuss objects like `dict`ionaries that don't have order.)
# - **Various `type`s**: i.e., a `list` can have objects belonging to different `type`s, such as an `int`, a `str`, and even another `list`!

# ## How do you create a `list`?
# 
# A `list` is created with square brackets, i.e., `[]`. 

# In[1]:


### This is an empty list
my_first_list = []
print(my_first_list)
print(type(my_first_list))


# You can put objects *into* the list by separating them with commas.

# In[2]:


## This list has an int and several strings.
assorted_objects = ["apple", 1, "class", "library"]
assorted_objects


# ### Check-in
# 
# Use the square brackets operator to create a `list` called `sample_list`. Put exactly three items in this list (they can be of any `type` you prefer).

# In[3]:


### Your code here


# ### Check-in
# 
# Now, double-check your work by using `len` to calculate the length of `sample_list`. Does it return the value `3`? If not, there are either too few or too many items.

# In[4]:


### Your code here


# ## Indexing into a list
# 
# > **Indexing** means returning the item at a particular position in a `list`.
# 
# You can *index* into a list using square brackets.

# In[5]:


assorted_objects[0]


# In[6]:


assorted_objects[1]


# In[7]:


assorted_objects[2]


# ### Check-in
# 
# Try indexing into `assorted_objects` with the number `4`. What happens? Why?

# In[8]:


### Your code here


# ### Counting backward
# 
# The index `[-1]` retrieves the *final item* on a list. Thus, you can use this syntax to "count backwards" from the end of a list.

# In[9]:


print(assorted_objects)


# In[10]:


### Last object
assorted_objects[-1]


# In[11]:


### Second-to-last object
assorted_objects[-2]


# ### Slicing
# 
# Just as we can **slice** into a `str` (i.e., retrieve *multiple* characters between a span of indices), we can do the same for a `list`.

# In[12]:


my_long_list = ["this", "is", "a", "set", "of", "words", "I", "made", "up"]
my_long_list[0:4]


# In[13]:


my_long_list[4:8]


# ### Interim summary: indexing
# 
# - Python indexing starts at zero.  
# - The final element of a sequence can be retrieved with `[-1]`. 
# - Multiple adjacent elements can be retrieved with `[start:stop]`. 
#    - This will include the element at `start`, but not the one at `stop`.  

# ### Check-in
# 
# Consider `my_long_list` below. How would you return the sub-list `["words", "I", "made", "up"]`?

# In[14]:


my_long_list = ["this", "is", "a", "set", "of", "words", "I", "made", "up"]
### Your code here


# ## Looping through a `list`
# 
# We've already discussed [loops](06-loops), so this will serve as a brief review/reminder.
# 
# There are two main ways of looping through a `list`:
# 
# - `for` loop.
# - `while` loop.

# ### `for` loops
# 
# A `for` loop will iterate through each item in a sequence, such as **list**.

# In[15]:


core_courses = ['CSS 1', 'CSS 2', 'CSS 100']
for course in core_courses:
    print(course)


# ### `while` loops
# 
# A `while` loop will continue running as long as some condition is met.
# 
# A common formulation is to use an **index** to loop through the elements of a `list`, which runs into the index reaches the `len` of the `list`. 

# In[16]:


i = 0
while i < len(core_courses):
    print(core_courses[i])
    i += 1 ## Make sure to increase index!


# ### `enumerate`
# 
# The `enumerate` function allows you to iterate through a list, as in a `for` loop, but it *also* tracks an index.

# In[17]:


for index, item in enumerate(core_courses):
    print(index)
    print(item)


# ## List "comprehensions"
# 
# > In Python, a [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) is a shorter, more efficient way to loop through a `list` (and possibly apply some function to each element of a list). 
# 
# Examples:
# 
# - Multiply each number in a list by 2.  
# - Make each `str` in a list lowercase.
# 
# A list comprehension will **return** another `list`, which has been modified in some way.

# In[18]:


### The simplest list comprehension simply returns every element in a list
original_list = ["This", "is", "CSS", "1"]
new_list = [i for i in original_list]
new_list


# ### Check-in (conceptual)
# 
# What do you notice about the **syntax** of a list comprehension? Does it remind you of any other technique we've discussed?

# ### Modifying elements of a `list`
# 
# You can also use a list comprehension to **modify** elements of a `list`.
# 
# In the code below, the list comprehension returns the elements of the original `1ist`, but converts them all to `upper`case.

# In[19]:


### Make everything upper-case.
original_list = ["This", "is", "CSS", "1"]
new_list = [i.upper() for i in original_list]
new_list


# ### Using conditions
# 
# You can also **conditionally modify** (or **conditionally return**) elements of a list using a `list` comprehension.

# In[20]:


### List of foods
foods = ["pasta", "pizza", "sushi", "curry", "rice"]
### Return only foods with letter "i"
foods_with_i = [food for food in foods if "i" in food]
foods_with_i


# ### Check-in
# 
# The `list` below contains both `int` and `str` objects. Use a list comprehension to multiply each `int` by 2, and ignore the `str` objects.

# In[21]:


### List of objects
assorted_list = [1, 5, "bottle", 10, "bag"]
### Your code here


# ### Check-in
# 
# The `list` below contains both `int` and `str` objects. Now, use a list comprehension to turn each `str` into an upper-case string, and ignore the `int` objects.

# In[22]:


### List of objects
assorted_list = [1, 5, "bottle", 10, "bag"]
### Your code here


# ## Checking membership
# 
# > The `in` operator can be used to check if a given item occurs **in** a particular `list`. It returns a boolean answer (i.e., `True` or `False`).
# 
# Note that this can be used with **strings** as well.

# In[23]:


"CSS 1" in core_courses


# In[24]:


"COGS 14B" in core_courses


# ### Check-in
# 
# Consider `my_long_list` below. How would you check whether the `str` `"words"` appears in that `list`?

# In[25]:


my_long_list = ["this", "is", "a", "set", "of", "words", "I", "made", "up"]
### Your code here


# ### Conclusion
# 
# This was a *brief* introduction to `list` objects. The lab this week will contain many more examples and practice problems; additionally, next week we'll talk about some more complex operations, such as combining lists, `append`ing items to a `list`, and more.
