# -*- coding: utf-8 -*-
import tools
import metrics.lev as distance

class Histogram(object):

    def __init__(self, words):
        self.words=words

    def __len__(self):
        return len(self.words.keys())

    def __getitem__(self, key):
        return self.words.get(key,0)

def build_word_histogram(filename):
    text=tools.read_text(filename,clean_txt=False)
    words=tools.find_words(text)
    return build_histogram(words)   

def build_distance_histogram(filename):
    pairs=tools.read_pairs(filename)
    dist=[distance.normalized_lev(word1,word2)
             for word1,word2 in pairs]
    return build_histogram(dist)  

def build_histogram(words):
    words_dict={}
    for word_i in words:
        if word_i in words_dict:
            words_dict[word_i]=words_dict[word_i]+1.0
        else:
        	words_dict[word_i]=0.0
    norm_c=sum(words_dict.values())
    for word_i in words_dict.keys():
    	words_dict[word_i]/=norm_c
    print(words_dict.values()[0:10])
    return Histogram(words_dict)

#build_word_histogram('resources/lab3/proza.iso.utf8')
hist=build_distance_histogram('resources/lab3/bledy.txt')
print(hist.words.keys())