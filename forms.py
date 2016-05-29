# -*- coding: utf-8 -*-
import tools
import metrics.lev as distance
import metrics.knn as knn
from metrics.lev import code_digraphs
import numpy as np
import codecs
import sys 

class Forms(object):
    def __init__(self,endings):
        self.endings=endings

    def get_ending(self,new_word,n=7):
    	begin=self.nearest_begin(new_word)
        #for begin_i in begin:
        #    print(begin_i)
        #    print(self.endings[begin_i])
        #print("************")
        words=self.full_words(begin)
        words=tools.unique_list(words)
        if(len(words)<n):
            n=len(words)
        #for word_i in words:
        #    print(word_i)
        print("*******")
        nearest_words=knn.nearest_k(new_word,words,k=n)
        nearest_words=[distance.decode_digraphs(word_i) 
                          for word_i in nearest_words]
        return nearest_words	

    def full_words(self,begin):
        full_words=[]
        for begin_i in begin: 
            #print(unicode(begin_i))
            endings_k=self.endings[begin_i]
            words_i=[begin_i+end_i for end_i in endings_k]
            #words_i.append(begin_i)
            full_words+=words_i
        return full_words

    def nearest_begin(self,new_word):
        keys=self.endings.keys()
        return knn.nearest_k_eff(new_word,keys)#.nearest_k(new_word,keys)
        
    def all_forms(self):
        all_words=[]
        for key_i in self.endings:
            all_words+=self.full_words(key_i)
        return all_words

    def stats(self):
        keys=self.endings.values()
        lengths=[len(key_i) for key_i in keys]
        return max(lengths)

def build_forms(begin_file,end_file):
    begin_lines=tools.read_lines(begin_file,clean_text=False)
    begin=parse_begin(begin_lines)
    end_lines=tools.read_lines(end_file,clean_text=False)
    end=parse_end(end_lines)
    unified=unify_dirs(begin,end)
    return Forms(unified)

def parse_begin(lines):
    lines=[line_i.split(u':') for line_i in lines]
    lines=[(line_i[0],int(line_i[1])) for line_i in lines
                            if len(line_i)==2]
    begin={}
    for key_i,value_i in lines:
        if(key_i in begin):
            begin[key_i].append(value_i)
        else:
            begin[key_i]=[value_i]
    return dict(begin)

def parse_end(lines):
    lines=[line_i.split(u';') for line_i in lines]
    def sub_parse(endings):
    	endings=endings.split(u':')
    	#for end_i in endings
    	              # if len(end_i)>0]
    	return endings
    lines=[(int(line_i[0]), sub_parse(line_i[2]) ) 
                   for line_i in lines]
    return dict(lines)

def unify_dirs(key_dir,value_dir,encode=True):
    new_dir={}
    for key_i in key_dir:
        index=key_dir[key_i]
        #new_dir[key_i]=valu_dir[index]
        all_endings=[]
        for end_i in index:
            all_endings+=value_dir[end_i]
        if(encode):
            key_i=code_digraphs(key_i)
            new_dir[key_i]=[code_digraphs(value_i) 
                                for value_i in all_endings]	
        else:
            new_dir[key_i]=all_endings 
    return new_dir	

#forms=build_forms(u'resources/lab2/pocz.dat',
#	         u'resources/lab2/konc.dat')
#print(forms.stats())

#all_form=forms.all_forms()
#for form_i in all_form:
#    print(form_i)