
text_name =""  #insert file path of the text
with open(text_name, 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)

import re
tokenized_list = re.split(" |'|\n", text)
list(tokenized_list)
while '' in tokenized_list:
    tokenized_list.remove('')
    
list(tokenized_list)
print(tokenized_list)

unigrams = []

for token in tokenized_list:
    token = token.lower() 
    token = token.replace('.', '')
    token = token.replace('!', '')
    token = token.replace('?', '')
    token = token.replace(',', '')
    token = token.replace(':', '')
    token = token.replace(';', '')
    token = token.replace('(', '')
    token = token.replace(')', '')
    
    unigrams.append(token)

list(unigrams)

print(unigrams)

from collections import Counter
word_counts = Counter(unigrams)
print(word_counts)
word_counts.most_common(50)
for gram, count in word_counts.most_common(50):
    print(gram.ljust(20), count)
import pandas as pd
import os
stop_words = []
stopwords_list_filename = '' #insert file path of the list

if os.path.exists(stopwords_list_filename):
    import csv
    with open(stopwords_list_filename, 'r') as f:
        stop_words = list(csv.reader(f))[0]
    print('Custom stopwords list loaded from CSV')
else:
    from nltk.corpus import stopwords
    stop_words = stopwords.words('italian')
    print('NLTK stopwords list loaded')
list(stop_words)
for gram, count in word_counts.items():
    clean_gram = gram.lower()
    if clean_gram in stop_words:
        continue
    print(clean_gram)
word_frequency = Counter()
word_frequency = Counter()

for gram, count in word_counts.items():
        clean_gram = gram.lower()
        if clean_gram in stop_words:
            continue   
        if not clean_gram.isalpha():
            continue
        if len(clean_gram) < 2:
            continue
        word_frequency[clean_gram] += count
print(word_frequency)
for gram, count in word_frequency.most_common(100):
    print(gram.ljust(20), count)

file_name = text_name.rsplit('/', 1)[-1]
file_name = file_name.split('.')[0]

import csv
w = csv.writer(open((""+"unigrams_count_"+file_name+".csv"), "w")) ## in the quotation marks insert the path of the output folder
for key, val in word_frequency.items():
    w.writerow([key, val])
    
          
from wordcloud import WordCloud
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image
cloud_mask = np.array(Image.open('')) ## in the quotation marks insert the path of cloud image
cloud_mask = np.where(cloud_mask > 3, 255, cloud_mask)
wordcloud = WordCloud(
    width = 800,
    height = 600,
    background_color = "white",
    colormap = 'viridis',
    max_words = 150,
    min_font_size = 4,
    
    contour_color = 'blue',
    mask = cloud_mask,
    contour_width = 1
).generate_from_frequencies(word_frequency)

mpl.rcParams['figure.figsize'] = (20,20)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
