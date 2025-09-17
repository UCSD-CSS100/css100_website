#!/usr/bin/env python
# coding: utf-8

# # Loops (continued)

# ## Announcements
# 
# - Problem set 1 due today!
# - Reminder: when modifying labs/problem sets, make sure not to **delete** or **modify** any of the test cells (or rename the assignment), as that can affect the auto-grader.

# ## Goals of this lecture
# 
# - **Loops**, revisited.  
# - `while` loops in Python.

# ## Loops, revisited
# 
# > A **loop** is a way to repeat the same piece of code multiple times.
# 
# Last lecture, we discussed `for` loops, in which the same code is run `for` each element of a sequence.
# 
# - `for` element in `list` or `str`...  
# - ...do "X" (where "X" = the code you want to run).

# ### `for` loops in action
# 
# A `for` loop can be run with any **sequence**.

# Here, we see a `for` loop used with a `list`.

# In[1]:


simple_list = [1, 2, 3]
for item in simple_list:
    print(item)


# Here, we see a `for` loop used with a `str`.

# In[2]:


simple_str = 'css'
for ch in simple_str:
    print(ch)


# ### Check-in
# 
# Write a `for` loop that iterates through a `range(10)`, printing each element along the way, but stops once it reaches `5`. 

# In[3]:


### Your code here


# ### Other important features
# 
# - `for` loops can be combined with **conditional statements**. 
# - `for` loops can be **nested**.  
# - Keywords like `continue` and `break` can give further control over `for` loops.

# ## `while` loops
# 
# > A `while` loop is a procedure to repeat the same piece of code `while` some condition is met.
# 
# For example:
# 
# - Add numbers to a `shopping_bill` variable `while shopping_bill < 50`.  
# - Increase a `temperature` variable `while temperature < 85`.  
# - `while` some condition is met, continue running a **simulation**. 

# ### Check-in
# 
# How are `for` and `while` loops similar? How are they different?

# ### `while` loops in action
# 
# A `while` loop is created using the `while` keyword, following by a **condition**. As long as this condition is met, the `while` loop will continue!  
# 
# In the code below:
# 
# - The `start` variable begins at `0`.  
# - We then declare a `while` loop, which will run as long as `start < 2`.  
# - Then, the `start` variable is incremented by `1` with each **iteration**, guaranteeing that eventually we'll reach the condition where `start >= 2` (thus "breaking" the loop).

# In[4]:


start = 0
while start < 2: ### Conditional statement
    print(start)
    start += 1


# ### Iterating through a `list`
# 
# `while` loops are often used to iterate through a `list`. 
# 
# To do this, we use an **index** variable, which simply keeps track of "where" in the list we are.
# 
# - Recall that we can **index** into a `list` using the syntax `list_name[0]`. 
# - We can also retrieve the **length** of that `list` using `len(list_name)`.  

# In[5]:


numbers = [1, 2, 3] ## List to iterate through
index = 0 ## Start index at 0
while index < len(numbers):
    print("Index: {i}. Number: {n}.".format(i = index, n = numbers[index]))
    index += 1


# ### Check-in
# 
# You want to keep your grocery costs low, so you decide not to buy anything above 9. How would you write a `while` loop that:
# 
# - Iterates through `costs`.  
# - Tracks a `final_bill` variable.  
# - Only adds items to `final_bill` if they're below 9$?
# 
# **Hints**:
# 
# - You can retrieve the *length* of a list using `len(list_name)`.  
# - If you're using an *index*, remember to **increment** it so you don't get stuck in a loop.

# In[6]:


costs = [5, 8, 4, 10, 15]
#### YOUR CODE HERE


# ### Solution

# In[7]:


index = 0
final_bill = 0
while index < len(costs):
    if costs[index] < 9:
        final_bill += costs[index]
    index += 1
print(final_bill)


# ### Stuck in a loop?
# 
# A common issue that programmers encounter is getting "stuck" in an **infinite** `while` loop. This happens because they haven't ensured that the **condition** will eventually evaluate as `False`.  
# 
# - This is surprisingly easy to do, even as an experienced programmer.  
# - For this reason, I typically prefer to use a `for` loop rather than a `while` loop, unless I absolutely have to.
# 
# If you **do** find yourself stuck, you can "cancel" the loop manually:
# 
# - Pressing the **Stop** button in the Jupyter toolbar. 
# - Pressing `Command + C` in the Terminal.  

# ### Check-in
# 
# What will the final value of `room_temperature` be if the following `while` loop is run? What about the final value of `body_temperature`?

# In[8]:


room_temperature = 40
body_temperature = 92
while room_temperature < 70:
    room_temperature += 1
    body_temperature += .2


# ### Check-in
# 
# Write a `while` loop to count the number of **vowels** in a string. The code block below starts with a `list` of vowels alreay, which you can use to cross-reference when iterating through a string.
# 
# **Hint**: If you're feeling extra ambitious, you might think about how to handle *upper-case* vowels.

# In[9]:


vowels = ['a', 'e', 'i', 'o', 'u']
example_string = "CSS is great"
### Your code here


# ### Solution

# In[10]:


### Practice 1
vowels = ['a', 'e', 'i', 'o', 'u']
example_string = "CSS is great"
num_vowels = 0
index = 0
while index < len(example_string):
    if example_string[index].lower() in vowels:
        num_vowels += 1
    index += 1
print(str(num_vowels) + " vowels in '{x}'".format(x = example_string))


# ## Conclusion
# 
# This concludes our unit on **loops**! We'll continue using both `for` and `while` **loops** throughout the course. 
# 
# Key takeaways:
# 
# - A **loop** can be used to repeat the same piece of code many times.  
# - A `for` loop **iterates** through a sequence and does the same thing for each item in that sequence.  
# - A `while` loop runs the code code as long as some **condition** is met.  
#    - `while` loops sometimes get "stuck", if you're not careful about ensuring this condition will eventually evaluate to `False`.  
