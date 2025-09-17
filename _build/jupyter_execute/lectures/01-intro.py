#!/usr/bin/env python
# coding: utf-8

# # Welcome to CSS 2

# ## Goals of this lecture
# 
# - Quick introductions/logistics.
# - Introduction to CSS: What is it and why does it matter?
#   - If you took CSS 1 last quarter, some of this will be familiar.
# - Overview of course content.

# ## Course Logistics: CSS 2
# 
# **Teaching Team**:
# 
# - [Sean Trott](https://seantrott.github.io/): Assistant Teaching Professor in Cognitive Science and CSS.
# - TAs:
# 
# 
# **When/Where?**:
# - Lecture: MWF 2-3 AM, HSS 1330 (also podcasted).  
#    
# [**Course Website**](https://ucsd-css2.github.io/ucsd-css2-website/intro.html).
# 
# - Contains web versions of each lecture.  
# - Also contains syllabus and schedule. 
# 

# ## What is CSS?
# 
# In a nutshell, [Computational Social Science](https://en.wikipedia.org/wiki/Computational_social_science) focuses on **computational approaches** to **social science**.
# 
# At UCSD, [Social Sciences](https://socialsciences.ucsd.edu/) encompasses many disciplines:
# 
# - Psychology.  
# - Economics.
# - Political Science.
# - Cognitive Science. 
# - Urban Studies and Planning.  
# 
# And [many more](https://socialsciences.ucsd.edu/about/org-chart.html)!

# ### What is social science?
# 
# **Social Science** refers to a domain of study: social phenomena.  
# 
# - Encompasses many **scales**: human psychology, language, economic behavior, political systems.  
# - Can involve many **approaches**: qualitative interviews, statistical analysis, simulations.  

# ### What is computation?
# 
# [**Computation**](https://en.wikipedia.org/wiki/Computation) is *calculation* using well-defined steps, e.g., an *algorithm*.
# 
# - A *computer* is anything that implements these well-defined steps.  
# - Historically, the term "computer" used to refer to *people*!
# 
# A **programming language** is a way to get a computer to do these things for you.  
# 
# - Can *automate* processes: speed things up!  
# - Can perform computations at *scale*.  
# - Can *share* with others.  

# ## CSS in action: inspirations
# 
# - CSS often involves analysis of **large-scale datasets** using **statistical tools**.
# - Can yield important theoretical and practical **insights**.

# ### Economic mobility
# 
# **N = 22B (Facebook connections)**
# 
# [*Jackson et al. (2022)*](https://www.nature.com/articles/s41586-022-04996-4?campaign_id=9&emc=edit_nn_20220801&instance_id=68142&nl=the-morning&regi_id=180204414&segment_id=100125&te=1&user_id=ee66cc1cf7db7a658ede84f5e390f1ff):
# 
# ![title](img/chetty_2022.png)

# ### The pandemic's effect on missed work in the USA
# 
# [Reference: Full Stack Economics](https://fullstackeconomics.com/18-charts-that-explain-the-american-economy/)
# 
# ![title](img/work_pandemic.png)

# ### Auditing racial discrimination in hiring
# 
# **N = 13,000 (applications)**
# 
# [*Quillian et al. (2020)*](https://academic.oup.com/sf/article/99/2/732/5816667?login=true&casa_token=MLzPTGCAAC4AAAAA:cr3p4XuFqdKEt8TLXYu0KJWJpaigrfsYg1oltxnuUPLhgSTLD8ZI_B3K2-_j0IQhYNpobYaFFsqBHj4)
# 
# ![title](img/discrimination.png)

# ### Moral decision-making across the world
# 
# **N = 70,000 (from 42 countries!)**
# 
# [*Awad et al. (2020)*](https://www.pnas.org/doi/10.1073/pnas.1911517117)
# 
# ![title](img/trolley_problem.png)

# ### Are song lyrics getting more negative over time?
# 
# **N = ~150K songs**
# 
# [*Brand et al. (2019)*](https://www.cambridge.org/core/journals/evolutionary-human-sciences/article/cultural-evolution-of-emotional-expression-in-50-years-of-song-lyrics/E6E64C02BDB0480DB13B8B6BB7DFF598)
# 
# ![title](img/lyrics.png)

# ### How similar are vocabularies across languages?
# 
# **N = 41 languages (1010 concepts)**
# 
# [*Thompson et al. (2020)*](https://www.nature.com/articles/s41562-020-0924-8)
# 
# ![title](img/alignment.png)

# ## Course Structure
# 
# Class time is divided into *lecture* and *section*.
# 
# - Lecture is a time to **introduce**, **explain**, and **demonstrate** new concepts.  
#   - There will be a focus on **hands-on practice** (i.e., "check-ins"). 
# - Section is a time to **practice** and **develop further fluency** with these concepts.  
# 

# ### Following along in lecture
# 
# - Lecture will have many opportunities to **follow along** via **check-ins**.  
# - I do recommend doing this, whether you're in-person or watching the podcast! 
# - The lectures can all be found on GitHub, and downloaded or **cloned** into your DataHub account: 
#    - Link: https://github.com/UCSD-CSS2/lectures
#    - We'll review exactly how to do that in class.

# ### Grading and Assessments
# 
# - Each week (except for final weeks) will have a **coding lab** due the following Monday.
# - There are also **four problem sets**, which will be auto-graded.
# - There is also a **final project**––like a big, more coherent problem set.
# 
# | Grade Component | Percentage of Final Grade |
# | --------------- | ------------------------- |
# | 8 Coding Labs | 50% (6.25% each) |
# | 4 Problem Sets | 32% (8% each) |
# | 1 Final Project| 18% |

# ### Expectations
# 
# - Course will involve programming in Python.  
#   - We will review basics, but expectations include [CSS 1 content](https://ucsd-css2.github.io/ucsd-css2-website/course/expectations.html).  
#   - Lab 1 will be basic Python review!
# - Will also involve using **DataHub** (and Jupyter notebooks).
# - Lecture/section attendance not required.  
# - No midterms or final exam.

# ### Academic Integrity
# 
# From the syllabus:
# 
# > Please turn in your own work. While you are encouraged to work together on some assignments (e.g., on [labs](../labs/overview.md)), you should still understand the code you've submitted. Problem sets and final project should be completed independently.
# 
# > Please review academic integrity policies [here](http://academicintegrity.ucsd.edu). Cheating and plagiarism are unfair to other students and ultimately to yourself, and you will be penalized if caught. Instead, if you're struggling with something, please come to office hours and ask for help! 
# 

# ## Course Content

# ### Key questions
# 
# We'll examine some **key questions** involved in CSS:
# 
# - How is a dataset **formatted**, and is this the appropriate format for what I want to do? 
# - Is this dataset **representative** or does it reflect a **biased sample**? 
# - What **ethical considerations** should I take into account when obtaining and analyzing data? 
# - What kind of **model** is the most appropriate for these data? 
# - How do I **design and implement** these models––ranging in complexity from [linear regression](https://en.wikipedia.org/wiki/Linear_regression) to [support vector machines](https://en.wikipedia.org/wiki/Support_vector_machine)? 

# ### Sample topics
# 
# - Ethical issues in CSS.
# - Data visualization. 
# - Data wrangling.  
# - Linear regression.  
# - Classification.  
# - Model evaluation.  
# 

# ## Welcome to CSS!
