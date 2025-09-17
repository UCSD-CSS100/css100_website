#!/usr/bin/env python
# coding: utf-8

# # 04-Review (Fundamentals)

# ## Goals of this lecture
# 
# This lecture is a quick refresher on **Python fundamentals**.
# 
# - Variables.
# - Defining and using functions.  
# - Conditional statements.
# - Loops. 
# 
# Hopefully, much of this will be review from CSS 1 (and lab 1).

# ## Variables
# 
# > A **variable** stores a particular value.  
# 
# - Unlike literals (e.g., an `int`), the value of a variable can change (i.e., it can **vary**).  
# - Variables can be assigned using the **assignment operator** (`=`). 
# - Once you've assigned a variable, you can *use* it by referencing that variable name.

# In[1]:


## Example variable
my_int = 5


# In[2]:


## Using this variable
my_int + 2


# In[3]:


## Changing the value of the variable
my_int += 10
my_int


# ### Rules on assigning variables
# 
# - Names on the left, values on the right (e.g., `test_var = 2`).  
# - Names are case sensitive (the variable `test_var` cannot be accessed with `test_VAR`).  
# - Variable names must begin with a letter.  
#    - They can contain a number (e.g., `test1`) or under-score, but can't *begin* with a number or under-score. 
# - Python [*mostly*](https://realpython.com/lessons/reserved-keywords/) doesn't care how you name your variables, though you should!
#    - Remember that code is intended to be **read** by others––so make sure it's clear!

# ### `type`s of objects
# 
# The value assigned to a variable can have different [**types**](https://www.w3schools.com/python/python_datatypes.asp). 
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

# ### Some `type`s have special functions
# 
# In Python, different `type`s of objects have different functions.
# 
# - The `str` object has the `replace` and `split` function.  
# - The `list` object has the `append` and `join` function.

# In[4]:


my_str = "CSS 1"
my_str = my_str.replace("1", "2")
my_str


# In[5]:


my_str.split(" ")


# ### Some `type`s are "collections"
# 
# - Both `list`s and `dict`ionaries store **collections** of items.

# In[6]:


### example list
my_list = [1, 2, "a"]
my_list


# In[7]:


### example dictionary
my_dictionary = {'a': 1, 'b': 2}
my_dictionary


# ## Functions
# 
# > A **function** is a re-usable piece of code that performs some operation (typically on some *input*), and then typically returns a result (i.e., an *output*). 
# 
# A function is defined using the `def` keyword:
# 
# ```python
# def func_name(arg1):
#     ### Whatever the function does
#     return some_value
# ```
# 
# Once a function has been created, you can *use* it.

# ### Functions: a simple example
# 
# The function `square` below returns the result of multiplying the input `x` by itself.

# In[8]:


def square(x):
    return x * x


# In[9]:


square(2)


# In[10]:


square(3)


# ### Check-in: functions vs. variables
# 
# Suppose we define a function called `cube`, which **cubes** some input `x`. How would we *call* that function, e.g., on an input like `2`?
# 
# - `cube`
# - `cube()`
# - `cube(2)`
# - `cube 2`

# ### Check-in: decoding a function
# 
# What does the following function do?

# In[11]:


def mystery_func(x, n):
    return x % n == 0


# #### Solution
# 
# Here, `mystery_func` checks whether `x` is divisible by `n`.

# In[12]:


mystery_func(10, 2)


# In[13]:


mystery_func(10, 3)


# ### Default values
# 
# > A **default value** is the value taken on by an argument *by default*. If no other value is specified, this is the value assumed by the function.
# 
# In the function definition, a default value can be specified by setting: `arg_name = default_value`.
# 
# - In the example below, `x` is required.
# - But `n` has a default value of `2`.

# In[14]:


def is_divisible(x, n = 2):
    return x % n == 0


# In[15]:


is_divisible(10) ### Assumes n = 2


# In[16]:


is_divisible(10, 3) ### Override with n = 3


# ### Check-in: positional vs. keyword arguments
# 
# An argument to a function can be indicated using its **position** or a **keyword**. Which of these is demonstrated in the code below? 
# 
# - Positional
# - Keyword
# - Both

# In[17]:


is_divisible(24, n = 3)


# ## Control Flow
# 
# > **Control flow** refers to tools we can use to control which lines of code get executed, when.
# 
# In Python, there are two main ways to control the "flow" of our program:
# 
# - **Conditional statements**: `if/elif/else`
# - **Loops**: `for/while`

# ## Conditional statements
# 
# > In a nutshell, a **conditional** is a statement that checks for whether some *condition* is met.
# 
# We can use the `if` command to **control** which lines of code are executed.

# In[18]:


x = "One string"
y = "One string"
if x == y:
    print("These strings are the same.")


# ### `else`
# 
# > An `else` statement tells Python what to do if an `if` statement evaluates to `False`.

# In[19]:


x = "One string"
y = "Different string"
if x == y:
    print("These strings are the same.")
else:
    print("These strings are different")


# ### Conditionals and functions
# 
# Conditional statements become particularly useful when we combine them with functions.

# In[20]:


def square_if_even(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return x


# ### Check-in
# 
# How would you write a function `fizzbuzz` that:
# 
# - Takes a number `x` as input. 
# - `return`s "Fizz" if the number is divisible by `3`.
# - `return`s "Buzz" if the number is divisible by `5`.
# - `return`s "FizzBuzz" if the number is divisible by both `3` and `5`.

# In[21]:


### Your code here


# #### Solution

# In[22]:


def fizzbuzz(x):
    if x % 5 == 0 and x % 3 == 0:
        return "FizzBuzz"
    if x % 3 == 0: 
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"


# ### Check-in
# 
# How would you write a function called `contains_letter` that:
# 
# - Takes both a `word` and a `letter` as inputs.  
# - Checks whether the `word` contains that `letter`.
#   - `if` it does, it `print`s out "Yes".
#   - Otherwise, it `print`s out "No".
# 

# In[23]:


### Your code here


# #### Solution

# In[24]:


def contains_letter(word, letter):
    if letter in word:
        print("Yes")
    else:
        print("No")


# In[25]:


contains_letter("dog", "o")


# In[26]:


contains_letter("cat", "o")


# ## Loops
# 
# > A **loop** is a way to repeat the same piece of code multiple times.
# 

# ### When should you use a loop?
# 
# **Rule of thumb**: if you find yourself copying/pasting the same code many different times...you might think about using a loop!  
# 
# More generally: in programming, we often want to execute the same action *multiple times*. 
# 
# - Apply the same instruction to every item on a `list`.  
# - Continue running some code until a condition is met.  

# ### `for` loops in action
# 
# > A `for` loop is used for [iterating over a sequence](https://www.w3schools.com/python/python_for_loops.asp). 
# 
# A `for` loop uses the syntax: 
# 
# ```python
# for elem in list_name:
#     # Do something
# ```

# In[27]:


## This is a list in Python
numbers = [1, 2, 3]
### This is a for loop
for number in numbers:  
    print(number)


# ### `for` loops and functions
# 
# Like `if` statements, a `for` loop becomes especially powerful when combined with a function.

# In[28]:


def multiply_list(numbers):
    product = 1 ## why do I start at 1, not 0?
    for i in numbers:
        product *= i
    return product ## note the indentation!


# In[29]:


multiply_list([1, 2, 3])


# ### Check-in
# 
# Write a function called `find_vowels`, which:
# 
# - Takes as input a `str`.
# - `return`s a list of the **vowels** in that string.

# In[30]:


### Your code here.


# ### Solution

# In[31]:


def find_vowels(s):
    vowels = []
    for c in s:
        if c.lower() in "aeiou":
            vowels.append(c)
    return vowels


# In[32]:


find_vowels("programming")


# In[33]:


find_vowels("cat")


# ## Conclusion
# 
# This was intended as a **rapidfire review** of Python fundamentals, including:
# 
# - Basic Python syntax.  
# - Defining functions.
# - Using `if` statements.
# - Using `for` loops.
# 
# Next time, we'll review packages that will be helpful for working with data, such as `pandas`.
