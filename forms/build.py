# -*- coding: utf-8 -*-
import tools
import sys,codecs
from metrics.lev import code_digraphs
from forms import FormsDict

def build_forms(begin_file,end_file):
    begin_lines=tools.read_lines(begin_file,clean_text=False)
    begin=parse_begin(begin_lines)
    end_lines=tools.read_lines(end_file,clean_text=False)
    end=parse_end(end_lines)
    unified=unify_dirs(begin,end)
    return FormsDict(unified)

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
    	return endings
    lines=[(int(line_i[0]), sub_parse(line_i[2]) ) 
                   for line_i in lines]
    return dict(lines)

def unify_dirs(key_dir,value_dir,encode=True):
    new_dir={}
    for key_i in key_dir:
        index=key_dir[key_i]
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