#!/usr/bin/env python
# coding: utf-8

# # Functions (advanced)

# ## Review: what is a function?
# 
# > A **function** is a re-usable piece of code that performs some operation (typically on some *input*), and then typically returns a result (i.e., an *output*). 
# 
# Breaking this down:
# 
# - **Input**: a variable defined by the user that is *passed into* a function using the `(input)` syntax.
#    - Also called an **argument**.
# - **Output**: the variable **returned** by a function after this operation is performed.  
#    - If a `return` value is not specified, a function will return `None`.

# In[1]:


def square(x):
    """Returns the square of X."""
    return x**2


# In[2]:


square(2)


# ## Goals of today's lecture
# 
# Today we'll be covering some more advanced topics with **functions**:
# 
# - Returning multiple values.
# - Namespaces.  
# - `lambda` functions. 
# - Varying number of arguments.  
# 
# We'll also be getting more hands-on practice with functions!

# ## Returning multiple values
# 
# Functions can `return` multiple values, or even another function. 
# 
# This can be useful when:
# 
# - The goal of a `function` can't be distilled into a single value.  
# - You want to `return` multiple bits of information about something, e.g., its `len`, its value, and so on.  
# 
# Multiple values can be separated with a `,`.

# ### Multiple `return` values: an example
# 
# Suppose we wanted a function that takes two numbers as input, and returns both:
# 
# - Their sum.  
# - Their product.

# In[3]:


def sum_product(a, b):
    return a + b, a * b


# In[4]:


sum_product(10, 200)


# ### Check-in
# 
# What do you notice about the `type` of the object that gets returned when a function returns *multiple values*?

# In[5]:


sum_product(5, 2)


# ### `return` and `tuple`s
# 
# By default, a `function` will package these multiple values into a `tuple`.
# 
# - It's possible to return them in another form, e.g., in a structured dictionary. 
# - But if you use the `return a, b` syntax, `a` and `b` will returned like: `(a, b)`

# ## Namespaces

# ### Review: what is a namespace?
# 
# > A [**namespace**](https://realpython.com/python-namespaces-scope/) is the "space" where a given set of variable names have been *declared*.
# 
# Python has several types of namespaces:
# 
# 1. **Built-in**: Built-in objects within Python (e.g., **Exceptions**, **lists**, and more). These can be accessed from anywhere.  
# 2. **Global**: Any objects defined in the main program. These can be accessed anywhere in the main program once you've defined them, but not in another Jupyter notebook, etc.
# 3. **Local**: If you define new variables within a *function*, those variables can only be accessed within the "scope" of that function.

# ### The global namespace
# 
# So far, we've mostly been working with variables defined in the **global namespace**.
# 
# - I.e., once we define a variable in a notebook (and run that cell), we can reference it in another cell.

# In[6]:


## define global variable
my_var = 2


# In[7]:


## reference global variable
print(my_var)


# ### Functions have their own namespace
# 
# If you declare a variable **within** a function definition, that variable does *not* persist outside the scope of that function.
# 
# In the function below, we declare a new variable called `answer`, which is eventually `return`ed.
# 
# - However, the **variable itself** does not exist outside the function.

# In[8]:


def exponentiate(num, exp):
    ### "answer" is a new variable 
    answer = num ** exp
    return answer


# In[9]:


### This will throw an error
print(answer)


# ### Global variables *can* be referenced inside a function
# 
# If you've defined a variable in the global namespace, you *can* reference it inside a function.
# 
# - **Word of caution ⚠️**: this can sometimes make for confusing code. 

# In[7]:


## define global variable
my_var = 2
## define function
def add_two(x):
    ## references my_var
    return x + my_var

add_two(2)


# ### Check-in
# 
# What would value of `new_var` be after running the code below?
# 
# What about `test_var`?

# In[8]:


test_var = 2
def test_func(x):
    test_var = x ** 2
    return test_var
new_var = test_func(5)


# ### Solution
# 
# The global variable `test_var` is *unaltered* by `test_func`.

# In[9]:


test_var = 2 ## global variable
def test_func(x):
    test_var = x ** 2
    return test_var
new_var = test_func(5)
print(new_var)
print(test_var)


# ### Using `whos`
# 
# Remember that you can check which variables are defined using `whos`.

# In[10]:


whos


# ## `lambda` functions
# 
# So far, we've focused on creating functions using the `def func_name(...)` syntax.
# 
# However, Python also has something called [**lambda functions**](https://www.w3schools.com/python/python_lambda.asp). 
# 
# - Syntax: `lambda x: ...`. 
# - Main advantage: can be written in a single line, best if you want a **simple function**.  
#    - Excellent for passing as *arguments* into other functions, such as `sorted`.

# In[9]:


square = lambda x: x**2
print(square(2))
print(square(4))


# In theory, `lambda` functions can have multiple arguments.

# In[10]:


exp = lambda x, y: x*y
print(exp(2, 3))


# ### Check-in
# 
# Convert the function below into a `lambda` function.

# In[11]:


def add_one(x):
    ## Adds 1 to x
    return x + 1

### Your code here


# ### Solution

# In[12]:


# Lambda solution
add_one = lambda x: x + 1
print(add_one(1))


# ### `lambda`: summary
# 
# - `lambda` is an easy, efficient way to define a simple function.  
# - In practice, `lambda` is most useful when defining functions "on the fly".
#    - As **arguments** to pass into another function.
#    - As **nested functions** within another function. 

# ## Varying number of arguments
# 
# So far, we've assumed that we *know* how many arguments will be passed into a function at any given time. But this isn't always the case.
# 
# Fortunately, Python gives us two ways to handle an **arbitrary number** of arguments:
# 
# - `*args`: allows a `function` to receive an arbitrary number of (positional) arguments, which can be "unpacked" as needed. The function treats them as a `tuple`. 
# - `**kwargs`: allows a `function` to receive a `dictionary` of (keyword) arguments, which can be "unpacked" as needed. 

# ### `*args` in practice
# 
# The `*args` syntax allows you to input an arbitrary number of arguments into a function.

# In[13]:


def my_function(*fruits):
    print("The last fruit is " + fruits[-1] + ".")


# In[14]:


my_function("strawberry")


# In[15]:


my_function("strawberry", "apple")


# #### Check-in
# 
# How exactly is this working? That is, what is `my_function` treating `*fruits` as? 
# 
# Try `print`ing out `fruits` to see what's going on.

# In[16]:


### Your code here


# #### Solution
# 
# The `*args` syntax tells Python to allow *an arbitrary number* of arguments. Any argument ends up being packaged as a `tuple`, which the body of your function code can then unpack.

# In[17]:


def my_function(*fruits):
    print(fruits)


# In[18]:


my_function("apple", "strawberry", "banana")


# ### `**kargs` in practice
# 
# The `*kwargs` is similar to `*args`, but allows for an arbitrary number of **keyword arguments**.
# 
# - These are treated as a `dict` by the function.

# In[19]:


def my_function(**fruits):
    print(fruits)


# In[20]:


### Keyword and value are automatically placed into dictionary
my_function(name = "apple", amount = 5)


# In[21]:


### The specific keyword can be altered as needed
my_function(name = "banana", cost = 10)


# #### Why use this?
# 
# In general, `**kwargs` is useful when you want **flexibility**.
# 
# For example, suppose you have a website, in which people can (optionally) fill out the following information:
# 
# - `Name`. 
# - `Email`. 
# - `Phone number`.
# - `Location`.
# 
# But because not everyone fills out *every field*, the function you use to store this information needs to be flexible about how many arguments it receives.

# In[22]:


def store_user(**info):
    ## For now, this is just a placeholder to demonstrate
    for item in info.items():
        print(item)


# In[23]:


store_user(Name = "Sean", Location = "San Diego")


# ## Practice problems
# 
# One of the best ways to learn a new concept is to actually practice it. Thus, I'm including a number of practice problems at the end of this lecture, which we'll work through.

# ### Problem 1: find the maximum number of a `list`
# 
# Goal: write a function that takes in a `list` of numbers as input, and finds the **maximum** of the `list`.  
# 
# The catch: you can't use the operator `max`. 
# 
# Things to consider:
# 
# - If the input `list` is empty, you should return `None`.  
# - Since you can't use `max`, you might consider using a `for` loop, checking the value of each number in turn.

# In[24]:


### Your code here


# #### Solution

# In[29]:


def find_max(lst):
    if len(lst) == 0:
        return None
    ### Start by setting max to first item in list
    m = lst[0]
    ### Then iterate through each item
    for i in lst:
        ### if item is greater than first item...
        if i > m:
            ### Reset max to new item
            m = i
    return m


# In[30]:


find_max([1, 2, 10, 5])


# In[31]:


find_max([])


# ### Problem 2: find the maximum number in a set of `*args`
# 
# Goal: write a function that takes in an arbitrary number of arguments (i.e., uses `*args`), and finds the maximum.
# 
# The catch: you can't use the operator `max`. 
# 
# Things to consider:
# 
# - If there are no arguments, you should return `None`.  
# - Since you can't use `max`, you might consider using a `for` loop, checking the value of each number in turn.

# In[33]:


### Your code here


# #### Solution

# In[55]:


def find_max(*args):
    ## if no args are presented, "args" = ([],)
    if args[0] == []:
        return None
    ### Start by setting max to first item in list
    m = args[0]
    ### Then iterate through each item
    for i in args:
        ### if item is greater than first item...
        if i > m:
            ### Reset max to new item
            m = i
    return m


# In[56]:


find_max([1, 2, 10, 5])


# In[54]:


find_max([])


# ### Problem 3: find the even numbers
# 
# Goal: write a function that takes in a `list` of numbers, and prints the even ones.

# In[57]:


### Your code here


# #### Solution

# In[58]:


def print_even(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)


# In[59]:


print_even([1, 2, 8])


# In[60]:


print_even([104, 57])


# ### Problem 4: find the tallest in a dictionary.
# 
# Suppose we want a `function` that takes in a `dict` of `Names` and `Heights`. That is, each *key* is a `Name`, and it maps onto a `Height`.
# 
# We want the function to return the `Name` of the person with the largest `Height`, *as well as* the `Height` itself.

# In[25]:


## Can't just max...that'll return "Sean"
heights = {'Sean': 67, 'Ben': 72, 'Anne': 66}
### Your code here


# #### Solution

# In[24]:


def get_tallest(info):
    ## Get all tuples...
    ### turn into list so we can index into it
    items = list(info.items())
    ## Start by assigning tallest to first in list
    tallest = items[0]
    ## Then iterate through tuples...
    for i in items:
        ### if item is taller than initial
        if i[1] > tallest[1]:
            ### Reset "tallest"
            tallest = i
    return tallest


# In[21]:


get_tallest(heights)


# In[22]:


get_tallest({'A': 20, 'B': 10, 'C': 200})

