#!/usr/bin/env python
# coding: utf-8

# <img align="left" src="https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/CC_BY.png"><br />
# 
# Created by [Nathan Kelber](http://nkelber.com) for [JSTOR Labs](https://labs.jstor.org/) under [Creative Commons CC BY License](https://creativecommons.org/licenses/by/4.0/)<br />
# For questions/comments/improvements, email nathan.kelber@ithaka.org.<br />
# ____

# # HOW TO TOKENIZE A TEXT AND COUNT UNIGRAMS

# ## Preparing a text for tokenization
# 
# You must have a .txt file which has already been pre-processed. You put the file in a folder in your Python environment and you open the file.

# In[ ]:


#Creating a statement to give a variable name to the file. The file must be indicate as 'folder_name/file_name'
text_name = 'data/apocalisse.txt'


# In[ ]:


# Opening a file in read mode. 
## If the text is too long, it could be better to not print it because there might be crash errors
### If you are using Constellate, the right environment is all inside the folder 'constellate-notebooks'.
with open(text_name, 'r') as f:
    text = f.read()
    print(text)


# In[ ]:


# See the raw string version of our text (i.e. in a sigle line, without tabs, paragraphs etc...)
text


# ## Splitting a text for tokenization
# 
# Now you split the text in unigrams and you create a clean and correct list of unigrams.

# In[ ]:


# Splitting the text string into a list of strings. 
# To choose multiple delimiters (empty spaces and apostrophes), we  use re.split function, but this function don't recognize the /n espace character (so we must add it as delimiters) 
## If you choose a single delimiter (for ex. empty spaces or commas) you can use the most simple .split method:
##tokenized_list = text.split()
##list(tokenized_list)

import re
tokenized_list = re.split(" |'|\n", text)
list(tokenized_list)


# In[ ]:


#Removing the empty items from the list.
#The empty items has been generated using \n as delimiter in the re.split function
#This is the system to remove not only the first but all the empty spaces.
while '' in tokenized_list:
    tokenized_list.remove('')
    
list(tokenized_list)


# In[ ]:


# Cleaning up the tokens
unigrams = []

for token in tokenized_list:
    token = token.lower() # lowercase tokens ## if some cases, the capital letters are a distinctive marks (ex. brown is a color and Brown is a surname), you have to differently rename one of the two cases (ex. brown and name-brown). 
    token = token.replace('.', '') # remove periods
    token = token.replace('!', '') # remove exclamation points
    token = token.replace('?', '') # remove question marks
    token = token.replace(',', '')
    token = token.replace(':', '')
    token = token.replace(';', '')
    token = token.replace('(', '')
    token = token.replace(')', '')
    
    unigrams.append(token)


# In[ ]:


# Preview the unigrams
list(unigrams)


# ## Counting the occurrences of unigrams with a word counter
# 
# Now you count the occurences of the unigrams. In this way you collect the tokens in types.

# In[ ]:


# Import, from a Python Library, the Counter function and count up the tokens using a Counter() object
from collections import Counter
word_counts = Counter(unigrams)
print(word_counts)


# In[ ]:


# Looking to the most common unigrams.
word_counts.most_common(50)


# In[ ]:


# Formatting the most common unigrams visualization
for gram, count in word_counts.most_common(50):
    print(gram.ljust(20), count)


# ## Loading a stop word list and clean the unigrams
# 
# Now you clean the unigram count from function words (articles, prepositions, conjuctions ecc...), from non-alphabethic unigrams and you re count the cleaned unigrams.

# In[ ]:


import pandas as pd
import os


# In[ ]:


# Load a custom stop_words.csv, if available, in a folder of your Python environment
# Otherwise, load the nltk stopwords list in your language (english, italian, ecc..)

# Create an empty Python list to hold the stopwords
stop_words = []

# The filename of the custom data/stop_words.csv file
stopwords_list_filename = 'data/stop_words_italian.csv'

if os.path.exists(stopwords_list_filename):
    import csv
    with open(stopwords_list_filename, 'r') as f:
        stop_words = list(csv.reader(f))[0]
    print('Custom stopwords list loaded from CSV')
else:
    # Load the NLTK stopwords list. You can choose a different language
    from nltk.corpus import stopwords
    stop_words = stopwords.words('italian')
    print('NLTK stopwords list loaded')


# In[ ]:


# Preview stop words
list(stop_words)


# In[ ]:


for gram, count in word_counts.items():
    clean_gram = gram.lower()
    if clean_gram in stop_words:
        continue
    print(clean_gram)


# In[ ]:


#removing from our previous unigram counts (word_counts): the loaded stop_words, the token that aren't composed only by alphabetic letters and the too short token. 

##assigning the name 'word_frequency' to the Counter function. This statement will be useful for creating a new list
word_frequency = Counter()

for gram, count in word_counts.items():
        clean_gram = gram.lower()  # from our previous unigrams count, you consider only unigrams in lower case (without count)
        if clean_gram in stop_words:
            continue               # if this condition is True (unigram = stop word), the unigram remain in the loop and it doesn't pass over             
        if not clean_gram.isalpha():
            continue                # if this condition is True (unigram with not only alphabetic letters), the unigram remain in the loop and it doesn't pass over
        if len(clean_gram) < 2:
            continue              # if this condition is True (unigram <2), the unigram remain in the loop and it doesn't pass over
        word_frequency[clean_gram] += count #every unigram that is pass over is considered and added up to the count


# In[ ]:


print(word_frequency)


# In[ ]:


for gram, count in word_frequency.most_common(100):
    print(gram.ljust(20), count)


# ## Asking for a single unigram count

# In[ ]:


# example with the word 'vino' 
word_frequency.get('vino','not found word')


# ## Creating a word cloud
# 
# We create a word cloud based on the word count.

# In[ ]:


# Add wordcloud
from wordcloud import WordCloud
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image


# In[ ]:


### Download cloud image for our word cloud shape
import urllib.request
download_url = 'https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/sample_cloud.png'
urllib.request.urlretrieve(download_url, './data/sample_cloud.png')


# In[ ]:


# Create a wordcloud from our data

# Adding a mask shape of a cloud to your word cloud
# By default, the shape will be a rectangle
# You can specify any shape you like based on an image file
cloud_mask = np.array(Image.open('./data/sample_cloud.png')) # Specifies the location of the mask shape
cloud_mask = np.where(cloud_mask > 3, 255, cloud_mask) # this line will take all values greater than 3 and make them 255 (white)

### Specify word cloud details
wordcloud = WordCloud(
    width = 800, # Change the pixel width of the image if blurry
    height = 600, # Change the pixel height of the image if blurry
    background_color = "white", # Change the background color
    colormap = 'viridis', # The colors of the words, see https://matplotlib.org/stable/tutorials/colors/colormaps.html
    max_words = 150, # Change the max number of words shown
    min_font_size = 4, # Do not show small text
    
    # Add a shape and outline (known as a mask) to your wordcloud
    contour_color = 'blue', # The outline color of your mask shape
    mask = cloud_mask, # 
    contour_width = 1
).generate_from_frequencies(word_frequency)

mpl.rcParams['figure.figsize'] = (20,20) # Change the image size displayed
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

