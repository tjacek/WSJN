# -*- coding: utf-8 -*-
import tools,histogram
import forms.build as build
import metrics.lev as distance
from metrics.lev import code_digraphs
import metrics.knn as knn
import numpy as np

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

    def correct(self,new_word,unique=False):
        new_word=code_digraphs(new_word)
        keys=self.forms_dict.all_basic()
        words=knn.nearest_k(new_word,keys,k=5,metric=norm_begin_metric)
        #tools.print_unicode(words)
        if(unique):
            full_words=[]
            for word_i in words:
                full_word_i=self.forms_dict.full_words([word_i])[0]
                full_words.append(full_word_i)
        else:
            full_words=self.forms_dict.full_words(words)
        prob_pairs=[ (word_i,self.p(new_word,word_i)) 
                        for word_i in full_words]
        prob_pairs.sort(key=lambda x: x[1], reverse=True)
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
    priori=histogram.build_forms_histogram(priori_path,basics,len(forms_dict))
    cond=CondProb(model,priori)
    return Spellchecker(cond,basics,forms_dict)

def build_cond_p(model_path,priori_path):
    model=build_distance_histogram(model_path)
    priori=histogram.build_word_histogram(priori_path)
    return CondProb(model,priori)

def build_distance_histogram(filename):
    pairs=tools.read_pairs(filename)
    dist=[normalized_lev(word1,word2)
             for word1,word2 in pairs]
    hist_size=max(dist)
    return histogram.build_histogram(dist,laplace_smoothing=True,size=hist_size)

def norm_begin_metric(word1,word2):
    d,diff=knn.begin_metric(word1,word2)
    if(d==np.inf):
        return d
    return int(4.0*d)

def normalized_lev(word1,word2):
    return int(4.0*distance.lev_cxt(word1,word2))