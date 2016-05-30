# -*- coding: utf-8 -*-
import tools,histogram
import forms.build as build
import metrics.lev as distance

class CondProb(object):
    def __init__(self, model,priori):
        self.model=model
        self.priori=priori

    def p(self,c,w):
    	dist=normalized_lev(c,w)
        p_wc=self.model[dist]
        p_c=self.priori[c]
        return p_wc*p_c

def build_spellchecker(begin_file,end_file,text_file):
    forms_dict=build.build_forms(begin_file,end_file)
    basics=forms_dict.forms_to_basic()
    histogram.build_forms_histogram(text_file,basics)
    print(basics.keys()[0:10])
    #forms.   

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

build_spellchecker(u'resources/lab3/pocz.dat',u'resources/lab3/konc.dat','resources/lab3/proza.iso.utf8')
#cond=build_cond_p('resources/lab3/bledy.txt','resources/lab3/proza.iso.utf8')
#print(cond.priori.k_keys(10))
#print(cond.p(u'lewym',u'lweym'))