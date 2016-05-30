# -*- coding: utf-8 -*-
import tools
import metrics.lev as distance
import metrics.knn as knn
import numpy as np

class FormsDict(object):
    def __init__(self,endings):
        self.endings=endings

    def get_ending(self,new_word,n=7):
    	begin=self.nearest_begin(new_word)
        words=self.full_words(begin)
        words=tools.unique_list(words)
        if(len(words)<n):
            n=len(words)
        nearest_words=knn.nearest_k(new_word,words,k=n)
        nearest_words=[distance.decode_digraphs(word_i) 
                          for word_i in nearest_words]
        return nearest_words	

    def full_words(self,begin):
        full_words=[]
        for begin_i in begin: 
            endings_k=self.endings[begin_i]
            words_i=[begin_i+end_i for end_i in endings_k]
            full_words+=words_i
        return full_words

    def nearest_begin(self,new_word):
        keys=self.endings.keys()
        return knn.nearest_k_eff(new_word,keys)
        
    def all_forms(self):
        all_words=[]
        for key_i in self.endings:
            all_words+=self.full_words(key_i)
        return all_words

    def stats(self):
        keys=self.endings.values()
        lengths=[len(key_i) for key_i in keys]
        return max(lengths)

    def forms_to_basic(self):
        forms2basic={}
        for key_i in self.endings:
            words=self.full_words([key_i])
            for word_i in words:
                forms2basic[word_i]=key_i
        return forms2basic        