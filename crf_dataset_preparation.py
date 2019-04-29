import nltk
import nltk.data
import pandas as pd
import numpy as np
from majority import dataset
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

data = dataset()
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def tag_set(sent, term1, term2, rel):
    data = dataset()
    
    tags = []
    senten = ''
    for j in word_tokenize(sent):
        senten = senten + j + ' '

    pos_term1_start = senten.find(term1)
    pos_term1_end = senten.find(term1)+len(term1)
    pos_term2_start = senten.find(term2)
    pos_term2_end = senten.find(term2)+len(term2)
    word = lemmatizer.lemmatize(ps.stem(rel))
    
    for j in range(len(senten)):
        if j >= pos_term1_start and j <= pos_term1_end:
            if senten[j] == ' ':
                tags.append('CC')
        elif j >= pos_term2_start and j <= pos_term2_end:
            if senten[j] == ' ':
                tags.append('EE')
        elif senten[j] == ' ':
        	tags.append('O')

    k=0
    for j in word_tokenize(senten):
    	if j.find(word) != -1:
    		tags[k] = 'RR' 
    	k = k+1
    return(tags)

l = []
tags = []

for i in range(len(data['sentence'])):
    text = data['sentence'][i]
    term1 = data['term1'][i]
    term2 = data['term2'][i]
    relation = data['relation'][i]
    tags = tag_set(text, term1, term2, relation)
    print(i)


    custom_sentence_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
    tokenized = custom_sentence_tokenizer.tokenize(text)
    
    k = 0
    word = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(word)
    
    for j in tagged:
        w, pos = j
        s = 'Sentence: '+str(i)
        l.append([s, w, pos, tags[k]])
        k +=1


columns= ['Sentence #', 'Word','POS', 'Tag']
data = pd.DataFrame(l, columns=columns)

data.to_csv('crf_dataset.csv', encoding='UTF-8', index=False)