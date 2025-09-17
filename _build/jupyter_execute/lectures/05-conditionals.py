#!/usr/bin/env python
# coding: utf-8

# # Control Flow: Conditionals

# ## Announcements
# 
# - Lab 2 is due **next Monday**.  
# - Problem set 1 is due **next Wednesday**.
# - Quick check-in: https://forms.gle/n48nBZYM8XsHf35g6

# ## Goals of this lecture
# 
# - What is "control flow"?  
# - What is a **conditional**?
# - Conditionals in action (`if/elif/else`).  
# - Complex and nested conditional statements.

# ## What is control flow?
# 
# By default, Python commands are executed in a *linear* order, i.e., line by line.  
#  - Unless we tell Python otherwise, *each line* will be executed once.
# 
# But sometimes it's useful to **control**:
# 1. Which lines get executed?
# 2. How many times do those lines get executed?  
# 
# These control "parameters" correspond, roughly, to:
# 
# 1. Conditional statements (`if/elif/else`).  
# 2. Loops (e.g., `for` or `while`). 

# ## What is a conditional?
# 
# > In a nutshell, a **conditional** is a statement that checks for whether some *condition* is met.
# 
# We can use the `if` command to **control** which lines of code are executed.

# In[1]:


condition = True
if condition:
    print("This code will only run if the condition is True.")


# In[2]:


condition = False
if condition:
    print("This code will only run if the condition is True.")


# ### Check-in
# 
# Consider the code block below. Which part is the **conditional statement**?

# In[3]:


x = 10
y = 5
if x > y:
    print("X is bigger than Y.")


# ### Check-in
# 
# Consider the code block below. Why won't the `print` statement run?

# In[4]:


x = "One string"
y = "Another string"
if x == y:
    print("These strings are the same.")


# ### What belongs in an `if` statement?
# 
# - An `if` statement should evaluate to `True` or `False`.  
#   - This includes the outcome of any **comparison** operation (`>`, `==`, etc.).  
#   - Technically, it also includes numbers/strings (which evaluate to `True`) and `NoneType` (which is equivalent to `False`).  
# - An `if` statement is *extremely useful* for modifying the behavior of a program, depending on some **condition**.

# In[5]:


if None:
    print("This won't print")


# ### Check-in
# 
# What happens if our `if` statement evaluates to `False` (e.g., the statement `4 > 5` would evaluate to `False`)? 

# ### Conditionals with operators
# 
# Conditional statements can be used with **operators**. This is really useful if you want to modify your program based on whether two variables are equal (`==`), or one is larger (`>`) or smaller (`<`) than the others, and so on.

# In[6]:


checking_account = 1000
if checking_account > 200:
    print("Withdrawal allowed.")


# ## `else` statement
# 
# > An `else` statement tells Python what to do if an `if` statement evaluates to `False`.

# In[7]:


condition = False
if condition:
    print("Condition is TRUE.")
else:
    print("Condition is FALSE.")


# ### When to use an `else` statement?
# 
# An `else` statement can **only** be used after an `if` statement (see the `SyntaxError` below).  

# In[8]:


else:
    print("test")


# An `else` statement is most useful if you want two different things to happen, depending some condition:
# 
# 1. If `condition == True`, execute Action A.  
# 2. `else`, execute Action B. 

# In[45]:


condition = False
if condition:
    print("Do this if the condition is TRUE.")
else:
    print("Do this if the condition is FALSE.")


# ## Quick note on indentation
# 
# Notice that the code below an `if` or `else` statement must be **indented**, if you want it to be associated with that statement.
# 
# If there is no indented code below an `if` statement, you'll get an `IndentationError`.

# In[46]:


if 3 > 2:
print("No idententation")


# However, you *can* still have un-indented code below an `if` or `else` statement, as long as there's *also* indented code.

# In[47]:


if 3 > 2:
    print("This will execute if the condition is met.")
print("This will execute regardless.")


# ### Check-in
# 
# Which lines in the code below would actually print?
# 
# ```python
# condition = False
# if condition:
#     print("Do this if the condition is TRUE.")
# else:
#     print("Do this if the condition is FALSE.")
# print("Also do this.")
# ```

# ## `elif` statement
# 
# > An `elif` statement tells Python what to do if an `if` statement evaluates to `False`, *and* some other condition is met.
# 
# This is kind of a combination of an `if` and `else` statement.  

# In[48]:


condition1 = False
condition2 = True
if condition1:
    print("Condition 1 is true.")
elif condition2:
    print("Condition 2 is true.")


# ### When will an `elif` statement run?
# 
# An `elif` statement will *only run* if the `if` statement evaluates to `False`––even if the `elif` statement would've evaluated to `True`!

# In[49]:


condition1 = True
condition2 = True
if condition1:
    print("Condition 1 is true.")
elif condition2:
    print("Condition 2 is also true, but this won't print.")


# #### `if` vs. `elif`
# 
# The key difference between two `if` statements in a row vs. an `if/elif` statement is:
# 
# - The code under both `if` statements can run if both statements are `True`.  
# - The code under an `elif` statement will only run if the `if` statement is False.

# In[50]:


condition1 = True
condition2 = True
if condition1:
    print("Condition 1 is true.")
if condition2:
    print("Condition 2 is also true, and this will also print.")


# #### `elif` vs. `else`
# 
# - An `elif` statement cannot be placed after an `else` statement.
#    - This will generate a `SyntaxError`. 
# - It also just doesn't make sense logically. If `elif` were at the end, it'd never be evaluated anyway, since `else` covers everything other than the `if` statement.
# 

# In[51]:


if 2 > 3:
    print("True")
else:
    print("False")
elif 2 > 1:
    print("True?")


# ### Check-in
# 
# What do you expect the value of `x` to be if the following code is run? (Try to figure it out before running the code to check what `x` is.)

# In[52]:


y = 1
x = 0
if y >= 1:
    x -= 2
elif y >= 1:
    x -= 1
else:
    x += 1


# ### Check-in
# 
# What do you expect the value of `x` to be if the following code is run? (Try to figure it out before running the code to check what `x` is.)

# In[53]:


y = 1
x = 0
if y >= 1:
    x -= 2
if y >= 0:
    x -= 1
else:
    x += 1


# ### Check-in
# 
# Why did those two different code blocks behave differently?

# ### Both `elif` and `else` "attach" to the nearest `if` statement
# 
# Any given `else` or `elif` statement is attached/associated with exactly one `if` statement (the one immediately above).  
# 
# This means that we must be very *careful* to think about what each `else` statement is actually comparing against.

# ### Check-in
# 
# The following code ends up printing a contradiction (e.g., `A is True`, followed by `Neither A nor B are True`). Why is this happening?
# 
# **Hint**: Think about what we just discussed––an `else` attaches to the nearest `if` statement.

# In[54]:


A = True
B = False
C = True
if A:
    print("A is True")
if B:
    print("B is True")
else:
    print("Neither A nor B are True.")


# ## More complex conditionals
# 
# So far, we've dealt with fairly limited **conditional** statements:
# 
# 1. Each `if` checks only a single condition.  
# 2. Relatively linear ordering: `if`, `elif`, then `else`.  
# 
# But conditional statements can be considerably more complex:
# 
# 1. Each `if` statement can check multiple conditions using [logical operators](04-basics-syntax) like `or` and `and`.  
# 2. Conditional statements can be **nested**.  

# ### Using `and` and `or`
# 
# Recall that `and` and `or` can be used to evaluate *multiple* statements.  
# 
# - `and` returns `True` if all statements are `True`.  
# - `or` returns `True` if at least one statement is `True`.  
# 
# We can use these to check for more complex conditions.

# In[55]:


a = 20
b = 30
c = 40
if b > a and c > b:
    print("Both conditions are True.")


# ### Check-in
# 
# Why does the top code block execute the code under the `if` statement, while the bottom one doesn't?

# In[56]:


a = 20
b = 30
c = 25
if b > a or c > b:
    print("At least one condition is True.")


# In[57]:


a = 20
b = 30
c = 25
if b > a and c > b:
    print("Both conditions are True.")


# ### A simple use-case for `and`

# In[58]:


is_password = True
checking_account = 1000
withdrawal = 500
if is_password and (withdrawal < checking_account):
    print("Withdrawal permitted.")
    checking_account -= withdrawal
    print(str(checking_account) + " left in checking.")


# ### A simple use-case for `or`

# In[60]:


is_dog = True
is_cat = False
if is_dog or is_cat:
    print("This is a dog or cat.")
else:
    print("This is neither a dog nor cat.")


# ### Check-in: `and` vs. `else`
# 
# How would an `else` statement behave following an `if` statement using an `and` (e.g., `X and Y`)? (Choose either (1) or (2).)
# 
# 1. The `else` statement will run if both `X` and `Y` are `False`.  
# 2. The `else` statement will run if at least one of `X` and `Y` is `False.

# ### Check-in: `or` vs. `else`
# 
# How would an `else` statement behave following an `if` statement using an `or` (e.g., `X or Y`)? (Choose either (1) or (2).)
# 
# 1. The `else` statement will run if both `X` and `Y` are `False`.  
# 2. The `else` statement will run if at least one of `X` and `Y` is `False.

# ### Using nested conditionals
# 
# > A **nested conditional** is one that contains at least one `if` statement "nested" within another conditional statement.

# In[63]:


a = 8
if a > 5:
    if a >= 10:
        print("A is greater than or equal to 10.")
    else:
        print("A is bigger than 5, but smaller than 10.")
else:
    print("A is smaller than or equal to 5.")


# ### Nested `if` vs. `and`
# 
# - A nested `if` statement functions similarly to an `and` statement.
# - In both cases, some block of code will only run if **both** conditions are met.  
# - The key difference is that a nested `if` statement allows you more **granularity** in terms of evaluating which conditions are met, and what to do in each case.

# ## Code Style: Indentation
# 
# - With conditionals, it's hugely important that you keep track of your **indentation**.  
# - It's easy to introduce **bugs** by making something indented where it shouldn't be, or the other way around.  
# - Debugging practice:
#    - As before, read each line carefully.  
#    - Track the **state** of each variable.  
#    - Track whether a given conditional statement evaluates to `True` or `False`, and what would happen next.

# ## Conclusion
# 
# - **Conditional statements** give you extra control over which lines in your Python program get run.  
# - This is very useful for modifying the behavior of your program, depending on some other condition.  
#    - When we discuss **functions** (and later on, **filtering** datasets), this will become even clearer.
# - Important to keep track of your **indentation** when dealing with `if` statements, especially nested statements.
