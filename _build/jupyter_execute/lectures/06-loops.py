#!/usr/bin/env python
# coding: utf-8

# # Control Flow: Loops

# ## Announcements
# 
# - Lab 1 due today.  
# - PS 1 due Wednesday.  
# - Final projects: will be like a longer problem set, with more coherent questions.

# ## Goals of this lecture
# 
# - Control flow, revisited.  
# - What is a **loop**? What is **iteration**? 
# - `for` loops in action. 

# ## Control flow, revisited
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

# ## Loops, explained
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

# ### A loop is an example of *iteration*
# 
# > Iteration simply means: repeating some sequence of instructions until a specific end result is achieved.
# 
# That "end result" could be any number of things:
# 
# - You reach the end of a `list`.  
# - Some other condition is met.  
# 
# In general, we'll use the term **iterate** to mean "do over and over again".
# 
# - The expression "iterate over a list" means: *Do X to every item of that list*. 

# ### Two kinds of loops
# 
# There are two main kinds of loops you'll use in Python: `for` loops and `while` loops.
# 
# - A `for` loop runs some code for every item of a `list` or sequence.
# - A `while` loop runs a piece of code until some condition is met (e.g., `while condition == True`). 
# 
# Today, we'll focus on `for` loops.

# ### Side note: lists
# 
# - We haven't discussed `list` objects in detail yet, but we will introduce them as part of the lecture today.  
# - High-level: 
#    - A `list` is an ordered collection of elements.  
#    - Different elements can be accessed by **indexing** through the list.

# In[1]:


## This is a list in Python
numbers = [1, 2, 3]
### This is how we "index" particular elements in that list
numbers[0]


# ## `for` loops in action
# 
# > A `for` loop is used for [iterating over a sequence](https://www.w3schools.com/python/python_for_loops.asp). 
# 
# A `for` loop uses the syntax: `for elem in list_name: ...`

# In[2]:


## This is a list in Python
numbers = [1, 2, 3]
### This is a for loop
for number in numbers:  
    print(number)


# ### Check-in
# 
# What do you expect the following code block to do, if you executed it?
# 
# ```python
# for l in "apple":
#     print(l)
# ```

# A `for` loop tells Python to **iterate** over each element in a sequence.
# 
# The **content** of that loop––the **indented code** underneath the `for` statement––tells Python what to do each time.

# In[3]:


for l in "apple":
    print(l)


# ### Check-in
# 
# Approximately how many lines of code would we need if we wanted to `print` each element of a `list` with **100 items**, *without* using any kind of loop? (I.e., copy/paste the same code?)

# ### Compare and contrast

# In[4]:


### This code prints each number independently
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])


# In[5]:


### This code iterates through the list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


# ### What can you use a `for` loop on?
# 
# > You can use a `for` loop on any **sequence**.
# 
# We'll talk more about sequences next week, but they include:
# 
# - Lists, e.g., `[1, 2, 10]`.  
# - Strings, e.g., `"apple"`. 
# - Ranges, e.g., `range(10)`
# 
# 

# ### Introducing `range`
# 
# > `range` is an **operator** used to create a range of numbers, e.g., from 0 to 100. It's very useful if your main goal is to execute some code $N$ times.
# 
# Note that `range(10)` will return an iterable object of 10 numbers from *0* to *9*.

# In[6]:


for i in range(10):
    print(i)


# If you want to start at a different number (e.g., `3`), you can enter that as an argument as well.

# In[7]:


for i in range(3, 10):
    print(i)


# Remember: `range` will produce numbers going all the way up to $N - 1$, *not* $N$. 

# In[8]:


for i in range(5):
    print(i)


# ### Check-in
# 
# Write a `for` loop that `print`s out every letter in the string `"CSS"`.

# In[9]:


## First, define a string using something like: word = "CSS"
### YOUR CODE HERE


# ### Check-in
# 
# Write a `for` loop that `print`s out every letter in the string `"Computational Social Science"`, **except for the spaces**.
# 
# **HINT**: Think about how you could combine a `for` loop with an `if` statement.

# In[10]:


## First, define a string using something like: word = "Computational Social Science"
### YOUR CODE HERE


# ## Loops and conditionals, *combined* 
# 
# The real expressive power of a `for` loop comes into play when we use **conditional statements**.
# 
# - Remember that an `if` statement allows us to run a piece of code *only if* some condition is met.  

# ### Check-in
# 
# Why/how could an `if` statement be helpful when using a `for` loop? 

# ### `for` and `if`: a simple use-case
# 
# Suppose you are instructed to write a program that prints out all the **even numbers** between 1 and 11.
# 
# Breaking the problem down:
# 
# 1. First, we want to **iterate** through a `range` from `(1, 22)`.  
# 2. Then, we want to check `if` each element of that range is **even**.  
# 3. `if` a given element is even, we `print` it out.

# #### Check-in
# 
# How might we determine if a number is even?
# 
# **Hint**: Think about the *modulo* operator (`%`).

# #### `print`ing even numbers in `range(1, 22)`

# In[11]:


for num in range(1, 22): ## for loop
    if num % 2 == 0:  ## conditional statement
        print(num)  ## the code we want to execute


# ### Check-in
# 
# Suppose you're going grocery shopping. Here are the costs of each item:

# In[12]:


costs = [5, 8, 4, 10, 15]
costs


# You want to keep your costs low, so you decide not to buy anything above $9. How would you write a `for` loop that:
# 
# - Iterates through `costs`.  
# - Tracks a `final_bill` variable.  
# - Only adds items to `final_bill` if they're below 9$?
# 
# Try to implement this code before looking at the solution below.

# In[13]:


#### YOUR CODE HERE


# ### Grocery shopping: a solution

# In[14]:


costs = [5, 8, 4, 10, 15]
final_bill = 0
for item in costs:
    if item <= 9:
        final_bill += item
print(final_bill)


# ## Controlling `for` loops
# 
# Sometimes, you may want an even finer degree of control over `for` loops. There are two commands that give you this control:
# 
# 1. `continue`: tells the `for` loop to **continue** onto the next item in the list (i.e., without necessarily doing anything with the current item). 
# 2. `break`: **cancels/stops** the `for` loop.

# ### `break` in action
# 
# The following code iterates through a `range`, and `break`s once it gets to `5`.

# In[15]:


for num in range(1, 10):
    if num == 5:
        break
    print(num)


# ### `continue` in action
# 
# The following code iterates through a `range`, and `continue`s once it gets to `5` (i.e., "skips").

# In[16]:


for num in range(1, 10):
    if num == 5:
        continue
    print(num)


# ### Check-in
# 
# How are `break` and `continue` different?

# ## Nested `for` loops
# 
# Just as we can **nest** conditional statements, we can also nest **loops**.  
# 
# > A **nested loop** is a `for` or `while` loop contained *within* another `for` or `while` loop.
# 
# As with nested `if` statements, it's very important to **be careful about your indentation**.

# ### Nested loops in action (pt. 1)

# In[17]:


professors = ['Trott', 'Ellis', 'Fleischer']
classes = ['COGS 18', 'CSS 1']
for cl in classes:
    for prof in professors:
        print("Is {cl} taught by {prof}?".format(cl = cl, prof = prof))


# ### Nested loops in action (pt. 2)
# 
# **Note**: The `end = " "` parameter in the `print` function just tells Python not to print the `str` on a new line.

# In[18]:


for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print(" ")


# ### A note of caution
# 
# - Nested `for` loops can take a very long to execute if:
#    - Your `list`s are very long.  
#    - You have many, many levels of nesting.  
# - Technically, the code in a nested for loop will run $N * M$ times, where $N$ is the length of the **outer loop**, and $M$ is the length of the **inner loop**.  
#    - This is beyond this course, but [making programs more efficient is an important part of Computer Science](https://en.wikipedia.org/wiki/Big_O_notation).  

# ## Some final (challenging) practice

# ### Practice 1
# 
# Write a `for` loop to count the number of **vowels** in a string. The code block below starts with a `list` of vowels alreay, which you can use to cross-reference when iterating through a string.
# 
# **Hint**: If you're feeling extra ambitious, you might think about how to handle *upper-case* vowels.

# In[19]:


vowels = ['a', 'e', 'i', 'o', 'u']
example_string = "CSS is great"
### Your code here


# ### Practice 2
# 
# Write a `for` loop that:
# 
# - Iterates through a `list` of numbers.  
# - `if` the number (e.g., `i`) is **even**, iterates through a **nested** `for` loop of all those same numbers, and...
#    - `if` a given number is **odd** `and` larger than `i`, `print`s out the sum of those numbers.
#    
# **Hint**: Remember that `%` can be used to figure out whether a given number is divisible by 2 (e.g., `4 % 2 == 0`). 

# In[20]:


### Your code here


# ### Answers to practice problems

# In[21]:


### Practice 1
vowels = ['a', 'e', 'i', 'o', 'u']
example_string = "CSS is great"
num_vowels = 0
for l in example_string:
    if l.lower() in vowels:
        num_vowels += 1
print(str(num_vowels) + " vowels in '{x}'".format(x = example_string))


# In[22]:


### Practice 2
numbers = range(1, 10)
for num in numbers:
    if num % 2 == 0:
        for num2 in numbers:
            if num2 % 2 == 1 and num2 > num:
                print("{x} + {y} = {z}".format(x = num,
                                               y = num2,
                                               z = num + num2))


# ## Conclusion
# 
# That was a (hopefully somewhat gentle) introduction to `for` loops. If you're feeling like you want more practice:
# 
# - This week's lab will contain many more examples.  
# - [W3 schools](https://www.w3schools.com/python/python_for_loops.asp), as always, has some good practice problems.
# 
# Next lecture we'll cover a *new* kind of loop: a `while` loop.

# In[ ]:




