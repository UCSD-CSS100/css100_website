#!/usr/bin/env python
# coding: utf-8

# # Dictionaries (Advanced)

# ## Review: dictionaries
# 
# > In Python, a **dictionary**, or `dict`, is a mutable collection of items, which stores **key/value** pairings.

# In[1]:


example_dict = {'Name': 'Sean Trott',
               'Occupation': 'Assistant Teaching Professor'}
print(example_dict['Name'])
print(example_dict['Occupation'])


# ## Goals of this lecture
# 
# Last time, we covered:
# 
# - How to create a dictionary.  
# - Basic operations, e.g., indexing and looping through a dictionary.
# 
# Today, we'll cover more **use cases**:
# 
# - Using **dictionary comprehensions**.
# - **Nested dictionaries**.
# - More practice problems with dictionaries.

# ## Using a dictionary comprehension
# 
# Recall that a **list comprehension** is:
# 
# > ... a shorter, more efficient way to loop through a `list` (and possibly apply some function to each element of a list). 
# 
# Similarly, a **dictionary comprehension** can be used to:
# 
# > ... quickly create a `dict` from a set of potential keys and values.

# In[2]:


## Creates dictionary mapping each key onto key * 2
example_dc = {i: i*2 for i in range(1, 10)}
print(example_dc)


# ### Why is a dictionary comprehension useful?
# 
# In theory, we could also use a normal `for` loop to accomplish the same goal.

# In[3]:


example_for = {}
for i in range(1, 10):
    example_for[i] = i*2
print(example_for)


# But a `dict` comprehension can be written on a single line, and *can* be clearer than a `for` loop.

# In[4]:


example_dc = {i: i*2 for i in range(1, 10)}
print(example_dc)


# ### Use case: bundling `tuple`s together
# 
# A dictionary comprehension is a useful way of **bundling together** a list of `tuple` pairs.
# 
# Code explanation:
# 
# - For each element of each `tuple` pair...
# - Store the first element as the `key`, and the second element as the `value`. 

# In[5]:


course_tuples = [('Trott', 'CSS 1'), ('Ellis', 'COGS 18')]
course_dict = {key: value for key, value in course_tuples}
print(course_dict)


# ### Check-in
# 
# Use a **dictionary comprehension** to convert this `list` of `tuple` pairs into a `dict`.

# In[6]:


fruit_tuples = [('banana', 5), ('apple', 2), ('orange', 3)]
### Your code here


# ### Check-in
# 
# The code below has two lists of equal length. Use a dictionary comprehension to combine them into a dictionary, where each element in `fruits` should be the **key**, mapping onto each element at the same position in `amounts`.
# 
# **Note**: This problem is a little harder! As a hint, think about how you could **iterate** through each item in each list using an index.

# In[7]:


fruits = ['banana', 'apple', 'orange']
amounts = [5, 2, 3]
### Your code here


# ### Possible solution

# In[8]:


fruits = ['banana', 'apple', 'orange']
amounts = [5, 2, 3]
fruits_dict = {fruits[i]: amounts[i] for i in range(len(fruits))}
fruits_dict


# ## Nested dictionaries
# 
# > A **nested dictionary** is a dictionary contained inside another dictionary, i.e., as a **value**.  
# 
# In principle, there is no limit on how many nested dictionaries can be contained in a `dict` (besides memory capacity on one's computer).
# 
# - A nested dictionary is useful when you want to store **complex information** in each entry.  
# - So far, we've dealt mostly with very simple key/value entries.  
# - But what if we wanted to represent more complicated information?
# 
# Example, for each instructor in CSS (or COGS, etc.), store:
# 
# - `username`.
# - `Name`.  
# - `Courses` (a `list`). 
# - `Department`
# - `Title`. 

# ### Check-in (conceptual)
# 
# What would be a useful `dict` structure to represent information about instructors? For example, say we wanted to represent:
# 
# - `username` (e.g., `sttrott`)
# - `Name` (e.g., `Sean Trott`)
# - `Courses` (e.g., `['COGS 14A', ...]`)
# - `Department` (e.g., `COGS`)
# - `Title` (e.g., `Assistant Teaching Professor`)

# ### A possible implementation
# 
# One approach is to use **nested dictionaries**.
# 
# - At the top level, each instructor is represented by their `username`.  
# - Each PID then maps onto a nested dictionary, which contains their `Name`, `Email`, and any other info we need.

# In[9]:


instructors = {
    'sttrott': {'Name': 'Sean Trott',
                'Courses': ['COGS 14A', 'CSS 1', 'CSS 2'],
               'Title': 'Assistant Teaching Professor',
               'Department': 'COGS'},
    'sellis': {'Name': 'Shannon Ellis',
                'Courses': ['COGS 18', 'COGS 108', 'COGS 137'],
               'Title': 'Associate Teaching Professor',
               'Department': 'COGS'},
    'wstyler': {'Name': 'Will Styler',
                'Courses': ['LING 6', 'LING 101'],
               'Title': 'Director of CSS',
               'Department': 'LING'},
}


# ### Indexing our nested `dict`
# 
# We can index into this `dict` as we would normally. Note that now, the **value** is itself a `dict`.

# In[10]:


instructors['sellis']


# #### Check-in
# 
# How might we index the `Title` of a particular instructor? I.e., what if we wanted to find out the `Title` of `sttrott`?

# In[11]:


### Your code here


# #### Nested indices
# 
# Indexing into a **nested dictionary** follows the same logic––we can *chain together* index statements to retrieve a particular value.

# In[12]:


instructors['sttrott']['Title']


# In[13]:


instructors['sttrott']['Department']


# ### Check-in
# 
# How would you retrieve the list of `username`s (i.e., keys) in this `dict`?

# ### Solution

# In[14]:


usernames = instructors.keys()
print(usernames)


# ## `sort`ing a dictionary
# 
# With a `list`, the `sorted` function returns a sorted version of that list (by default, with smaller values at the beginning).
# 
# With a `dict`, the `sorted` function returns a sorted list of **keys**.

# In[15]:


fruits_dict = {'banana': 5, 'apple': 2, 'orange': 3}
### Sorted list of keys
sorted(fruits_dict)


# ### Sorting by key
# 
# We can use `sorted`, along with a dictionary comprehension, to sort our dictionary by **key**.
# 
# Logic:
# 
# - For each key in a **sorted** list of `fruits_dict` keys...
# - Add that key/value to a new `dict` called `fruits_sorted`.
# - This will create a `dict` whose keys are sorted alphabetically.

# In[16]:


fruits_sorted = {i: fruits_dict[i] for i in sorted(fruits_dict)}
fruits_sorted


# ### Check-in
# 
# How would you sort the dictionary below by key?

# In[17]:


instructors = {'Trott': 'COGS', 
               'Ellis': 'COGS', 
               'Styler': 'LING'}
### Your code here


# ## Conclusion
# 
# Now you've had a more thorough introduction to Python **dictionaries**.
# 
# In the section below, there are several **bonus problems**, in case you do want extra practice; however, you're not expected to complete them on your own. (We will review them in class if there is time.)

# ## Bonus problems
# 
# These are **bonus problems** that are particularly challenging or advanced. I've included them in case:
# 
# - The question occurred to you (i.e., you want to know how to sort by value).  
# - You're keen to get some more hands-on practice with Python.
# - There's extra time in lecture to review them. 

# ### Problem: Sorting a nested dictionary
# 
# How would you sort a nested dictionary, e.g., `instructors`, by key?

# In[18]:


instructors = {
    'sttrott': {'Name': 'Sean Trott',
                'Courses': ['COGS 14A', 'CSS 1', 'CSS 2'],
               'Title': 'Assistant Teaching Professor',
               'Department': 'COGS'},
    'sellis': {'Name': 'Shannon Ellis',
                'Courses': ['COGS 18', 'COGS 108', 'COGS 137'],
               'Title': 'Associate Teaching Professor',
               'Department': 'COGS'},
    'wstyler': {'Name': 'Will Styler',
                'Courses': ['LING 6', 'LING 101'],
               'Title': 'Director of CSS',
               'Department': 'LING'},
}


# #### Solution
# 
# The solution ends up being the same as sorting a simpler dictionary.

# In[19]:


instructors_sorted = {i: instructors[i] for i in sorted(instructors)}
instructors_sorted


# ### Problem: Sorting by value
# 
# What if we wanted to sort `fruits_dict` by **value**––i.e., such that `orange` should go before `banana`? 
# 
# This ends up being considerably more complicated! We'll rely on:
# 
# - The ability to use a custom **sorting mechanism** in `sorted`.  
# - Wrapping a list of `tuples` in a call to `dict`.

# In[20]:


### How can we make sure "banana" goes last?
fruits_dict


# #### Part 1: sort items by value
# 
# First, we can sort our list of items.
# 
# By default, calling `sorted` will sort by the first element in each `tuple`.

# In[21]:


## By default, sorts by first element
sorted(fruits_dict.items())


# However, we can use a `lambda` operator (to be discussed more next week), to tell Python we want to instead sort by the *second element*.

# In[22]:


## Sort instead by second element
sorted(fruits_dict.items(), 
       ### This retrieves the *second* element in a tuple instead
       key = lambda item: item[1])


# #### Part 2: sort items by value
# 
# Now, we can **wrap** that sorted list of items in a call to `dict`.

# In[23]:


fruits_sorted_value = dict(
    sorted(fruits_dict.items(), 
           key = lambda item: item[1]))
fruits_sorted_value

