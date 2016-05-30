# -*- coding: utf-8 -*-
import tools
import metrics.lev as distance
from metrics.lev import code_digraphs
from sets import Set

class Histogram(object):

    def __init__(self, words,default):
        self.words=words
        self.default=default

    def __len__(self):
        return len(self.words.keys())

    def __getitem__(self, key):
        return self.words.get(key,self.default)

    def k_keys(self,k=10):
        return self.words.keys()[0:k]

def build_forms_histogram(filename,forms2basic,hist_size=0):
    text=tools.read_text(filename,clean_txt=False)
    words=tools.find_words(text)    
    words=[code_digraphs(word_i) for word_i in words]
    forms=[ forms2basic[word_i] for word_i in words
                     if(word_i in forms2basic)]
    #print(len(forms))
    forms=tools.unique_list(forms)#list(forms)        
    #print(len(forms))
    #print(forms2basic)
    return build_histogram(forms,laplace_smoothing=True,size=hist_size)   

def build_word_histogram(filename,forms):
    text=tools.read_text(filename,clean_txt=False)
    words=tools.find_words(text)    
    return build_histogram(words,laplace_smoothing=False)   

def build_histogram(words,laplace_smoothing=True,size=0):
    words_dict={}
    for word_i in words:
        if word_i in words_dict:
            words_dict[word_i]=words_dict[word_i]+1.0
        else:
        	words_dict[word_i]=1.0
    if(laplace_smoothing):
        n=sum(words_dict.values())
        m=float(size) #len(words_dict.keys()))
        norm_c=n+m
        for word_i in words_dict.keys():
            words_dict[word_i]+=1.0
            words_dict[word_i]/=norm_c
        return Histogram(words_dict,default=1.0/norm_c)
    else:
        norm_c=sum(words_dict.values())
        for word_i in words_dict.keys():
    	    words_dict[word_i]/=norm_c
    #print(words_dict.values()[0:10])
        return Histogram(words_dict,default=0)