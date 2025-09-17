#!/usr/bin/env python
# coding: utf-8

# # Working with Text Files

# ## Goals of this lecture
# 
# In programming––*especially* for CSS––it's quite common that you'll need to **read** and **write** files.
# 
# This lecture will cover the basics of that process.
# 
# - The **why**: why would we want to read in a *file*?
# - The **what**: what is a file? Where is it stored? What is a **filepath**? 
# - The **how**: how do you *read* in a file? How do you *write* a file?
# 
# This lecture will focus specifically on **text files**, though there are a number of file types (`.json`, `.csv`, etc.).

# ## Why read and write files?
# 
# Fundamentally, a **file** is just a way to store **data**.
# 
# This data could take many forms:
# 
# - Unstructured text.  
# - [JSON](https://www.json.org/json-en.html), i.e., a kind of `dict`.  
# - `.csv`, i.e., like an Excel file.  
# - An executable file, like a Python script (`.py`). 
# 
# **Computational Social Science** centers around working with data. Thus, it's important to understand how to read and write these files.

# ### Some common use cases
# 
# In CSS research, reading and writing files is pretty much *unavoidable*. It happens almost anytime you want to work with data.
# 
# Examples:
# 
# - Reading in a [text corpus](https://en.wikipedia.org/wiki/Text_corpus) of Tweets on a particular topic to perform **sentiment analysis**. 
# - Reading in a corpus of [song lyrics](https://pudding.cool/2017/02/vocabulary/) to perform analyses about vocabulary, rhythm, and more.
# - Reading in [tabular data](https://www.statology.org/tabular-data/#:~:text=In%20statistics%2C%20tabular%20data%20refers,represent%20attributes%20for%20those%20observations.) about Economics to correlate `Economic Connectedness` with `Social Mobility`.  

# ## So what is a file?
# 
# > A **file** is a set of *bytes* used to store some kind of data.
# 
# The **format** of this data depends on what you're using it for, but at some level, it is translated into *binary bits* (`1`s and `0`s). 
# 
# The file format is usually specified in the **file extension**.  
# 
# - `.csv`: comma separated values.  
# - `.txt`: a plain text file.  
# - `.py`: an executable Python file.  
# - `.png`: a portable network graphic file (i.e., an image).

# ### Where are files?
# 
# Files are **stored** somewhere on your computer (or in a server, etc.), typically in a folder (also called a **directory**). Thus, each file has its own **location**
# 
# - We call this **location** of a file its **path**.  
# - File paths can be either **absolute** or **relative**.

# ### Absolute file paths
# 
# An **absolute** file path specifies the location of a file relative to some **root** directory.
# 
# - On my computer, the root might be: `/Users/sttrott/...`
# - If a file is called `my_file.txt`, the absolute file path would include *every directory* leading up to that file, starting from the root.
# - On Mac/Linux, each directory/folder is separated by the the `/` notation.
# - On Windows, they are separated by the `\` notation.
# 
# Example: `Users/sttrott/CSS/css1/my_file.txt`

# ### Relative file paths
# 
# A **relative** file path specifies the location of a file relative to the **current** directory (i.e., the one you're in right now). 
# 
# - For example, say our current directory is `css1`. 
# - If a file is called `my_file.txt`, the relative file path would tell the computer how to get to `my_file.txt` from `css`.
# - On Mac/Linux, each directory/folder is separated by the the `/` notation.
# - On Windows, they are separated by the `\` notation.
# 
# Example: `css1/my_file.txt`

# #### The `..` syntax
# 
# If your target file (e.g., `my_file.txt`) is not stored within your current directory, you'll need to use the `..` syntax.
# 
# - This tells your computer to "go up a level".
# 
# For example, if we're currently in `css1/lectures/week6`, but we want to get to `css1/my_file.txt`, we'll need to use this notation:
# 
# `../../my_file.txt`.
# 

# ### Check-in
# 
# Suppose we want to access a file called `notes.txt`. This is the absolute path leading to that file:
# 
# `/Users/sttrott/css/lectures`
# 
# How would we write the full **absolute path**, including the file name?
# 

# In[1]:


### Your response here


# #### Solution
# 
# Suppose we want to access a file called `notes.txt`. This is the absolute path leading to that file:
# 
# `/Users/sttrott/css/lectures`
# 
# Absolute path: `/Users/sttrott/css/lectures/notes.txt`

# ### Check-in
# 
# Suppose we want to access a file called `notes.txt`. This is the absolute path leading to that file:
# 
# `/Users/sttrott/css/lectures`
# 
# However, we're currently in the `labs` directory, which is also in the `css` folder.
# 
# How would we write the **relative path** leading from our *current directory* to `lectures/notes.txt`?
# 

# In[2]:


### Your response here


# #### Solution
# 
# Suppose we want to access a file called `notes.txt`. This is the absolute path leading to that file:
# 
# `/Users/sttrott/css/lectures`
# 
# Relative path from `css/labs`: `../lectures/notes.txt`

# ### File paths: wrap-up
# 
# **File paths** can be one of the hardest things to get right.
# 
# - Even as a more experienced programmer, I mess file paths up *all the time* (including for this class!). 
# 
# A helpful command is `pwd`, which reminds us *where we are*: i.e., what our current directory is.

# In[3]:


pwd


# ## The *how*: interacting with files
# 
# Once you've located a file, you probably want to either **read** or **write** it in some way. Both **modes** of interacting with a file will require the `open` keyword.
# 
# In turn, you can `open` a file in one of several **modes**:
# 
# - `w`: writing to that file (i.e., adding text to it).  
# - `r`: reading that file (i.e., reading what's already in it).
# - `a`: appending to what's already in the file. 
# 
# Let's take these step by step.

# ### Writing a file
# 
# The syntax to `open` a file in the **writing mode** is as follows:
# 
# `open("filename.txt", "w")`
# 
# Often, we'll use the `with` keyword as in the codeblock below, which allows us to `open` that filename and assign it immediately to a variable.
# 
# - Then, we can can call `var_name.write("TEXT TO ADD TO FILE")`
# - The advantage of `with` is that it will automatically `close` the file once we're done with the `with` block.

# In[4]:


### Open up a file called `test.txt`
with open("test.txt", "w") as f:
    ### Write string to file
    f.write("This is a file.")


# #### Things to be aware of
# 
# - `filename.txt` doesn't have to exist when you open a file for **writing**. It will be *created* by calling `open(filename.txt).  
# - If `filename.txt` *does* already exist, then by default you'll over-write what's there. If you want to just *add* to the file, use the `a` (**append**) mode instead.
# - To separate lines in this file, use the `\n` character (*newline*). 

# ### Reading a file
# 
# The syntax to `open` a file in the **reading mode** is as follows:
# 
# `open("filename.txt", "r")`
# 
# Once we've opened the file, we can `read` the contents. The `read` function will return the contents as a `str`.

# In[5]:


### Open up a file called `test.txt`
with open("test.txt", "r") as f:
    ### Read the contents
    contents = f.read()


# In[6]:


### print out contents
print(contents)


# ### Check-in
# 
# Use the `open` command to create and write a new file called `my_first_file.txt`. Once you've opened it, **write** a series of lines to that file:
# 
# - The first line should read: `My name is {NAME}\n`.
# - The next 5 lines should read: `This is line {i} of the file.\n`, where `i` refers to the specfiic line number.
# 
# **Hint**: Remember to use the *newline* character to separate each line.

# In[7]:


### Your code here


# #### Solution

# In[8]:


with open("my_first_file.txt", "w") as f:
    f.write("My name is Sean.\n")
    for i in range(0, 4):
        f.write("This is line {i} of the file.\n".format(i = i+2))


# ### Check-in
# 
# Now use the `open` command to open `my_first_file.txt`. Once you've opened it, **read** the contents of that file into a new variable called `file_contents`.

# In[9]:


### Your code here


# #### Solution

# In[10]:


with open("my_first_file.txt", "r") as f:
    file_contents = f.read()


# In[11]:


print(file_contents)


# ### File reading, continued
# 
# Before, we read in the *entire* file as one big `str`. There are several other ways to interact with and **read** a file, however.
# 
# - `.read(n)`, where `n` refers to the number of characters you want to read.  
# - `.readlines()`, which returns a `list` of each *line* in the file.

# #### `.read(n)`
# 
# The `read` function can be **parameterized** by the `n` argument, which tells Python how many characters of the file to read. 

# In[12]:


with open("my_first_file.txt", "r") as f:
    n_characters = f.read(10)
print(n_characters)


# In[13]:


with open("my_first_file.txt", "r") as f:
    n_characters = f.read(15)
print(n_characters)


# #### `.readlines()`
# 
# The `readlines` function returns a `list`, where each element in the list corresponds to a line in the file.
# 
# - *Lines* are defined as being separated by a `\n` character.

# In[14]:


with open("my_first_file.txt", "r") as f:
    all_lines = f.readlines()


# In[15]:


all_lines


# ### Check-in
# 
# - Use the `readlines` function to read in all lines from `my_first_file.txt`. 
# - Then, use a `for` loop to iterate through each line.  
#   - For each line, `replace` the `\n` character with an empty character (i.e., `""`). 
#   - Then, `print` out the line.

# In[16]:


### Your code here


# #### Solution

# In[17]:


with open("my_first_file.txt", "r") as f:
    all_lines = f.readlines()


# In[18]:


for line in all_lines:
    l = line.replace("\n", "")
    print(l)


# ### Appending a file
# 
# If you `open` a pre-existing file in the `w` mode, you can *overwrite* all of its existing content.
# 
# If you wish to simply *add* to that file, you can instead open it in the `a` mode: `open("filename.txt", "a")`

# In[19]:


## Open in append mode
with open("my_first_file.txt", "a") as f:
    ## Syntax to write is the same.
    f.write("This is new text I'm adding.")


# In[20]:


## Now let's check if it worked...
with open("my_first_file.txt", "r") as f:
    file_contents = f.read()
print(file_contents)


# ### Closing a file
# 
# Technically, it is good practice to always `close` a file once you've opened it. 
# 
# - If you're using the `with` keyword, it'll automatically `close` the file once you finish the `with` block.  
# - But if you're not, you can `close` a file using `var_name.close()`.
# 
# 

# ## Conclusion
# 
# There's lots more to working with files (including text files), but this sets the **foundation**. Now you should feel a little more comfortable:
# 
# - Understanding how to navigate your computer's **directory structure**.  
#   - E.g., knowing "where" a file is located.
# - Knowing how to `open` a file in Python.
# - Knowing how to **read** or **write** that file.
# 
# This will form the basis of working with future file types, such as `.csv` (a very common format for representing tabular data).
