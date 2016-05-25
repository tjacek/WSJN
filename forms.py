# -*- coding: utf-8 -*-
import tools
import metrics.lev as distance
import numpy as np

class Forms(object):
    def __init__(self,endings):
        self.endings=endings

    def get_ending(self,new_word):
    	begin=self.nearest_begin(new_word)
        words=self.full_words(begin)
        dist=[distance.lev_cxt(new_word,word_i) for word_i in words] 
        dist=np.array(dist)
        index=np.argmin(dist)
        return words[index]	

    def full_words(self,begin):
    	endings_k=self.endings[begin]
        return [begin+end_i for end_i in endings_k]

    def nearest_begin(self,new_word):
    	keys=self.endings.keys()
        dist=[distance.lev_cxt(new_word,key_i) for key_i in keys] 
        dist=np.array(dist)
        index=np.argmin(dist)
        return keys[index]	

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
    return dict(lines)

def parse_end(lines):
    lines=[line_i.split(u';') for line_i in lines]
    def sub_parse(endings):
    	endings=endings.split(u':')
    	endings=[end_i for end_i in endings
    	               if len(end_i)>0]
    	return endings
    lines=[(int(line_i[0]), sub_parse(line_i[2]) ) 
                   for line_i in lines]
    return dict(lines)

def unify_dirs(key_dir,valu_dir):
    new_dir={}
    for key_i in key_dir:
        index=key_dir[key_i]
        new_dir[key_i]=valu_dir[index]		
    return new_dir	

forms=build_forms(u'resources/lab2/pocz.dat',
	         u'resources/lab2/konc.dat')

print(forms.get_ending('a'))