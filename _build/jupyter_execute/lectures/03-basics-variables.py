#!/usr/bin/env python
# coding: utf-8

# # Python Basics: Variables

# ### Announcements
# 
# - **Extra credit survey** is due today (already lots of responses, so thank you!). 
# - For people with trouble logging into DataHub (i.e., a **network error**), try the following:
#    - Visit this page: https://datahub.ucsd.edu/hub/spawn
#    - Click "Services" --> "manual-resetter" --> follow instructions.
#    - (This has worked for us and also students we've suggested it to.)

# ## Goals of this lecture
# 
# In this lecture, we'll introduce the concept of a **variable**.
# 
# - What is it?  
# - What do we use it for?  
# - How does it work?  

# In[1]:


99 % 2


# In[2]:


3 != 5


# In[ ]:





# In[ ]:





# ## Python expressions
# 
# An **expression** is just a block of code, e.g.,
# 
# ```python
# a = 1
# b = 2
# c = a + b
# ```
# 
# Key things to remember:
# 
# - Python will **execute** (run) an expression from top to bottom.  
# - Expressions must obey the **syntax** of Python (we'll discuss this more later).  
# 

# ### Literal expressions
# 
# - Some kinds of code will be interpreted "literally" by Python.  
# - A [literal](https://www.scaler.com/topics/python/literals-in-python/) is a kind of object/quantity whose value does not change during the execution of a program (i.e., these are *not* variables).  

# In[3]:


## Literals can be numbers
2


# In[4]:


# Or strings
"Hello, world!"


# In[5]:


# Or a "boolean"
True


# In[6]:


# Or even the special value "None"
None


# ### Check-in
# 
# Why do you think executing the cell above (i.e., with `None`) doesn't return anything, whereas executing a cell with `True` or `2` does? ([More on `NoneType`](https://www.w3schools.com/python/ref_keyword_none.asp).)

# ### Variables
# 
# - A **variable** stores a particular value.  
#   - You can think of this as a **container**.  
#   - Technically, a variable *points* to an object in memory.  
# - Unlike literals, the value of a variable can change (i.e., it can **vary**).  
# - Variables can be "set" (or "assigned") using the **assignment operator** (`=`). 
# 
# 

# In[7]:


## This assigns the variable name "example_var" to the value 1.
example_var = 1
example_var


# In[8]:


## This assigns the variable name "example_var" to the value 1.
example_var2 = "This is a string"
example_var2


# ### Check-in
# 
# What happens to the value of the variable `test_var` if we run the following code? Feel free to run it in the Jupyter notebook if you're not sure.
# 
# ```python
# test_var = 3
# test_var = test_var + 4
# ```

# In[9]:


## Your code here


# ### Check-in
# 
# What happens to the value of the variable `test_var` if we run this code? Feel free to run it in the Jupyter notebook if you're not sure.
# 
# ```python
# test_var = 3
# test_var = test_var + new_var
# ```

# In[10]:


## Your code here


# ### Quick detour: Exceptions and Errors
# 
# - Sometimes, there's an [**error**](https://docs.python.org/3/tutorial/errors.html) in our code.  
# - Fundamentally, an error (or "exception") means that our code can't run as written. 
# - But there are multiple reasons that an error can arise:  
#    - A `SyntaxError` means that we used the wrong syntax in our expression, e.g., it was formatted incorrectly.  
#    - Even if our code is formatted correctly, other errors can arise, such as a `NameError`.  
# - When an error arises, Python will give us a message indicating the type and source of the error.

# In[11]:


# This code is referencing "new_var", which hasn't been defined
test_var + new_var


# ### Assigning variables (cont'd)
# 
# In programming, `=` means **assignment**: it is *not* a test for **equality**.  
# 
# - The `==` operator is a test for equality (e.g., `1 == (2 - 1)`). 
# 
# Multiple variables can be assigned in a single line:
# 
# ```python
# test_var = new_var = 2
# ```
# 
# The Python **interpreter** will always start with the rightmost value (e.g., `2`), then proceed to the left. 
# 
# Note that the order of these terms matters:
# 
# ```python
# test_var = 2   # This is okay!
# 2 = test_var   # This is not okay!
# ```

# ### Rules on assigning variables
# 
# - Names on the left, values on the right (e.g., `test_var = 2`).  
# - Names are case sensitive (the variable `test_var` cannot be accessed with `test_VAR`).  
# - Variable names must begin with a letter.  
#    - They can contain a number (e.g., `test1`) or under-score, but can't *begin* with a number or under-score. 
# - Python [*mostly*](https://realpython.com/lessons/reserved-keywords/) doesn't care how you name your variables, though you should!
#    - Remember that code is intended to be **read** by others––so make sure it's clear!

# ### Reserved words
# 
# Python mostly doesn't care how you name variables, but there are a handful of **reserved words**. 
# 
# The [full list is here](https://realpython.com/lessons/reserved-keywords/), but here are some examples:
# 
# - `in` 
# - `True`
# - `for`
# 
# Importantly, these keywords are **special literals** in Python, meaning they have a built-in function or value.
# 
# - `in` checks if a value is in a `list`.  
# - `True` is a boolean type (as opposed to `False`).  
# - `for` is a way to start a `for` loop (more on this later).   

# In[8]:


## This yields a SyntaxError
for = 3


# ## Namespaces
# 
# A [**namespace**](https://realpython.com/python-namespaces-scope/) is the "space" where a given set of variable names have been *declared*.
# 
# Recall that *assignment* creates a symbolic name that *points* to a particular value:
# 
# ```python
# new_var = 2
# ```
# 
# - Critically, that pointer only exists in the current namespace. 
# - If you opened up a separate Jupyter notebook, `new_var` would not be defined.

# ### Types of namespaces
# 
# Python has several types of namespaces:
# 
# 1. **Built-in**: Built-in objects within Python (e.g., **Exceptions**, **lists**, and more). These can be accessed from anywhere.  
# 2. **Global**: Any objects defined in the main program. These can be accessed anywhere in the main program once you've defined them, but not in another Jupyter notebook, etc.
# 3. **Local**: If you define new variables within a *function*, those variables can only be accessed within the "scope" of that function. (This will make more sense when we discuss functions.)

# ### Check-in
# 
# What happens when you type in `whos?` And what does that `Type` column mean?

# In[9]:


whos


# ## Variable Types
# 
# Variables/values have different [**types**](https://www.w3schools.com/python/python_datatypes.asp). Intuitively, this is the "type" of thing that a variable is (a string, a number, etc.).  
# 
# Here are some of the possible **types** in Python:
# 
# | Type | Description | Example |
# | ---- | ----------- | ------- |
# | `str` | String/text | `"A String"`|
# | `int` | Integer     | `2`|
# | `float` | Float       | `2.6789`|
# | `list`| List | `[1, 2, 3]`|
# | `dict`| Dictionary | `{'a': 2}`|
# | `bool`| Boolean | `True`|
# | `NoneType`| None | `None`|
# 

# ### `int` vs. `float`
# 
# An **integer** stores a whole number, like `1`. 
# 
# A **float** stores a decimal-point number, like `1.5`.
# 

# ### `str`
# 
# A **string** (`str`) stores *characters* as text.
# 
# - Strings are defined by wrapping a sequence of characters in quotes.  
# - Note that a string doesn't have to be *words*: `int_string = "1"` would define a string with the character `"1"`.  
# 

# ### `bool`
# 
# A **boolean** (`boolean`) stores either `True` or `False`.  
# 
# - Booleans will become very important when we want to use **conditional statements**, e.g., "if X, do Y...".  
# - When you check for equality using `==`, the output is a boolean.

# In[10]:


### Checking for equality
1 == 2


# ### Checking variable `type`
# 
# If you're not sure what the **type** of a variable is, you can use the `type` function.
# 

# In[11]:


type(2)


# In[12]:


type(2.77)


# In[13]:


type("some words")


# ### Check-in
# 
# Suppose we execute the following code:
# 
# ```
# start_var = 1
# new_var = str(start_var)
# type(new_var)
# ```
# 
# What do you think the `type` of `new_var` would be?

# ### Casting
# 
# We can use [casting](https://www.w3schools.com/python/python_casting.asp) to force a particular variable to take on a certain type.
# 
# - `x = int(1)` will ensure that `x` is an `int`.  
# - `x = str(1)` will ensure that `x` is a `str`.  

# In[14]:


x = str(1)
print(type(x))


# ### How do different types interact?
# 
# The `type` of a variable determines what it it can and can't do.  
# 
# - Two `int` variables can be added, subtracted, etc.  
# - But you can't add or subtract an `int` from a `str`.  
#     - This would cause a `TypeError`!
# - (However, note that you *can* "add" two `str` variables together––this just **concatenates** them.)

# In[39]:


1 + 1 # This is fine


# In[40]:


1 + "test" # This is not okay


# In[46]:


"test" + "test" # This is okay


# ### `type` can sometimes be tricky
# 
# Even if *we* think something is a numeric type, if it's wrapped in quotes, it'll be interpreted as a string.
# 

# In[47]:


numeric_string = "1" # This is a string
type(numeric_string)


# In[48]:


numeric_int = 1 # This is an int
type(numeric_int)


# ## Debugging Guide: best practices
# 
# When **reading code**, it's very helpful to put yourself in the mind of the Python interpreter.
# 
# Remember:
# 
# - Python reads a block of code from top to bottom.  
# - When interpreting an **assignment** statement, Python evaluates the right-hand side of the expression first, then works leftward.  
# - For each line of code, think about the **state** of the namespace.
#    - Which variables are defined?  
#    - What are their types and values?
# 
# When **debugging**, it's helpful to `print` out the value of different variables at different points.

# ### Check-in
# 
# Will the code below run successfully without an error? If so, what is the value of `c`?
# 
# ```python
# a = 1
# b = 'new'
# c = a + b
# ```

# In[17]:


### Your code here


# ### Check-in
# 
# Will the code below run successfully without an error? If so, what is the value of `c`?
# 
# ```python
# a = 1
# b = 'new'
# a = str(a)
# c = a + b
# ```

# In[21]:


### Your code here


# ### Using `print` to debug
# 
# We can `print` out the *value* and the `type` of different variables throughout a block of code.
# 
# This helps us **isolate** where exactly the code is going wrong.

# In[22]:


a = 1
b = 2
print(type(a))
print(type(b))
c = str(b)
print(type(c))
d = a + c


# ## Style Guide: best practices
# 
# Technically, you can use whatever style you want when defining variables (e.g., `new_var`, `NEW_VAR`, `newVar`, etc.).
# 
# However, it helps to be *consistent*––and within particular programming communities, ceratin styles are preferred.
# 
# In Python, many people follow these practices:
# 
# 1. Put a **space** around either side of the assignment operator (`a = 1`, not `a=1`).  
# 2. Use **snake_case** for variable names (`new_var`, not `newVar`).  
# 3. Use **informative** variable names (`current_amt`, not `a`).  

# ## Conclusion
# 
# This was an introduction to **variables** in Python. There's lots more we could discuss, but hopefully now you have a better sense of:
# 
# 1. What a variable is.  
# 2. Some of the rules/guidelines around variables.  
# 3. What you might use a variable for.
# 
# The coding lab will give you lots more practice with variables, but if you want even more, [W3 schools](https://www.w3schools.com/python/python_variables.asp) has a nice tutorial too.
