#!/usr/bin/env python
# coding: utf-8

# # Strings in Python

# ## Announcements
# 
# - Lab 1 grades posted. 
# - Lab 2 grades will be posted by early next week. 
# - Please direct grade questions to me (or TAs) in office hours or Piazza.

# ## Goals of this lecture
# 
# - What is a **string** (`str`) type? 
# - Why should we care about strings?
# - Working with `str` types in Python.  
#   - Assigning a string to a variable.  
#   - Indexing characters in a `str` object.  
#   - Looping through a `str` object.
# - Next time: more **complex operations** with strings.

# ## What is a string?
# 
# > A **string** is a *sequence* of characters. It belongs to the `str` type in Python.
# 
# A string stores characters as text, and is created using either single (`''`) or double (`""`) quotes.
# 
# Note that although strings are often used to store *words*, this isn't necessarily the case. A string could be:

# In[1]:


"dog"


# In[2]:


"abcdef"


# In[3]:


"1 + 4"


# With many more possibilities. Basically, *any* character that you wrap with quotes becomes part of a `str` in Python.

# ### Multi-line strings
# 
# Multi-line strings can be defined using `""" """`, as below.

# In[4]:


long_str = """
This string spans multiple lines.
This is the second line.
This is the third line.
"""
print(long_str)


# ### Side note: a `str` is a kind of sequence
# 
# > A **sequence** is a collection of items (e.g., numbers, characters, etc.) with some *determined order*.  
# 
# A `list` and `str` are both kinds of sequences. 
# 
# We'll discuss **sequences** more when we talk about `list`s, but there are a couple of important properties to remember:
# 
# - Sequences have a particular *order*.  
# - You can **index** into a sequence to obtain the item at a particular position.  

# ### Checking whether something is a `str`
# 
# Recall that you can check the **type** of a variable using `type`.

# In[5]:


type("This is a sentence.")


# In[6]:


type("1 + 4")


# In[7]:


type(1 + 4)


# ### Check-in
# 
# Which of the following variables would evaluate to a `str`?

# In[8]:


x1 = 1.5
x2 = True
x3 = "2 * 100"


# ## Why care about strings?
# 
# **Strings** are incredibly useful and versatile, so it's important to understand how they work and how to manipulate them.
# 
# Common uses of strings:
# 
# - Pretty much all text data is stored as a `str` (e.g., a text corpus, a word, etc.).  
# - Storing information that can't be represented as `int` or `bool`, such as **password**.  
# - Declaring **features** of an object in Python that can't be represented as `int` or `bool`. 
# - Representing a **filename**.
# 
# Strings are so useful that virtually all programming languages have something like a `str` type.

# ## Working with strings: basic operations
# 
# Today, we're going to focus on a few **basic operations** we can use with strings. In a future lecture, we'll talk about more complex operations.
# 
# The basic operations include:
# 
# 1. Getting the length (`len`) of a string.  
# 2. Indexing into a string (`string_name[0]`).  
# 3. Looping through a string (`for ch in string_name...`).  
# 
# You'll note that each of these operations can also be applied to a `list` type!

# ### Calculating string length with `len`
# 
# > The `len` operator calculates the number of characters in a `str` (or `list`).  

# In[9]:


x1 = "CSS"
print(len(x1))


# In[10]:


x2 = "class"
print(len(x2))


# #### Check-in
# 
# How many characters are in the string `"2 + 2"`?
# 
# Try answering before you try typing in the expression.

# #### Spaces count as characters!
# 
# An empty space (`" "`) counts as a character in Python.
# 
# Thus, the `str` `"big dog"` has one extra character than the `str` `"bigdog"`. 

# In[11]:


len("big dog")


# In[12]:


len("bigdog")


# #### Check-in
# 
# How many characters are in the `str` below?

# In[13]:


str_test = "Computational Social Science is fun."


# #### Putting quotes into a string
# 
# Certain characters, like quotes, require an **escape** character if you want to put them into a string. Otherwise they'll simply *end* the string.

# In[14]:


quote_str = "Then he said, \"I love CSS!\""
print(quote_str)


# ### Indexing into a `str`
# 
# > In programming, **indexing** into a sequence means retrieving the item at a particular position.
# 
# Because a `str` is a kind of sequence, we can retrieve the character at a particular position.
# 
# We can index into a `str` (or `list`) using the `string_name[...]` notation, where `...` would be replaced with the **index** of the character we want to retrieve.

# In[15]:


test_var = "computer"
test_var[0]


# #### Note on indexing
# 
# Python uses **zero-indexing**: the first element in a sequence is assigned the index `0`, the second is assigned `1`, and so on.
# 
# - This can be hard to get used to at first!  
# - But over time, it'll start to seem more natural.  

# #### Check-in
# 
# Which of the indexing operations below would return the letter `"S"`?

# In[16]:


s = "CSS"
x1 = s[0]
x2 = s[1]
x3 = s[2]


# #### Check-in
# 
# Why does the code below return an **error**?

# In[17]:


s = "CSS"
s[4]


# ### Slicing into a `str`
# 
# > **Slicing** is like indexing, but allows you to return a *subset* within a sequence.
# 
# For example, rather than getting the *n-th* character of a `str`, you can return the characters between index `0` and index `2`.
# 
# - To **slice**, use the syntax `[start_index:end_index]`.  
# - `start_index` is the index of the first character you want to return.  
# - `end_index` is the index of the final character you want to return, plus one.
#    - Like `range`, the final index is not "inclusive".  

# In[14]:


s = "programming"
s[0:4]


# #### Check-in
# 
# How many characters would the following **slice** return? *Which* characters would they be?

# In[15]:


s = "programming"
subset = s[5:7] ## how many characters is this?


# #### Check-in
# 
# Write a **slice** operation to return the `str` `"humid"` within the string `"dehumidify"`.

# In[16]:


original_str = "dehumidify"
### Your code here


# ### Looping through strings
# 
# > **Looping** through a `str` means repeating some piece of code for each (or a subset) of the characters within a string.
# 
# We've already discussed [loops in previous lectures](06-loops), so this will be a brief review:
# 
# - A `for` loop **iterates** through each item in a sequence (like a `str`), repeating some piece of code.  
# - A `while` loop **continues** as long as some condition is met, and can also be used to iterate through a sequence.

# #### Looping with a `for` loop

# In[17]:


seq = "CSS"
for i in seq:
    print(i)


# #### Looping with a `while` loop

# In[18]:


i = 0
seq = "CSS"
while i < len(seq):
    print(seq[i])
    i += 1


# ## Conclusion
# 
# As you learn more about Python (or other programming languages), you'll encounter **strings** more and more frequently. Next time, we'll discuss more **advanced operations** we can use with strings, such as modifying the **case** of characters in a `str`, replacing certain characters with other characters, and so on.
