text_name =""   #insert file path of the text
with open(text_name, 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)

from spacy.lang.it import Italian
nlp = Italian()

my_doc = nlp(text)

tokens = []
for token in my_doc:
    tokens.append(token.text)

while '' in tokens:
    tokens=tokens.remove('')

print(tokens)

file_name = text_name.rsplit('/', 1)[-1]
file_name = file_name.split('.')[0]

import csv
w = csv.writer(open((""+"spaCy_TOKENS_"+file_name+".csv"), "w", newline="", encoding='utf-8')) ## in the quotation marks insert the path of the output folder
for i in tokens:
    w.writerow([i])


import spacy

nlp = spacy.load('it_core_news_sm') ## it is possibile to load models in other languages
my_doc = nlp(text)


import csv
w = csv.writer(open((""+"spaCy_POS_"+file_name+".csv"), "w", newline="", encoding='utf-8'))  ## in the quotation marks insert the path of the output folder
for token in my_doc:
    if token.text.isalpha() == True :
        w.writerow([token, token.pos_])


w = csv.writer(open(("C:/Users/LORENZO.BABINI/OneDrive - Università Cattolica del Sacro Cuore/Documenti/Digital Humanities/Python-environment/output/"+"spaCy_LEMMA_"+file_name+".csv"), "w", newline="", encoding='utf-8'))
for token in my_doc:
    if token.text.isalpha() == True :
        w.writerow([token, token.lemma_])

