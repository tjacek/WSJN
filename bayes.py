# -*- coding: utf-8 -*-
import tools,histogram
import forms.build as build
import metrics.lev as distance
from metrics.lev import code_digraphs
import metrics.knn as knn

class Spellchecker(object):
    def __init__(self,cond,basic,forms_dict):
        self.cond=cond
        self.basic=basic
        self.forms_dict=forms_dict

    def p(self,c,w):
        #c=code_digraphs(c)
        #w=code_digraphs(w)
        w_form=self.basic[w]
        return self.cond.p(c,w_form)

    def correct(self,new_word):
        new_word=code_digraphs(new_word)
        keys=self.forms_dict.all_basic()
        words=knn.nearest_k(new_word,keys)
        full_words=self.forms_dict.full_words(words)
        prob_pairs=[ (word_i,self.p(new_word,word_i)) 
                        for word_i in full_words]
        return prob_pairs

class CondProb(object):
    def __init__(self, model,priori):
        self.model=model
        self.priori=priori

    def p(self,c,w):
    	dist=normalized_lev(c,w)
        p_wc=self.model[dist]
        p_c=self.priori[c]
        return p_wc*p_c

def build_spellchecker(begin_file,end_file,
	                     model_path,priori_path):
    forms_dict=build.build_forms(begin_file,end_file)
    basics=forms_dict.forms_to_basic()
    model=build_distance_histogram(model_path)
    priori=histogram.build_forms_histogram(priori_path,basics)
    cond=CondProb(model,priori)
    #print(basics.keys()[0:10])
    return Spellchecker(cond,basics,forms_dict)

def build_cond_p(model_path,priori_path):
    model=build_distance_histogram(model_path)
    priori=histogram.build_word_histogram(priori_path)
    return CondProb(model,priori)

def build_distance_histogram(filename):
    pairs=tools.read_pairs(filename)
    dist=[normalized_lev(word1,word2)
             for word1,word2 in pairs]
    return histogram.build_histogram(dist)

def normalized_lev(word1,word2):
    return int(4.0*distance.lev_cxt(word1,word2))

spell=build_spellchecker(u'resources/lab3/pocz.dat',u'resources/lab3/konc.dat',
	               u'resources/lab3/bledy.txt',u'resources/lab3/proza.iso.utf8')
print(spell.correct(u'mlody'))
#cond=build_cond_p('resources/lab3/bledy.txt','resources/lab3/proza.iso.utf8')
#print(cond.priori.k_keys(10))
#print(cond.p(u'lewym',u'lweym'))