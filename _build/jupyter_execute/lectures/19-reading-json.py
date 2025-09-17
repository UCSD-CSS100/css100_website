#!/usr/bin/env python
# coding: utf-8

# # Working with JSON Files

# ## Goals of this lecture
# 
# We've already discussed the basics of **reading** and **writing** text (`.txt`) files. 
# 
# But another common file type is a `.json` file, which allows you to store **structured data**.
# 
# This lecture will cover:
# 
# - What is a `.json` file? What is JSON more generally and why is it useful?  
# - How do we **read in** a `.json` file?  
# - How do we **write** a `.json` file?  
# - JSON files vs. JSON strings.

# ## What is a `.json` file?
# 
# > A `.json` file is a **file written in the JSON file format**. It allows us to store structured data objects consisting of **key-value** pairs.

# ### What is JSON?
# 
# **JSON** = JavaScript Object Notation.
# 
# - Standard format for *representing* and *transmitting* data.  
#    - "Standard" = different people/systems agree to use this format to send and receive information.  
# - Represents data in **key-value** pairs.

# #### Check-in
# 
# What else have we seen that represents data in **key-value pairs**?

# ### A Python `dict` is a collection of key-value pairs
# 
# A **dictionary** (`dict`) stores **key-value** pairs.

# In[1]:


my_class = {'Code': '1',
           'Department': 'CSS',
           'Instructor': 'Trott',
            'Prerequisite': True,
           'Enrollment': 120}
print(my_class)


# In[2]:


my_class['Department']


# ### JSON and `dict`: an analogy
# 
# Conceptually, JSON accomplishes the same goals as a Python `dict`.
# 
# - In fact, Python programmers often *convert* a `dict` into a JSON `str` when they want to store it in a file.  
# - Similarly, you can **read in** a `.json` file and convert the contents into a `dict`.
# 
# **Bottom line**: we're not dealing with a fundamentally new data sturcture––it's another standardized way to represent **key-value pairs**.

# ## Reading in a `.json` file
# 
# Reading in a `.json` file shares some similarities with [reading `.txt` files](17-reading-text).  
# 
# - Must specify a **file path**.  
# - File path can be either *absolute* or *relative*.
# 
# But there are also some important differences:
# 
# - To **read in** a `.json` file, we'll need to `import` the `json` library.  
# - `json.load` will read in a **structured `.json` file** as a `dict`, not a `str`.

# ### Example: simple file
# 
# Here, we will work with a simple `.json` file: `data/restaurant.json`. 
# 
# - The file contains a structured representation of a restaurant.  
# - We use `json.load(...)` to **load** this representation as a `dict`.

# In[3]:


## This imports the json library
import json


# In[4]:


## As with normal .txt. files, we use "open" to open the target restaurant
with open("data/restaurant.json", "r") as fp:
    ## use json.load to load as dict
    info = json.load(fp)


# In[5]:


info


# ### `load` creates a `dict`
# 
# Now, we can work with the **contents** of this file as we would any `dict`.

# In[6]:


info['Name']


# In[7]:


info['Location']


# In[8]:


info['Cuisine']


# ### Check-in
# 
# Try reading in another file that's stored in `data`: `data/school.json`. 
# 
# What is the value of the **Name** key?

# In[9]:


### Your code here


# ### Solution

# In[10]:


## As before, we use "open" to open the target file
with open("data/school.json", "r") as fp:
    ## use json.load to load as dict
    school_info = json.load(fp)


# In[11]:


## Get name of school
school_info['Name']


# ## Writing a `.json` file
# 
# Often, you'll want to **write** a structured `dict` to a file.  
# 
# - Useful for *storing* information, so you can access it later.  
# - Useful for *transmitting* information between programs.  
# 
# We can use `json.dump(...)` to **write** (or "dump") a `dict` into a `.json` file.

# ### Simple example: course 
# 
# To start out, let's use the `my_class` dict we defined earlier.

# In[12]:


my_class['Code']


# To **write** this to a file, we:
# 
# - `open` (create) a file with the name we want to call it.  
# - Use `json.dump(dict_name, filename)`.

# In[13]:


with open("course.json", "w") as fp:
    json.dump(my_class, fp)


# #### Checking that this worked

# In[14]:


with open("course.json", "r") as fp:
    course_info = json.load(fp)
print(course_info)


# ### Check-in
# 
# Create a new `dict` called `my_info`. Add the following keys/values:
# 
# - `Name`. 
# - `Major`. 
# 
# Then, use `json.dump` to **write** this `dict` to a `.json` file called `my_info.json` to your own computer (in whichever directory you prefer).

# In[15]:


### Your code here


# #### Solution

# In[16]:


my_info = {'Name': 'Sean', 'Major': 'Cognitive Science'}
with open("data/my_info.json", "w") as fp:
    json.dump(my_info, fp)


# ## JSON files vs. JSON strings
# 
# The `load` and `dump` methods can be used to **read** and **write** a `dict` from/to a `.json` file.  
# 
# However, Python can also represent JSON as a **`str`**.
# 
# - To *read* a `dict` from a JSON `str`, use `loads` (load + *s*tring).  
# - To *write* a `dict` into a JSON `str`, use `dumps` (dump + *s*tring).

# ### `json.dumps`
# 
# - Input: a `dict`. 
# - Output: a JSON `str`.  

# In[17]:


json_str = json.dumps(my_class)
json_str


# In[18]:


type(json_str)


# ### `json.loads`
# 
# - Input: a JSON `str`.  
# - Output: a `dict`.

# ### Other objects besides `dict`s
# 
# - Technically, you can use `dumps`/`loads` for other objects, such as `str`, `list`, and more.
# - Though in my experience, a `dict` is the most common format.

# In[19]:


json.dumps([1, 2, 3])


# In[20]:


json.loads('[1, 2, 3]')


# ## Conclusion
# 
# This was a brief introduction to working with `.json` files. Hopefully you have a better handle on:
# 
# - What *is* a `.json` file?
# - How do I read and write `.json` files?  
