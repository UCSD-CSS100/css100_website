#!/usr/bin/env python
# coding: utf-8

# # Functions

# ## Goals of today's lecture
# 
# Today we'll be focusing on **functions** in Python.
# 
# - What is a function? What are they good for?
# - How do you create or define a function?  
#    - Key concepts: `def`, `return`, and **arguments**.  
#    - How do you use or *call* a function?  
# - More details on functions:
#   - Input `type`.  
#   - Default argument values.

# ## What is a function?
# 
# > A **function** is a re-usable piece of code that performs some operation (typically on some *input*), and then typically returns a result (i.e., an *output*). 
# 
# Breaking this down:
# 
# - **Input**: a variable defined by the user that is *passed into* a function using the `(input)` syntax.
#    - Also called an **argument**.
#    - Functions can have multiple **arguments**.
# - **Output**: the variable **returned** by a function after this operation is performed.  
#    - If a `return` value is not specified, a function will return `None`.

# ### A very simple function
# 
# We'll explore the syntax more in a bit, but this will give you a sense for what we're talking about.

# In[1]:


def square(x):
    """Returns the square of X."""
    return x**2


# In[2]:


square(1)


# In[3]:


square(2)


# ## Why functions?
# 
# In principle, we could just rewrite the same code each time we want to execute that operation. So why bother defining functions at all?
# 
# The answer lies in **modular programming**.
# 
# - As operations become more and more complex, it becomes unwieldy (and just inefficient) to copy/paste the *same code* again and again.  
# - In modular programming, we emphasize building **re-usable chunks of code**.
# - Functions (and loops) are ways to re-use chunks of code that solve basic, recurring problems.
# 
# Learning to think in a modular way can be hard! But it's a helpful approach to **breaking down a problem into its sub-components**.

# ### Functions we've encountered
# 
# We've already encountered a number of functions in this course.
# 
# #### `print`
# 
# - Input: something to `print`.  
# - Output: technically, `None`.  
# - "Side effects": `print`s out input to designated log (by default, the terminal/Jupyter cell).

# In[4]:


print("Hello!")


# #### `sorted`
# 
# - Input: a `list` 
# - Output: a sorted `list`.

# In[5]:


unsorted = [2, 1, 5]
sorted(unsorted)


# ## Defining a function
# 
# In Python, a new function can be created or **defined** using the `def` keyword, followed by the name of the function.
# 
# See the `square` function definition below:
# 
# - Function name: `square`. 
# - Function arguments: `x`.  
# - Function `return`: `x ** 2`.  

# In[6]:


def square(x):
    """Returns the square of X."""
    return x**2


# ### Executing a function
# 
# To **execute** a function, we can reference the function name (like a variable), followed by the parentheses `()` and any arguments/input for the function.

# In[7]:


## Function name = square
## Input = 2
square(2)


# In[8]:


## Function name = square
## Input = 4
square(4)


# ### What type is a function?
# 
# A function belongs to a special `type` in Python, called `function`.

# In[9]:


type(square)


# ### A more complex function
# 
# What if we wanted a function that did the following:
# 
# - `if` the input `x` is **even**, we square it.  
# - `if` the input `x` is **odd**, we just `return` that number.

# In[10]:


def square_if_even(x):
    """Squares x if x is even; otherwise return x."""
    if x % 2 == 0: ## check if even
        return x ** 2 ## if so, return square
    else: ## otherwise..
        return x ## just return x


# In[11]:


## 2 is even, so square it
square_if_even(2)


# In[12]:


## 3 is odd, so just return it
square_if_even(3)


# ### Another more complex function
# 
# So far, our functions have only had a **single argument**. But functions can take in *many* arguments. 
# 
# Let's define a function with *two inputs*, which just adds those inputs together.

# In[13]:


def add_two_numbers(num1, num2):
    """Adds num1 to num2."""
    return num1 + num2


# In[14]:


add_two_numbers(1, 2)


# In[15]:


add_two_numbers(5, 3)


# ### Check-in
# 
# What would the function below produce if the input `x` was `25`?
# 
# More generally: how would you describe what this function *does*? 

# In[16]:


def mystery_func(x):
    if x % 5 == 0:
        return True
    return False


# ### Solution
# 
# `mystery_func` can be thought of as a binary "check" for whether a particular number is divisible by `5`. 

# In[17]:


mystery_func(25)


# In[18]:


mystery_func(28)


# ### Check-in
# 
# Write a function that takes a `name` as input and `return`s the formatted `str`: `"My name is {name}."`
# 
# The code below can get you started:
# 
# ```
# def hello(name):
# ### your code here
# ```

# In[19]:


# Your code here


# ### Solution

# In[20]:


def hello(name):
    return "My name is {name}".format(name=name)


# In[21]:


hello("Sean")


# ## Interim summary
# 
# What we've learned so far:
# 
# - A **function** is a re-usable piece of code that does something.  
# - A function can take in some **input** and `return` some **output**.  
# - In principle, a function can be as complex as you need (can contain `if` statements, `for` loops, etc.).
#    - Word of caution: a function should be modular.
# - In principle, a function also take in many different inputs and even produce multiple outputs. 
#    - Again: be careful not to make things too complex.

# ## Function arguments: the details
# 
# Beyond the basics, there are several other important things to know about the **arguments** for a function:
# 
# - It's important to be aware of what `type` your function expects as an argument.
# - Arguments can have **default values**.  
# - Some arguments can be accessed with a **keyword**, while others are **positional** arguments.

# ### Argument `type`
# 
# Some languages, like Java, require that you specify the `type` of an argument (and variable names, etc.).
# 
# Python doesn't require that, but it's still important to be aware of.
# 
# - Otherwise, you can run into a `TypeError`.
# - If you're interested: Python uses something called [duck typing](https://en.wikipedia.org/wiki/Duck_typing). 

# #### Example of a `TypeError`
# 
# Here, the `square` function performs an operation with `x` that requires `x` to be an `int`.

# In[22]:


def square(x):
    return x ** 2
square("two")


# #### How to avoid a `TypeError`?
# 
# In practice, the best way to avoid a `TypeError` is to **document your code**. 
# 
# - In the `docstring` under a function, you can write details about what the function expects, e.g., whether the input is an `int`, a `str`, etc.

# In[23]:


def square(x):
    """
    Parameters
    ------
    x: int
      number to be squared
    
    Returns
    -------
    int
      square of x
    """
    return x ** 2


# #### Check-in
# 
# Will the function below result in an error if you called it on the input `"test"`? Why or why not?

# In[24]:


def mystery_func(x):
    return x ** 3


# #### Solution
# 
# As before, Python throws an error, because there's no way to raise a `str` to the power `3`. 

# In[25]:


mystery_func("test")


# ### Default values
# 
# > A **default value** is the value taken on by an argument *by default*. If no other value is specified, this is the value assumed by the function.
# 
# In the function definition, a default value can be specified by setting: `arg_name = default_value`.
# 
# - In the example below, `name` is required.
# - But `major` has a default value of `"COGS"`.

# In[26]:


def my_info(name, major = "COGS"):
    return "My name is {name}, and my major is {major}.".format(name = name, major = major)


# Even if we don't specify a value for `major`, the function will run just fine––it just uses the default value.

# In[27]:


my_info("Sean")


# #### Overriding a default value
# 
# A default value can be overridden in the call to the function itself. 
# 
# - Note that this can reference the argument name (`major`), or just occupy the correct **position** in the series of arguments. (More on this later.)

# In[28]:


my_info("Sean", major = "LIGN")


# In[29]:


my_info("Sean", "LIGN")


# #### Arguments without a default must be referenced!
# 
# If an argument *doesn't* have a default, the function will throw an error if you don't pass in enough arguments.

# In[30]:


my_info()


# #### Check-in
# 
# Why does the following code not throw an error?

# In[31]:


my_info("LIGN")


# ### Positional vs. keyword arguments
# 
# An argument to a function can be indicated using either:
# 
# - Its **position**, i.e., in the list of possible arguments.
# - A **keyword**, i.e., the *name* of that argument.

# A **positional argument** uses the relative position of the arguments to determine which is which. 

# In[32]:


def exponentiate(num, exp):
    return num ** exp


# In[33]:


## Raise 2 ^ 3
exponentiate(2, 3)


# In[34]:


## Raise 3 ^ 2
exponentiate(3, 2)


# A **keyword argument** uses the *name* of the argument to determine which is which. 
# 
# - Even if the positions are swapped, the *keyword* will take priority. 
# - (Note that the best practice is to keep the order consistent, however.)

# In[35]:


## Raise 2 ^ 3
exponentiate(num = 2, exp = 3)


# In[36]:


## Raise 2 ^ 3
exponentiate(exp = 3, num = 2)


# #### Position before keyword
# 
# - Once you've used a keyword argument, you can't rely on **position** for any arguments coming after that keyword. This will throw a `SyntaxError`.
# - However, a **positional argument** can come before a **keyword argument**.
# 

# In[37]:


## This is incorrect
exponentiate(num = 2, 3)


# In[38]:


## This is fine
exponentiate(2, exp = 3)


# ## Conclusion
# 
# This concludes our initial introduction to **functions**. If there is time, there are also two more challenging practice problems below to work on.

# ## Practice problems

# ### Problem 1
# 
# Write a function called `fizzbuzz`. It should take in a single argument, `x`, and follow this behavior:
# 
# - If `x` is divisible by both `3` and `5`, return the `str` `"fizzbuzz"`. 
# - If `x` is divisible by only `3` (and not `5`), return `"fizz"`).
# - If `x` is divisible by only `5` (and not `3`), return `"buzz"`).
# 
# Note: this is part of a famous problem in **coding interviews**!

# In[39]:


def fizzbuzz(x):
    pass ## Replace this with your code


# ### Problem 2
# 
# Write a function called **product**, which takes a `list` (`lst`) as input, and returns the **product** of every item in the list.

# In[40]:


def product(lst):
    pass ## Replace this with your code


# ## Practice problems: solutions

# ### Problem 1

# In[41]:


def fizzbuzz(x):
    if x % 5 == 0 and x % 3 == 0:
        return "fizzbuzz"
    if x % 3 == 0: 
        return "fizz"
    if x % 5 == 0:
        return "buzz"


# In[42]:


fizzbuzz(15)


# In[43]:


fizzbuzz(25)


# ### Problem 2

# In[44]:


def product(lst):
    prod = 1
    for i in lst:
        prod = prod * i
    return prod


# In[45]:


product([1, 2, 3])


# In[46]:


product([9, 10, 0])

