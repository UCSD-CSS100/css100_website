#!/usr/bin/env python
# coding: utf-8

# # Dictionaries

# ## Goals of this lecture
# 
# The goal of this lecture is to introduce **dictionaries**. Python [dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) are incredibly powerful objects, which you'll end up using a lot (as well as *variants* of dictionaries) in your work.
# 
# - What is a dictionary? How is it different from a `list`?
# - How do you create a dictionary?  
# - How do you **index** into a dictionary? 
# - Updating a dictionary.  
# - Iterating through a dictionary.  

# ## What is a dictionary?
# 
# > In Python, a **dictionary**, or `dict`, is a mutable collection of items, which stores **key/value** pairings.
# 
# Key features:
# 
# - **Mutable**: dictionaries can be updated.  
# - **Collection**: like a `list`, dictionaries can contain multiple *entries*.  
# - **Key/value pairings**: unlike a `list`, dictionary entries consist of a *key* (i.e., how you *index* into that entry), and its *value* (i.e., what it maps onto). 

# ### Simple example of a `dict`
# 
# A dictionary is very useful for storing **structured information**. 

# In[1]:


person = {'Name': 'Sean Trott',
          'Occupation': 'Assistant Teaching Professor',
          'Location': 'San Diego'}
print(type(person))
print(person)


# They also make it really easy to **access** that information. 

# In[2]:


print(person['Name'])
print(person['Occupation'])


# ### `dict` vs. `list`
# 
# We could store the same information in a `list`, but it would be a little harder to work with.

# In[3]:


person_list = ['Sean Trott', 
               'Assistant Teaching Professor', 
               'San Diego']


# To access the information, we have to remember **where** a particular value was stored. This is harder to do, especially if there's not any intrinsic ordering to the values.

# In[4]:


print(person_list[0])


# ### Rules about keys and values
# 
# - A `dict` cannot contain **duplicate keys**. That is, all keys must be unique.  
# - However, multiple keys can have the same **value**.

# In[5]:


## Different keys, same value
fruits = {'apple': 25, 
         'banana': 25}
fruits


# ## How do you create a dictionary?
# 
# A dictionary (`dict`) can be created with curly brackets `{}`, along with the syntax `{key_name:value}`.

# In[6]:


simple_dict = {'a': 1,
              'b': 2}
simple_dict


# In[7]:


simple_dict['a']


# ### Keys vs. values
# 
# **Keys** are your access-point into a dictionary. 
# 
# - Must be an immutable type (e.g., a `str` or `int`); they *can't* be a `list`.  
# - Not all keys must be of same `type`.
# 
# **Values** are what the keys *map onto*.  
# 
# - Values can be anything: a `str`, `int`, `list`, or even another `dict`.

# In[8]:


allowable_dict = {'a': [1, 2, 3]}
allowable_dict['a']


# In[9]:


bad_key = {[1, 2, 3]: 'a'}


# ### Dictionary length
# 
# The `len` of a `dict` is the number of **keys** that it has (*not* the number of values).

# In[ ]:


allowable_dict = {'a': [1, 2, 3],
                 'b': [2, 3, 4, 5, 6, 8]}
len(allowable_dict)


# ### Check-in
# 
# What would the `len` of the dictionary below?

# In[10]:


test_dict = {'Artist': 'The Beatles',
            'Songs': ['Hey Jude', 'Revolution', 
                      'In My Life']}
### Your code here


# ### Check-in
# 
# What would the `len` of the dictionary below?

# In[11]:


test_dict = {'name': 'Sean',
            'items': {'food': 'sandwich',
                     'money': '$40'}}
### Your code here


# ## Indexing into a dictionary
# 
# Once you've created a dictionary, you'll want to **access** the items in it.
# 
# - An advantage of a `dict` (over a `list`) is that key/value pairings are inherently **structured**.  
# - So rather than indexing by *position*, you can index by *key*.
# 
# The syntax for indexing is: `dict_name[key_name]`. 

# In[12]:


person = {'Name': 'Sean Trott',
          'Occupation': 'Assistant Teaching Professor',
          'Location': 'San Diego'}
print(person['Name'])


# In[13]:


print(person['Location'])


# ### Check-in
# 
# How would you retrieve the value `25` from the dictionary below?

# In[14]:


test_dict = {'apple': 25,
            'banana': 37}
### Your code here


# ### Indexing requires a key
# 
# To index into a `dict`, you **need to use the key**.
# 
# - The *position* of a value will not work.  
# - The *value* itself will also not work.

# In[17]:


test_dict[0] ### will throw an error


# In[16]:


test_dict[25] ### will throw an error


# ## Updating a `dict`
# 
# Once you've created a `dict`, it's not set in stone––there are multiple ways to **modify** that dictionary.
# 
# - Adding new entries.  
# - Deleting existing entries.  
# - Combining two dictionaries.

# ### Adding new entries

# In[19]:


## First, let's create a new dictionary
registrar = {'Trott': 'COGS',
            'Fleischer': 'COGS'}
print(registrar)


# We can add a new entry using the `dict_name[key_name] = new_value` syntax.

# In[21]:


## Now we add a new entry to the dictionary
registrar['Styler'] = 'LING'
print(registrar)


# ### Check-in
# 
# Add an entry for the price of `"pasta"` to `prices_dict` below using this new syntax. 

# In[24]:


prices_dict = {'rice': 4, 'bananas': 3}
### Your code here


# ### Check-in
# 
# What would the `len` of `prices_dict` be after you've added that entry?

# In[25]:


### How long is prices_dict after you've added "pasta"?


# ### Deleting entries
# 
# We can also use the `del` function to delete specific key/value pairs from a dictionary.

# In[29]:


## First, we create a new dictionary.
attendance = {'A1': True, 'A2': False}
print(attendance)


# In[30]:


## Then, we delete the entry with the "A2" key.
del(attendance['A2'])
print(attendance)


# ### Merging dictionaries using `update`
# 
# What if we have **two different dictionaries** that we want to combine or *merge*? 
# 
# The `update` function can be used to do this.

# In[35]:


## First, we create a new dictionary.
registrar = {'Trott': 'COGS',
            'Fleischer': 'COGS'}
print(registrar)


# In[36]:


## Now, we define another dictionary with more info.
registrar_other = {'Styler': 'LING',
                   'Ellis': 'COGS',
                  'Rangel': 'COGS'}
## Finally, we "update" original registrar
registrar.update(registrar_other)


# In[37]:


print(registrar)


# ### Check-in
# 
# Recall that a dictionary cannot contain **duplicate keys**. What do you think would happen to `original_dict` if we ran the code below?

# In[39]:


original_dict = {'a': 1, 'b': 3}
new_dict = {'a': 2}
original_dict.update(new_dict)
### What happens to original_dict['a']?


# #### Updating with duplicate keys
# 
# If we `update` a dictionary with another dictionary that contains **overlapping keys**, the **new values** replace the old values.

# In[41]:


original_dict = {'a': 1, 'b': 3}
new_dict = {'a': 2}
original_dict.update(new_dict)
print(original_dict['a'])


# ## Iterating through a `dict`
# 
# Dictionaries are **structured** collections of **key/value pairings**.
# 
# As such, there are several ways to iterate (i.e., **loop**) through a `dict`:
# 
# - Iterating through a `list` of **keys** (`.keys()`).  
# - Iterating through a `list` of **values** (`.values()`). 
# - Iterating through a `list` of **key/value** `tuples` (`.items()`).

# ### Looping through keys with `.keys()`
# 
# Each dictionary can be thought of as a `list` of **keys**; each key in turn maps onto some **value**.
# 
# We can retrieve that `list` of keys using `dict_name.keys()`.

# In[42]:


courses = {'CSS 1': 'Introduction to Programming',
          'CSS 2': 'Data and Model Programming',
          'CSS 100': 'Advanced Analytic Programming'}
courses.keys()


# This `dict_keys` object behaves like a `list`: we can index into it, loop through it, and so on.

# In[43]:


for course in courses.keys():
    print(course)


# #### Check-in
# 
# How could we retrieve each **value** of the `dict` using `keys()`?

# In[44]:


### Your code here


# #### Retrieving values
# 
# Because each key maps onto a **value**, we can simply use it to index into `courses`.

# In[46]:


for course in courses.keys():
    ## Index into courses
    name = courses[course]
    print(name)


# ### Looping through values with `.values()`
# 
# We can also retrieve the **values** directly using `dict_name.values()`.

# In[48]:


courses.values()


# In[49]:


for course_name in courses.values():
    print(course_name)


# ### Looping through key/value pairings with `.items()`
# 
# Dictionaries are, at their core, a list of **key/value pairings**. 
# 
# - We can access each of these using `dict_name.items()`.  
# - `items()` returns a `list` of `tuples`:
#   - The first element of each `tuple` is the **key**.
#   - The second element of each `tuple` is the **value**.

# In[50]:


for item in courses.items():
    print(item)


# #### Assignment "unpacking"
# 
# - We can access each element of the `tuple` using indexing, e.g., `item[0]` or `item[1]`.  
# - However, sometimes it's more convenient to **unpack** these elements directly in the `for` loop itself.

# In[53]:


for code, name in courses.items():
    print(code)
    print(name)


# #### Converting back to a `dict`
# 
# We can use the `dict` function to convert a list of **items** back to a `dict`.

# In[60]:


items = courses.items()
print(items)


# In[61]:


course_dict = dict(items)
print(course_dict)


# ### Check-in: Looping through values
# 
# Use the `.items()` function to loop through `fruits_dict` below. `print` out each item in a formatted string using `format`: 
# 
# `{fruit_name}: {price}`. 

# In[57]:


fruits_dict = {'apple': 2, 'banana': 3}
### Your code here


# ### Check-in: Debug
# 
# Suppose someone writes a piece of code (see below) to loop through `fruits_dict`. Ultimately, they want to print out the price of each fruit. 
# 
# However, they keep running into an error. Can you figure out what they're doing wrong? And further, could you suggest a way to fix it?

# In[59]:


### Why is this throwing an error?
for fruit in fruits_dict.values():
    print(fruits_dict[fruit])


# ## Conclusion
# 
# This concludes our introduction to **dictionaries**.
# 
# As mentioned earlier, dictionaries are very widely used. They also help set the stage for a couple topics we'll be discussing later on:
# 
# - [Reading JSON files](https://www.json.org/json-en.html).  
# - Using `pandas.DataFrame`.  
# 
# Next time, we'll discuss a few more common operations that we use with dictionaries, and get some more hands-on practice.
