#!/usr/bin/env python
# coding: utf-8

# # Working with Text Files (pt. 2)

# ## Goals of this lecture
# 
# In the previous lecture, we discussed the basics of `open`ing a `.txt` file, as well as **reading** and **writing** to that file.
# 
# In this lecture, we'll talk about what you can do with a text file once you've already opened it. Because text files are `read` in as strings, you'll see many echoes of our previous lecture on [working with strings](strings).
# 
# - **Finding** a target `str` in a file.  
# - **Counting** the number of words in a file.  
#   - **Counting** how many times *each word* occurs.
#   - Finding the most **frequent** word in a text.

# ## Finding a target `str`
# 
# One common use case is **searching** a large volume of text to `return` particular sub-string.
# 
# - Where in the text does this sub-string occur?  
# - What is the text surrounding one of its occurrences?
# 
# Note that this is not too far afield from a **search engine** like [Google](https://www.google.com/)!

# ### Our sample text
# 
# To start, we'll use a `.txt` file of [**Hamlet**](https://en.wikipedia.org/wiki/Hamlet), by [William Shakespeare](https://en.wikipedia.org/wiki/William_Shakespeare). The `.txt` file was retrieved from the [Project Gutenberg Corpus](https://www.gutenberg.org/browse/scores/top) online, and should be credited as such. 
# 
# The file is included in the `lectures` GitHub repository under the `data` directory.
# 
# First, let's use `readlines()` to extract each **line** of the play as a separate item in a list.

# In[1]:


with open("data/hamlet.txt") as f:
    book = f.readlines()


# #### Inspecting the text

# In[2]:


## This is just the title
book[0]


# In[3]:


## Partial list of characters in play
for line in book[5:12]:
    l = line.replace("\n", "")
    print(l)


# #### Check-in
# 
# How could we check how many **lines** are in the `.txt` file?

# In[4]:


### Your code here


# #### Solution

# In[5]:


### Number of entries in list
len(book)


# ### Finding a sample `str`
# 
# One of the most famous lines in *Hamlet* reads:
# 
# > To be, or not to be- that is the question...
# 
# Suppose we wanted to **find** the `str` `"that is the question"` in the book, and **return** the line number (at least in this `.txt` file).
# 
# How could we go about that?

# ### Solution: `enumerate`
# 
# - Use `enumerate` to iterate through each line of the play.  
# - For each line, check if some `target_str` occurs in that line.  
# - If it does, use `break` to **stop** iterating, and record which line it is.

# In[6]:


target_str = "that is the question"
for index, line in enumerate(book):
    if target_str in line:
        break
print("Line: {x}".format(x = line.replace("\n", "")))
print("Line number: {x}".format(x = index))


# ### Check-in: Finding the next $N$ lines
# 
# What if we wanted to return the next $N$ (e.g., `5`) lines *after* this target string? 
# 
# - To do this, we just need to add another variable: `keep_lines`, which tells us *how many* additional lines we want to return.  
# - Then, once we've retrieved the `index` of our `target_str`, we can **slice** between that `index` and `index + 3`.
# 
# Try implementing this algorithm yourself first. 
# 
# **Hint**: The code can be *mostly* the same as before (i.e., use `enumerate`, etc.). 

# In[7]:


### Your code here


# ### Solution

# In[8]:


target_str = "that is the question"
keep_lines = 5 ### New variable to track
for index, line in enumerate(book):
    if target_str in line:
        break


# In[9]:


# Retrieve all lines between target and 3 lines later
targets = book[index: index+ keep_lines]
## Now, print out each of those lines
for i in targets:
    print(i.replace("\n",""))


# ### Check-in: What if `target_str` occurs multiple times?
# 
# What if we were looking for a more common `target_str`, e.g., one that occurred multiple times?  
# 
# 1. What problems do you see with our previous approach (e.g., using `break` once we find `target_str`)?
# 2. How might you solve this problem? 

# In[10]:


### Your answer here


# ### Solution
# 
# **Problem**: If we `break` *as soon as* we find the `target_str`, we'll always only ever find the first instance.
# 
# **Solution**: Instead, we can **track** the indices of each occurrence of `target_str`. Then, we `return` a `list` of these indices when we finish checking the entire book.

# In[11]:


target_str = "the question"
## Track a list of indices
line_indices = []
for index, line in enumerate(book):
    if target_str in line:
        ## Rather than breaking, we 
        ## add index to list_indices
        line_indices.append(index)


# #### Checking `line_indices`

# In[12]:


print(line_indices)


# In[13]:


for l in line_indices:
    line = book[l].replace("\n", "")
    print("Line {x}: {y}".format(x = l, y = line))


# ### Check-in: Other considerations
# 
# These exercises really only scratch the surface of **searching** a file. Here are some other issues for consideration and discussion. 
# 
# How might you address:
# 
# 1. Issues of **case**: e.g., what if *question* is spelled `"Question"`, not `"question"`?
# 2. Situations where a `target_str` spans multiple *lines*? 
# 3. Mismatch in punctuation, e.g., a misplaced `,`? 
# 4. A **partial match**, e.g., if $90\%$ of the characters match?
# 
# **Note**: These are challenging issues! And each of them likely has multiple solutions.

# In[14]:


### Discussion


# ## Counting Words
# 
# Another very common **use case** is simply **counting** words.
# 
# - How many words are there overall?  
# - How many *unique words* are used?  
# - How many times does *each word* occur?  
# - What is the *most frequent word*?

# ### Caveat: what *is* a word?
# 
# The question of what defines a word is surprisingly complex.
# 
# - First, languages have very different [**morphological systems**](https://en.wikipedia.org/wiki/Morphological_typology). So even *conceptually*, it's not always clear what makes a word "a word" in a given language.  
# - Second, languages have very different [**writing systems**](https://en.wikipedia.org/wiki/Orthography). 
#   - Some languages (like English, Spanish, etc.) have *spaces* between words in their written form.  
#   - Other languages (like Classical Latin, Chinese, etc.) do [not typically use *spaces* between words](https://en.wikipedia.org/wiki/Scriptio_continua) in their written form.
# 
# Many **conceptual definitions** and **tools** for identifying *words* are rooted in English specifically, but those definitions and tools don't always generalize––languages can be very different.

# #### NLP is (historically) English-centric
# 
# Historically, work in [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing) has been quite English-centric. 
# 
# - Often, English was seen as the "default language"––to such a degree that researchers didn't always mention that they were working on English specifically!
# - However, this is starting to change.
#   - Researchers like [Emily Bender](https://faculty.washington.edu/ebender/) have pushed scholars to [**name the language they're working on**](https://thegradient.pub/the-benderrule-on-naming-the-languages-we-study-and-why-it-matters/).  
#   - [Word segmentation](https://en.wikipedia.org/wiki/Text_segmentation) is increasingly recognized as an important problem.  
# 
# This will be important to keep in mind as we discuss **identifying** and **counting** words in written English text.

# ### How *many* words?
# 
# The first question that might occur to us is *how many words* are in a book. 
# 
# To do this, we could:
# 
# - `read` the book in as one long `str`.  
# - Use the `split` function to separate this long `str` by **spaces**, into a `list` of words.
# - Count the number of items in this list.

# #### Using `split`: a review

# In[15]:


sentence = "To be or not to be, that is the question"
sentence.split(" ")


# #### Using `split` for Hamlet

# In[16]:


# First, read in as string
with open("data/hamlet.txt", "r") as f:
    book_str = f.read()


# In[17]:


# We should also clean up all those *newline* characters.
book_str = book_str.replace("\n", " ")
# To make it easier for later, we can also turn it into lowercase
book_str = book_str.lower()
# Now, use split to separate into words
book_words = book_str.split()
book_words[0:5]


# In[18]:


# How many items in list?
len(book_words)


# ### How many *unique* words?
# 
# Above, we calculated how many word *tokens* were in the book. 
# 
# - This means that the word "the" will be counted *every time* it occurs.  
# - Instead, let's calculate the number of *unique* word types.

# #### Using `set`
# 
# The `set` function will turn a `list` into a `set` object, which contains only the *unique elements* in that list.

# In[19]:


my_list = ["the", "dog", "is", "the", "best"]
set(my_list)


# #### Check-in
# 
# Use the `set` function to calculate how many *unique* words are in this book.

# In[20]:


### Your code here


# #### Solution
# 
# We already have the `book_words` list, so we can just convert this to a `set`.

# In[21]:


words_set = set(book_words)
len(words_set)


# ### How many times does each word occur?
# 
# We might also want to know *how many times* each word occurs. 
# 
# - For example, perhaps "the" occurs $>1000$ times, whereas "question" occurs only ~$10$ times.  
# - Ideally, we would store this in a `dict`:
#    - Each **key** represents a *word*.  
#    - Each **value** represents *how many times* that word occurred in *Hamlet*.
# 
# How might we go about this?

# #### First pass: counting each word
# 
# As a first pass, let's use the following approach:
# 
# - First, create a `dict` to store our words.  
# - Then, *iterate* through our `list` of words.  
# - `if` a given word is not in our `dict`, add an entry for it (and set the value to `1`).  
# - `if` a given word *is* in a `dict`, increase its value by `1`.

# In[22]:


word_counts = {}
for w in book_words:
    if w not in word_counts:
        word_counts[w] = 1
    else:
        word_counts[w] += 1


# In[23]:


# How many times does "the" occur?
word_counts['the']


# In[24]:


# How many times does "king" occur?
word_counts['king']


# #### Check-in
# 
# Any issues with this **first pass** approach? 
# 
# **Hint**: One issue could have to do with punctuation...

# In[25]:


### Your code here


# #### Solution
# 
# One problem that you might've noticed is that words occurring at the *end of a sentence* don't have a space between the word and a period (e.g., `question.`). 
# 
# - This will *under-count* certain words.
# 
# To resolve this, we can `replace` all periods with an empty character before adding a word to our `dict`.

# In[26]:


word_counts = {}
for w in book_words:
    w_no_period = w.replace(".", "")
    if w_no_period not in word_counts:
        word_counts[w_no_period] = 1
    else:
        word_counts[w_no_period] += 1


# In[27]:


# How many times does "king" occur?
word_counts['king']


# ### Which word is most common?
# 
# Now that we have a `dict` representing how many times each word occurs, we can calculate **which word** is most common.
# 
# **Check-in**: Which word do you think is most frequent in *Hamlet*?

# #### Finding the most frequent word
# 
# As always, there are multiple ways to do this.
# 
# But one simple approach is to:
# 
# - Use a `for` loop to iterate through all `items()` in the `dict`.  
# - Track the `key_with_highest_value` we've seen so far.  
# - Once the `for` loop is done, inspect `key_with_highest_value`.

# In[28]:


key_with_highest_value = None
max_count = 0
for word, count in word_counts.items():
    # If this word frequency > max_count
    if count > max_count:
        # Set new "highest word" to this word
        key_with_highest_value = word
        max_count = count


# In[29]:


## Now, inspect which word was most frequent
key_with_highest_value


# #### Other approaches
# 
# There are *many different approaches* you could take to solving this problem. Some are more generalizable (but also more complicated) than what I've shown here.
# 
# - You can `sort` the dictionary by **value** (see the lecture on [advanced dictionary operations](13-dictionaries-advanced)).  
# - You could use the `max` function with `dict.get` as your `key` parameter (see below).

# In[30]:


# Another approach
max(word_counts, key = word_counts.get)


# ## Conclusion
# 
# This concludes our brief introduction to *working with text files*.
# 
# - The material in this lecture is a pre-cursor to basic Natural Language Processing techniques.  
# - The material in the [previous lecture](17-reading-text) covers the basics of **interacting with files** (`open`ing a file, using `read` and `write`, etc.). 

# In[ ]:




