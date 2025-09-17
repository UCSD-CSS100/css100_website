#!/usr/bin/env python
# coding: utf-8

# # Classes

# ## Goals of this lecture
# 
# This lecture will cover **classes** in Python.
# 
# While there's not enough time to discuss classes in detail, we'll focus on the following topics:
# 
# - What is a **class**? What is it useful for?
# - How do you define a class in Python?  
# - Practical: how do you find out information about a `class`? 

# ## What is a class?
# 
# > A Python `class` defines an **object**. Each object is a way to organize *data* (**attributes**) and *operations* to perform on that data (**methods**).  
# 
# We've encountered objects before.
# 
# - A `list` is a type of object, which has associated **methods**: 
#    - `append`, `pop`, and more. 
# - A `dict` is also a type of object.  
#    - `update`, `keys`, `items`, and more.
# - So are different types of data (`bool`, etc.) and even `function`s. 

# ### What makes objects useful?
# 
# Objects are useful for **organizing** data and operations in a structured way.
# 
# - Example: consider representing the **date**.
# - Format is **MM/DD/YYYY**: 09/18/2022

# #### Using a `str`
# 
# We could represent the date with a `str`, but it's hard to perform operations with this representation. (E.g., what if we wanted to compare this date to another date?)

# In[1]:


## Representing as a string
date_str = "09/18/2022"
date_str


# #### Using a `list`
# 
# We could represent the date with a `list`, but then we'd have to remember which *index* corresponds to each feature.

# In[2]:


## Each index corresponds to MM, DD, and YYYY
date_list = ['09', '18', '2022']
date_list


# #### Using a `dict`
# 
# We could also represent the date with a `dict`, which adds more structure.

# In[3]:


## Now each *key* tells us more about what a given value reflects.
date_dictionary = {'day': 18,
                  'month': 9,
                  'year': 2022}
date_dictionary


# #### Using `datetime`
# 
# But we could also use a Python object that's **engineered to represent the date specifically**.

# In[4]:


## This is called an import statement
## We're *importing* a useful package to use
from datetime import date


# In[5]:


date_object = date(day = 18,
                  month = 9,
                  year = 2022)
date_object


# #### Classes can unlock more affordances
# 
# Because the `date` object is built specifically to represent **dates**, it has many custom *methods* we can use to perform operations on those dates.

# In[6]:


## Retrieve day information
date_object.day


# In[7]:


## Convert to calendar time
date_object.ctime()


# #### Comparing dates!
# 
# Having a custom object makes certain operations much easier, like comparing dates.

# In[8]:


date2 = date(day = 17, month = 9,
            year = 2022)
## How far apart are these dates?
date_object - date2


# ### Attributes vs. methods
# 
# An **attribute** is data associated with an object. We can access attributes using the dot (`object.attr_name`) syntax.

# In[9]:


date2.day


# A **method** is a function that belongs to an object, and which operates on that object. We can access methods using the dot syntax as well (`object.method_name()`), but they also require parentheses `()`, since they are functions.

# In[10]:


date2.ctime()


# ### Summary: why classes?
# 
# - Often, we need to work with a set of **data** and **operations** to perform on that data.
# - In theory, we can do that with a combination of `list`s and `dict`ionaries.  
# - But a *custom class* makes things much easier.
#   - Python has *tons* of custom objects, that make your life easier in this regard.
#   - We'll also learn how to define a class ourselves.

# ## Defining a class
# 
# To create a new class, we use the `class ClassName` syntax.

# In[11]:


## By convention, class names are capitalized
class Cat():
    
    # By default, make color "black"
    color = "black"
    
    # This is a custom *method* 
    def meow(self, n_times = 2):
        return "Meow" * n_times
    
    # This is another custom *method*
    def purr(self, n_times = 4):
        return "Purr" * n_times


# ### Instantiating a class
# 
# Now that we've defined a class, we can *instantiate* it.
# 
# - **Instantiation** means creating a particular *instance* of that class.
#    - Analogy: "Cat" is an abstract concept/category, but "patroclus" could be a specific cat.
# - Syntax: `instance_name = ClassName()` 

# In[12]:


## Create a cat object
patroclus = Cat()
# Use purr method
patroclus.purr()


# In[13]:


## Access attribute
patroclus.color


# In[14]:


# Use meow method
patroclus.meow(n_times = 1)


# ### Instance attributes
# 
# The `__init__` function allows us to define a class with custom **attributes** as well as methods.
# 
# - The `self` keyword refers to specific *instances* of that class.

# In[15]:


class Cat():    
    ## __init__ method allows custom color
    def __init__(self, color):
        self.color = color
        
    def meow(self, n_times = 2):
        return "Meow" * n_times
    def purr(self, n_times = 4):
        return "Purr" * n_times


# In[16]:


## Create two cats with different colors
patroclus = Cat(color = "black")
rex = Cat(color = "orange")
print("Patroclus is {x}".format(x = patroclus.color))
print("Rex is {x}".format(x = rex.color))


# ### Check-in
# 
# For an object `person` with the attribute `height`, how would you access that attribute?
# 
# - `person.height`
# - `person.height()`
# - `height(person)`

# In[17]:


## Your response here


# ### Solution
# 
# You'd use `person.height` for the attribute.

# ### Check-in
# 
# For an object `person` with the method `speak`, how would you access that method?
# 
# - `person.speak`
# - `person.speak()`
# - `speak(person)`

# In[18]:


## Your response here


# ### Solution
# 
# You'd use `person.speak()` for the method.

# ### A more complex class.
# 
# Let's define a custom `class` called `BankAccount`. It should have the following features:
# 
# - It stores an **attribute** called `balance`, which tells us how much money is in the account.  
# - It has a method called `deposit`, which balance us to deposit a custom amount of money.  
#    - `deposit` should affect the value of `amount`.
# - It has a method called `withdraw`, which allows us to take out a custom amount of money.
#    - `withdraw` should affect the value of `balance`.
# 
# Try thinking through this yourself first, then we'll discuss a solution.

# In[19]:


### Your code here


# ### Solution: `BankAccount`

# In[20]:


class BankAccount():
    
    def __init__(self, starting_amount):
        self.balance = starting_amount
    
    def deposit(self, cash):
        # Change amount by this much
        self.balance += cash
    
    def withdraw(self, cash):
        # Change balance
        self.balance -= cash
        # Return amount
        return cash


# #### `BankAccount` in practice

# In[21]:


# Create an instance, with starting_amount = 10
my_account = BankAccount(starting_amount = 10)
my_account.balance


# In[22]:


# Deposit 5 more dollars
my_account.deposit(5)
my_account.balance


# In[23]:


# Withdraw 15 dollars
my_account.withdraw(15)
my_account.balance


# ### Check-in
# 
# Right now, `withdraw` doesn't check to make sure we have enough money in the account. How could we change this method, so that it instead:
# 
# - Checks that `balance >= cash`.  
# - If `balance >= cash`, return `cash` and change `balance`. 
# - If `balance < cash`, `print` out a message saying: "Not enough in account!"

# In[24]:


# Your code here


# ## Finding out how a class works
# 
# In CSS, you'll probably use classes defined by *other people* more frequently than you define your own.
# 
# Thus, it's important to know how to find out how a class works.
# 
# - How do I **instantiate** this class?
# - What kinds of **methods** does this class have?  

# ### Using `dir`
# 
# The `dir` keyword will list all **attributes** and **methods** associated with an object.
# 
# - The **under-score** in those attributes/methods (called **dunders**) are special features associated with most Python objects.

# In[25]:


dir(patroclus)


# ### Other helpful resources
# 
# - The `?ClassName` syntax will bring up a window giving you information about that class (i.e., the documentation).  
# - You can also search for this documentation on Google, e.g., "Python ClassName documentation".  
# - Finally, StackOverflow often has answers!
# 
# Learning to navigate these resources is an important part of programming. For me, much of my time programming is spent learning about a custom object/class in Python and looking at examples of it in use.

# ## Conclusion
# 
# - This is by no means a complete introduction to classes.
# - An Intro to Programming class in CSE would spend considerably more time, as classes are a key part of object-oriented programming and software engineering.  
# - For our purposes, it's important to **know what a class is**, **how to define a class**, and **how to find out information about classes**.  
# 
