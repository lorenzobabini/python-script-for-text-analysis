text_name ="" #insert the file path of your .txt
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

unigrams_list = []

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
    token = token.replace('"', '')
    
    unigrams_list.append(token)

print(unigrams_list)

import nltk
from nltk.tokenize import TreebankWordTokenizer

bigrams = list(nltk.bigrams(unigrams_list))
trigrams = list(nltk.trigrams(unigrams_list))

print('Bigrams: \n ', bigrams, '\n')
    
print('Trigrams: \n,', trigrams)

from collections import Counter

def convert_tuple_bigrams(tuples_to_convert):
    """Converts NLTK tuples into bigram strings"""
    string_grams = []
    for tuple_grams in tuples_to_convert:
        first_word = tuple_grams[0]
        second_word = tuple_grams[1]
        gram_string = f'{first_word} {second_word}'
        string_grams.append(gram_string)
    return string_grams

def convert_tuple_trigrams(tuples_to_convert):
    """Converts NLTK tuples into trigram strings"""
    string_grams = []
    for tuple_grams in tuples_to_convert:
        first_word = tuple_grams[0]
        second_word = tuple_grams[1]
        third_word = tuple_grams[2]
        gram_string = f'{first_word} {second_word} {third_word}'
        string_grams.append(gram_string)
    return string_grams

def convert_strings_to_counts(string_grams):
    """Converts a Counter of n-grams into a dictionary"""
    counter_of_grams = Counter(string_grams)
    dict_of_grams = dict(counter_of_grams)
    return dict_of_grams

string_bigrams = convert_tuple_bigrams(bigrams)
bigramCount = convert_strings_to_counts(string_bigrams)


string_trigrams = convert_tuple_trigrams(trigrams)
trigramCount = convert_strings_to_counts(string_trigrams)


sort_bigramCount = sorted(bigramCount.items(), key=lambda x: x[1], reverse=True)


file_name = text_name.rsplit('/', 1)[-1]
file_name = file_name.split('.')[0]

import csv
w = csv.writer(open((""+"bigrams_count_"+file_name+".csv"), "w")) #in the quotation marks, insert the output folder
for i in sort_bigramCount:
    w.writerow([i[0], i[1]])


sort_trigramCount = sorted(trigramCount.items(), key=lambda x: x[1], reverse=True)


w = csv.writer(open((""+"trigrams_count_"+file_name+".csv"), "w"))   #in the quotation marks, insert the output folder
for i in sort_trigramCount:
    w.writerow([i[0], i[1]])
