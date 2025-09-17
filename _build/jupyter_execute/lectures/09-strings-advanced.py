#!/usr/bin/env python
# coding: utf-8

# # Strings in Python (continued)

# ## Review: strings
# 
# > A **string** is a *sequence* of characters. It belongs to the `str` type in Python.
# 
# A string stores characters as text, and is created using single (`''`) or double (`""`) quotes; multi-line strings can be created with three quotes (`""" """`). 

# In[1]:


print("This is a string that I'm printing.")


# In[2]:


print("This is also a string, even though it has numbers like 2, 4, and 100 * 2.")


# ## Goals of this lecture
# 
# Today, we'll cover a variety of **advanced operations** we can use with strings. These are not exhaustive (see [here](https://www.w3schools.com/python/python_strings_methods.asp) for a huge list), but they will highlight the flexibility and utility of strings.
# 
# - Modifying case (`.upper()`, `.lower()`, and `.title()`) 
# - Replacing characters (`.replace()`)
# - Concatenating strings using `+`.  
# - Splitting a string (`.split()`). 

# ## Modifying case
# 
# Often, you'll need to modify the **case** of a `str` (i.e., make it either *upper* or *lower* case). 
# 
# - One use-case for this is needing to *compare* two strings, but not caring about whether they have identical case. 
# - E.g., "APplE" is the same *word* as "apple", but these strings wouldn't evaluate as equal.

# In[3]:


"APPLE" == "apple"


# In[4]:


"apple" == "apple"


# ### `upper` and `lower`
# 
# As the names imply, `upper` and `lower` are both *functions* that you can use on a `str`.  

# In[5]:


"APPLE".lower()


# In[6]:


"apple".upper()


# In[7]:


"APPLE".lower() == "apple"


# ### `title`
# 
# The `title` function is a variant of `upper`/`lower`, which just capitalizes the *first* letter of each word.

# In[8]:


og_string = "introduction to programming for computational social science"
og_string.title()


# Note that if you have capital letters *after* the first letter of a word, these will now become lowercase!

# In[9]:


og_string = "CSS"
og_string.title()


# ### Evaluating case
# 
# Just as you can **modify** the case of these strings, you can also evaluate it:
# 
# - `isupper()` 
# - `islower()` 
# - `istitle()`
# 
# These functions all check whether a string conforms to those patterns.

# In[10]:


"CSS".isupper()


# In[11]:


"CSS".islower()


# In[12]:


"I Love Programming".istitle()


# ### Check-in
# 
# If you called `istitle()` on the following string, would it evaluate to `True` or `False`?

# In[13]:


test_str = "I love CSS"
### Your answer/code here


# ### Other helpful evaluation methods
# 
# There are a few other helpful methods for **evaluating** properties of a string:
# 
# - `isdigit`: checks if the characters are entirely digits (e.g., $0, 1, ..., 9$)  
# - `isalpha`: checks if the characters are entirely alphabetic characters (e.g., `abcd...`). 
# - `isspace`: checks if the string is entirely space characters (e.g., ` `). 

# ## Replacing characters
# 
# Another common operation is [**replacing** elements of a string](https://www.w3schools.com/python/ref_string_replace.asp). 
# 
# Examples:
# 
# - In a `list` of filenames, replacing every `-` with a `_`. 
# - Removing certain words or characters, e.g., replacing every instance of a word with a ` `.  
# 
# This can be done with the `replace` function.

# In[14]:


## Replace "-" with "_"
og_filename = "css-lab-1"
og_filename.replace("-", "_")


# ### Replacing the first $N$ instances
# 
# `replace` can also be used to replace only the first $N$ instances of a string. 

# In[15]:


## Replace only the first instance of "bananas"
og_string = "bananas, apples, bananas, grapes"
og_string.replace("bananas", "oranges", 1)


# ### Check-in
# 
# Use the `replace` function to replace the **first 2 instances** of `-` with `_`.

# In[16]:


original_filename = "css-ps1-fa22-test.py"
### Your code here


# ### `replace` is case-sensitive
# 
# Note that `replace` attempts an **exact match** of the `str` you're looking to replace.
# 
# - This includes exact **case match**. 
# - `"apple" != "APPLE"`. 

# In[17]:


case_mismatch = "I like Apples"
### replace won't do anything here
case_mismatch.replace("apples", "bananas")


# In[18]:


case_mismatch = "I like Apples"
### replace will replace it here
case_mismatch.replace("Apples", "bananas")


# ## Concatenating strings
# 
# > String **concatenation** simply means *combining* multiple strings.
# 
# Often, you'll need to *combine* the characters in multiple strings.
# 
# - Combining the **directory path** and a **filename** to get the full path of a file.
# - Combining parts of strings to get a valid **URL**.  
# - Combining the first and last name of a client to `print` out the **full name**.

# ### Approach 1: the `+` operator
# 
# The `+` operator can be used to **combine** multiple `str` objects.

# In[19]:


"Comput" + "ational"


# In[20]:


"css1/" + "lab1/" + "file.py"


# #### Check-in
# 
# What do you notice about how these strings are combined? Is a space added between each constituent `str` or no?

# #### Watch out for spaces (and lack thereof)!
# 
# By default, `+` will just combine two different string objects directly.
# 
# That is, `"Hello" + "World"` will become `"HelloWorld"`.
# 
# If you want to add a space *between* these objects, make sure to add a space character in your concatenation operation.

# In[21]:


p1 = "Hello"
p2 = "World"
p1 + " " + p2


# #### Check-in
# 
# Why does the code below throw an error? 
# 
# **Bonus**: What would you need to do to make it *not* throw an error?

# In[22]:


2 + " cats"


# #### Concatenating an `int` to a `str`
# 
# The `+` operator assumes you are concatenating multiple `str` objects. Thus, trying to combine an `int` with a `str` this way will throw an error.
# 
# However, you can use **type-casting** to turn the `int` into a `str`, and then combine them.

# In[24]:


str(2) + " cats"


# #### Check-in
# 
# Use the `+` operator to combine the variables below into a single string (in order, i.e., `var1` followed by `var2`, etc.). 
# - Add a space between each variable. 
# - Watch out for conflicting types!

# In[28]:


var1 = "This"
var2 = "Is"
var3 = "CSS"
var4 = 1
#### Your code here


# ### Approach 2: using `format`
# 
# The `format` method can also be used to merge multiple strings together.
# 
# - This approach is less intuitive at first, but is very flexible.  
# - I use this approach when I'm `print`ing out lots of custom variable values, e.g., as in an output message.
# 
# With `format`, you can declare "variables" within a `str` using the `{x}` syntax. 

# In[29]:


first = "Sean"
last = "Trott"
print("Hello, {f} {l}".format(f = first, l = last))


# #### Check-in
# 
# Use `format` to `print` out a message that reads: 
# 
# `"Welcome to CSS 1"`.

# In[30]:


department = "CSS"
number = "1"
#### Your code here


# ### Approach 3: using `join`
# 
# Another somewhat common use-case is **joining** strings that are currently stored as elements of a list.
# 
# The `join` syntax starts with the *character* (or character*s*) you'll be using to **join** each `str` together.
# 
# - This could be a space character, an underscore, or anything you want.  
# - It then makes a call to `.join(list_name)`. 

# In[36]:


separate_str = ['The', 'quick', 'brown', 'fox', 'jumped']
separate_str


# In[37]:


" ".join(separate_str)


# #### Check-in
# 
# Use `join` to turn the following list of directory and sub-directory names into a full file path, connected by the `"\"` symbol. 

# In[39]:


dirs = ["css", "1", "labs", "lab1"]
#### Your code here


# ### Other approaches
# 
# There are a number of [other approaches](https://www.pythontutorial.net/python-string-methods/python-string-concatenation/) to concatenating strings. 
# 
# Personally, I primarily use:
# 
# - The `format` operator when I'm `print`ing out complicated strings. 
# - The `+` operator for everything else.  

# ## `split`ting a string
# 
# Just as you can `join` parts of a `list` into a `str`, you can also `split` a `str` into a `list`!
# 
# Common use cases:
# 
# - Extracting directories and sub-directories of a file path.  
# - **Tokenizing** a sentence, i.e., retrieving all the distinct *words* (e.g., in English, written words are typically separated by spaces).  
# - Extracting different **hash-tags** from a tweet (e.g., `"#CSS#Programming"`). 

# In[41]:


example_sentence = "The quick brown fox jumped over the lazy dog"
example_sentence.split(" ")


# #### Check-in
# 
# How many **words** (i.e., character-sequences separated by spaces) are in the sentence below?
# 
# Hint: use a combination of `split` and `len` to solve this question.

# In[44]:


test_sentence = "This sentence has a number of different words and your goal is to count them"
### Your code here


# ## Conclusion
# 
# Strings are **ubiquitous** in Python. Now that you've had a brief introduction, you'll have a better understanding of:
# 
# - Indexing and looping through strings.  
# - Checking `str` objects for various features, e.g., whether they are upper or lower-case.  
# - Using `split` and `join` to convert `str` to and from `list` objects, respectively.  
# 
# Coming up next, we'll explore `list`s in more depth.
