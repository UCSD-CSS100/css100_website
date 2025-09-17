#!/usr/bin/env python
# coding: utf-8

# # 02-Tooling

# ## Addressing Q/A
# 
# **Question**: What is Piazza?
# **Answer**: Piazza is a way to ask questions about course content. In general, we prefer questions over Piazza than email. The course Piazza can be found here: https://piazza.com/class?nid=l88zbj22p6w26z
# 
# **Question**: People are talking about DataHub, labs, etc. I feel a little behind because I don't know what they're referring to.  
# **Answer**: I know it can feel overwhelming, but we're going to start covering those details today. *No labs or assignments have been relased yet, so don't worry that you've missed anything.*
# 
# **Question**: What is DataHub? How do I login?  
# **Answer**: DataHub is a way to use Jupyter notebooks (and more) through UCSD server infrastructure. We'll talk about that more today. You *should* be able to login using your student-sign on (SSO). **Note that if DataHub continues to have issues, we will extend the deadline for the first lab!**
# 
# **Question**: Where will I find assignments?  
# **Answer**: Assignments will be released through DataHub. We have a guide on the website for **fetching** and **submitting assignments** but 
# 
# **Question**: I'm on the waitlist. Can/will I get into the class?  
# **Answer**: I don't have direct control over the waitlist. I've contacted the CSS administration about this and will keep you updated; if you have questions, I recommend contacting CSS staff.

# ## Office Hours
# 
# My office hours will be: 
# 
# - When: Monday, 10-11 AM (after class).
# - Where: CSB courtyard. 
# 
# TA Office hours:
# 
# - Nikolay Kudrin: 4-5pm (Zoom/remote). 
# - (Others updated shortly)

# ## Goals of this lecture
# 
# In this lecture, we'll discuss some of the key **software tools** we'll be using throughout the course.
# 
# - [Python](https://www.python.org/).
# - [Jupyter notebooks](https://jupyter.org/).  
# - [Datahub](http://datahub.ucsd.edu/hub/login).  
# - [Anaconda](https://www.anaconda.com/products/distribution).  

# ## What is tooling, and why is it hard?  
# 
# Often, one of the hardest things about learning programming is **tooling**. 
# 
# - There are tons of new tools you've never used before, and it can seem overwhelming.  
# - Lots of new technical terms: "library", "syntax", "version".
# - So if you *do* feel overwhelmed, you're not alone.  
# 
# This means: **Don't hesitate to ask us for help!**
# 
# 

# ## Tool 1: Python

# ![title](img/python_logo.png)

# ### What is Python?
# 
# - Python is a **programming language**. 
#   - It's a way to "do" computation.  
#   - Each programming language has its own "syntax": how to write commands in that language.
# - Python is also an **ecosystem**.
#   - A particular computational approach with its own community and practices.  
# 

# In[1]:


var_string = "This is a Python string"
print(var_string)


# ### Versions
# 
# - Many different *versions* of Python.  
#   - Main difference between versions is specific syntax (e.g., `print "..."` vs. `print("...")`). 
# - The version on DataHub is **3.9**.
#   - Any version $>3.6$ should work.
# 

# ### Libraries
# 
# - Python also has many different *libraries* you can `import`.  
# - A "library" is a **set of useful tools/functions** that eliminate the need for you to code something from scratch.  
#    - `seaborn` has many functions to make beautiful visualizations.
#    - `numpy` has many functions to work with `arrays`, e.g., calculate the `mean` or `median`.  
# - Some libraries are "native" to Python, and others must be installed.  
# - DataHub should already have the packages we'll need for the course.
# 

# In[2]:


import numpy as np ### Example import statement
np.mean([2, 6, 8, 10]) ### Example function with numpy


# ## Tool 2: Jupyter Notebooks
# 
# [Jupyter notebooks](https://jupyter.org/) are tools to make **interactive code** with a variety of programming languages, including Python.
# 
# - [Official documentation](https://jupyter-notebook.readthedocs.io/en/stable/).  
# - [Example notebooks](https://github.com/jupyter/notebook/tree/main/docs/source/examples/Notebook).  
# 
# Notebooks are also tools for **scientific communication**.

# ### Notebooks are versatile
# 
# - This lecture was written in a Jupyter notebook ([source code here](https://github.com/seantrott/css1_ucsd/blob/main/lectures/02-tooling.ipynb)). 
#    - The same notebook can contain Python code *and* `markdown` code.  
# - The course website was created using an extension of Jupyter notebooks called [`jupyter book`](https://jupyterbook.org/en/stable/intro.html).  
# - The labs, problem sets, and final project will all be distributed and submitted using Jupyter notebooks.

# ### What is a "cell"?
# 
# - Cells are an independent unit in a Jupyter notebook. 
# - A cell can contain Python code, `markdown` text, or another programming language.  
#   - The "type" of cell can be specified accordingly (`markdown`, `Code`, etc.).  
# - Code cells can be **executed** by pressing `Shift` + `Enter/Return`, or by pressing the `Run` button above.

# In[3]:


### This is a code cell; it will produce output.
2 + 2


# This is a `markdown` cell; the same expression will not produce output.
# 
# 2 + 2

# ### What is `markdown`?
# 
# - `markdown` is a way to specify how text is formatted.  
# - Simple examples:
#    - **Bold text** can be created with two asterisks on each side (`**like this**`), or with two undescores (`__like this__`).  
#    - *Italicized text* can be created with one asterisk on each side (`*like this*`), or with one underscore (`_like this_`).  
# - Ultimately, [markdown](https://www.markdownguide.org/) gets turned into [`html`](https://en.wikipedia.org/wiki/HTML), another **markup language**.  
# - Thus, you can create `html` websites (like this one!) using `markdown`.
# 

# ### Check-in
# 
# What would happen if I surrounded text with three asterisks, e.g., `***this is a test***`?

# (If you're following along with Jupyter notebook, modify this cell to check.)

# ### Additional uses of `markdown`
# 
# - `markdown` can also be used to [make links](https://www.markdownguide.org/) using `[text](url)`.
# - Additionally, you can make **lists** in `markdown` (like this one) using `-`.  
#    - These lists can have indented points.  
# - You can change the font size using **headings** (e.g., `#` vs. `##`).

# ### Check-in
# 
# What creates a bigger heading, `#heading 1` vs. `##heading 2`?

# (If you're following along with Jupyter notebook, modify this cell to check.)

# ### Code cells, revisited
# 
# - If you're writing a Python program, you'll want to make sure you're using a **code cell**.  
# - Each code cell can have either very few or very many different lines of code.  
# - Cells can also produce **output**, e.g., by using `print` or simply calling a variable at the end of the cell.

# In[4]:


print("This cell only has one line, plus a comment")


# In[5]:


for word in "This cell has multiple lines".split():
    print(word)


# ### Check-in
# 
# How would you create a cell that outputs the value `200`?

# In[6]:


#### Your code here


# ### Additional functions
# 
# - Code cells have a really useful **auto-complete function**.  
# - As you're typing code, press the `tab` key, and a menu will appear showing possible functions/variables you might be referencing.  

# #### Auto-complete
# 
# - Code cells have a really useful **auto-complete function**.  
# - As you're typing code, press the `tab` key, and a menu will appear showing possible functions/variables you might be referencing.  

# In[7]:


#### If you're following along, try typing something (e.g., np), then press tab. 


# #### Documentation
# 
# - Additionally, you can get information about a particular variable or function by typing `?` before the name of that function.

# In[8]:


#### If you're following along, try uncommenting the following line
### ?print


# ## Tool 3: Datahub
# 
# [Datahub](http://datahub.ucsd.edu/hub/login) is a way to use Jupyter notebooks (and other software) using UCSD **infrastructure**. 
# 
# There are several advantages to this:
# 
# - Everyone uses the same version, so we're all on the same page.  
# - You won't need to install everything yourself, which is sometimes a painful process!  
# - You can access/submit assignments directly through Datahub.

# ### What will you find on Datahub?
# 
# - Course lectures. 
# - Coding labs.  
# - Problem sets.  
# - Final project.

# ### Working on assignments
# 
# - The problem sets and final project will be **auto-graded**.
# - For this to work correctly, it's very important that:  
#   - You don't change any file names.  
#   - You don't delete or remove any cells.  
# - It's fine to add *more* cells (i.e., to answer a question).  

# ### Turning in assignments
# 
# - Make sure you press **submit**.
#    - Otherwise we won't see the updated version you completed!
# - If you have doubts, double-check that your project/lab/etc. shows up under "submitted assignments".  
# - We only have access to your most recent submission.  

# ## Tool 4: Anaconda
# 
# [Anaconda](https://www.anaconda.com/products/distribution) is a **distribution**. This means it includes a *version* of Python, plus a bunch of really useful packages.

# ### Why Anaconda is useful:
# 
# - Features over 8000 open-source data science and machine learning packages (e.g., `pandas`, `seaborn`, etc.).  
# - Auto-installs all these packages: again, installation can be very painful, so Anaconda takes care of all that for you "under the hood".  
#    - Makes sure that installed versions are all compatible, etc.
# - **If you want to work on Python/Jupyter locally (i.e., not on Datahub), Anaconda is one of the easiest ways to get things installed**. 

# # Conclusion
# 
# This concludes the high-level introduction to various **tools**.
# 
# If you're feeling a bit overwhelmed by all the software you haven't encountered before, try not to worry! As we progress through the class, you'll start to feel more comfortable with these tools. And again, if you have questions, please don't hesitate to reach out to the teaching team (or other classmates)!
