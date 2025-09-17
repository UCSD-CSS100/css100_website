#!/usr/bin/env python
# coding: utf-8

# # Python Basics: Operators and Syntax

# ## Announcements
# 
# - **Lab 1** due today.
# - **Problem set 1** will be released today (due *next Wednesday*).
#   - Similar to Lab 1, but to be completed independently.
# - **Lab 2** will also be released by end of day (due *next Monday*).  

# ## Goals of this lecture
# 
# - What is syntax?
# - Key [**operators** in Python](https://www.w3schools.com/python/python_operators.asp). 
#    - Math.
#    - Logic. 
#    - Comparisons.  
#    - Identity.  
#    - Membership. 
# - Indentation in Python. 

# ## Python Syntax: Overview
# 
# The **syntax** of a programming language is the set of rules about how different symbols can be combined to produce correctly structured statements.  
# 
# Like other programming languages, Python has particular **syntactic rules**.  
# - Failure to follow these rules results in a `SyntaxError`.
# - Although following syntactic rules can *sometimes* seem annoying, remember that there's always a reason the language was designed in a certain way.  
# 
# Syntax goes hand-in-hand with the **operators** we use in a language, and the rules about how those operators are used.

# ## Operators
# 
# An **operator** is used to perform an *operation* on variables and values.
# 
# We've already seen an example of an operator: `=` is used to **assign** a variable name to some value.

# In[1]:


### Assignment operator
x = 10


# But operators can also include basic *arithmetic operations*, like addition (`+`) and subtraction (`-`). 

# In[2]:


### Addition operator
1 + 1


# ### Arithmetic in Python
# 
# Python code can be used to perform arithmetic calculations with **numeric** values, including:
# 
# | Operation | Symbol |
# | --------- | ------ |
# | Addition | `+`|
# | Subtraction | `-`|
# | Division | `/`|
# | Multiplication | `*`|
# | Exponentiation | `**`|
# | Modulus | `%`|
# | Floor division | `//`|

# In[3]:


### Exponentiation
2 ** 3


# In[4]:


### Division
2 / 4


# In[5]:


### Modulus
8 % 3


# #### Order of operations
# 
# If a single line of code has *multiple operations*, Python executes these operations according to [PEMDAS](https://www.cuemath.com/numbers/pemdas/). 
# 
# - E.g., `()` first, then `**`, then `*`/`/`, then `+`/`-`. 
# - Word of caution: it's easy to misplace parentheses (`()`)––many experienced programmers can introduce **bugs** this way.

# ### Check-in
# 
# What value would `x` take on in the following code?
# 
# ```python
# x = (1 + 2) / (18 - 3)
# ```

# In[6]:


### Your code here


# ### Check-in
# 
# What about this code?
# 
# ```python
# x = 1 + 2 / 18 - 3
# ```

# In[7]:


### Your code here


# #### "Adding" strings
# 
# The `+` operator can also be applied to **strings**. In this case, it **concatenates** the strings (i.e., puts them together).
# 
# We'll revisit this soon when we discuss strings in more depth.

# In[8]:


### Addition "concatenates" strings
"a" + "pple"


# ### Assignment in Python
# 
# We've already learned about the basic **assignment operator**: the symbol `=` can be used to assign a value to a variable name.
# 
# There are also a few "syntactic tricks" with this operator, such as:
# 
# | Operation | Symbol | Example |
# | --------- | ------ | ------- |
# | Add to variable | `+=` | `x += 1`|
# | Subtract from | `+=` | `x -= 1`|
# 
# 
# These are equivalent to just writing out something like: `x = x + 1`.

# In[9]:


x = 10
x += 1
x


# ### Logical operators
# 
# Logical operators can be used to produce a `boolean` value. They are particularly useful when writing **conditional statements**, which we'll discuss soon.
# 
# | Symbol | Description | Example |
# | --------- | ------ | ------- |
# | `and` | Returns `True` if both parts are true | `True and True`|
# | `or` | Returns `True` if at least one part is true | `True or False`|
# | `not` | Returns the reverse | `not True`|
# 

# In[10]:


True and False


# In[11]:


True or False


# In[12]:


True and (not False)


# ### Comparison operators
# 
# A **comparison operator** *compares* one value to another. This includes whether those values are the *same*, but also whether one is larger or smaller than the other, and so on.
# 
# | Symbol | Description |
# | --------- | ------ | 
# | `==` | Equal | 
# | `!=` | Not Equal | 
# | `>` | Greater Than |
# | `<` | Less Than |
# | `>=` | Greater Than or Equal To|
# | `<=` | Less Than or Equal To|

# In[13]:


## Equal operator
2 == (1 + 1)


# In[14]:


## Greater than
2 > (1 + 1)


# #### Comparing strings
# 
# Note that these operators can also be applied to *strings*.
# 
# - The equality operator (`==`) tests whether the two strings have the same characters.  
# - The greater/less than operators (`>` and `<`) test the relative *ordinal value* of the strings, i.e., if they were to be sorted.

# In[15]:


## Are these strings equal?
"test" == "test"


# In[16]:


## Is b "larger" than a?
"b" > "a"


# In[17]:


## Is ab "larger" than aa?
"ab" > "aa"


# ### Check-in
# 
# Would the following code return `True` or `False`?
# 
# ```python
# "bat" > "cat"
# ```

# In[18]:


### Your code here


# ### Identity operators
# 
# An **identity operator** determines whether two objects are `identical` or not. There are just two symbols:
# 
# | Symbol | Description |
# | --------- | ------ | 
# | `is` | Identical | 
# | `is not` | Not Identical | 
# 
# 
# Note that **identity** is [not exactly the same as **equality**](https://realpython.com/python-is-identity-vs-equality/#comparing-equality-with-the-python-and-operators). 
# 
# - A test for **equality** (`==`) checks whether two *values* are the same.  
# - A test for **identity** (`is`) checks whether two operands point to the same *object* in memory.  
#   - You don't need to know all the details here––the most important thing is that they're subtly different.

# In[19]:


# Comparing equality vs. identity
a = "This is a fairly long string"
b = "This is a fairly long string"
print(a == b)
print(a is b)


# #### Identity vs. Equality: The details
# 
# Two variables can have the same **value** (they're *equal*), but reference different objects in **memory** (i.e., they're not *identical*). We can access the `id` of an object using `id(x)`. 

# In[20]:


x = 1000
y = 1000
print(id(x))
print(id(y))
print(x == y)
print(x is y)


# Behind the scenes, Python creates *objects* in memory whenever we declare a new variable referencing a value, with *some exceptions*:
# 
# - Simple/short strings.  
# - Integers between `-5` and `256`
# 

# In[21]:


x = 1
y = 1
print(x is y)
print(x == y)


# ### Membership operators
# 
# A **membership operator** determines whether a given value or variable is present within a larger sequence. 
# 
# 
# | Symbol | Description |
# | --------- | ------ | 
# | `in` | Is the variable/value in the sequence? | 
# | `not` | Is the variable/value *not* in the sequence? | 
# 
# 
# This will become clearer when we discuss different kinds of **sequences**, such as *strings* (`str`) and *lists* (`list`). For now, it's enough to compare/contrast the examples below.

# In[22]:


print("a" in "apple")
print("b" in "apple")


# In[23]:


print("a" not in "apple")
print("b" not in "apple")


# ## Indentation in Python
# 
# In Python, **indentation** matters for how different blocks of code get evaluated.
# 
# - Everything within an *indented block* gets interpreted as happening "within" that block (e.g., within a loop).
# - This will make more sense when we discuss **conditional logic** (`if/else`) and **loops** (e.g., a `for` loop).  
# - If you indent where it's not necessary or expected, you'll get a `SyntaxError`. 

# In[24]:


## We shouldn't have indented here
    print("Don't indent here")


# In[25]:


## It's appropriate to indent after a conditional statement
x = 2 - 1
if x == 1:
    print("This is an indented block")


# ## Conclusion
# 
# As always, there's more we could discuss. However, hopefully this was a useful introduction to the notion of an **operator** in Python, along with some of the syntactic rules around how to use these operators in code. 
