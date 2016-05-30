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

    def k_keys(self,k=10):
        return self.words.keys()[0:k]

def build_word_histogram(filename):
    text=tools.read_text(filename,clean_txt=False)
    words=tools.find_words(text)
    return build_histogram(words,laplace_smoothing=True)   

def build_histogram(words,laplace_smoothing=True):
    words_dict={}
    for word_i in words:
        if word_i in words_dict:
            words_dict[word_i]=words_dict[word_i]+1.0
        else:
        	words_dict[word_i]=0.0
    if(laplace_smoothing):
        n=sum(words_dict.values())
        m=float(len(words_dict.keys()))
        norm_c=n+m
        for word_i in words_dict.keys():
            words_dict[word_i]+=1.0
            words_dict[word_i]/=norm_c
    else:
        norm_c=sum(words_dict.values())
        for word_i in words_dict.keys():
    	    words_dict[word_i]/=norm_c
    #print(words_dict.values()[0:10])
    return Histogram(words_dict)