# -*- coding: utf-8 -*-
import numpy as np
import os,re
import codecs,sys 
from collections import defaultdict
import timeit
from metrics.lev import decode_digraphs

def find_words(text):
    return re.findall(u'[(a-z)|ż|ź|ć|ź|ń|ó|ł|ą|ę]+', text.lower()) 

def read_dataset(dir_path):
    path_cats,cats=get_paths(dir_path)
    dataset=[]
    for path_i,cat_i in zip(path_cats,cats):
        text_paths,names=get_paths(path_i)
        text_files=[(cat_i,read_lines(text_path_i)) 
                    for text_path_i in text_paths]
        dataset+=text_files
    print(len(dataset))
    return dataset

def get_paths(path):
    names=os.listdir(path)
    paths=[path+"/"+name_i for name_i in names]
    return paths,names

def read_lines(filename,clean_text=True):
    txt = codecs.open(filename,'r','utf8')
    lines = txt.read()#lines()
    lines=lines.split('\n')
    lines=[line_i for line_i in lines
            if len(line_i)>0]
    if(clean_text):
        lines=[clean(line_i) for line_i in lines]
    return lines

def read_text(filename,clean_txt=True):
    txt = open(filename)
    txt=txt.read()
    if(clean_txt):
        txt=clean(txt)
    return txt

def read_pairs(filename,sep=';'):
    lines=read_lines(filename,clean_text=True)
    pairs=[ tuple(line_i.split(sep)) for line_i in lines]
    return pairs 

def clean(text):
    #text=text.lower()
    #tabu=["\"",",",".","(",")","{","}","!","?"]
    #for token in tabu:
    #    text=text.replace(token,"") 
    #text = re.sub("\d+", "", text)
    text=find_words(text)
    return " ".join(text)

def read(path):
    txt = open(path)
    txt=txt.read()
    return txt

def save(path,text):
    f = open(path,'w')
    f.write(text)
    f.close()

def make_dir(path):
    if(not os.path.isdir(path)):
        os.mkdir(path)

def clock(func):
    def inner_func(*args):
        start_time=timeit.default_timer()
        result=func(*args)
        end_time = timeit.default_timer()
        total_time = (end_time - start_time)
        print("time %i ",total_time)
        return result
    return inner_func

def ui_loop(cls,fun):
    while(True):
        if(not fun(cls)):
            break

def unique_list(list_i):
    return list(set(list_i))

def print_unicode(items,to_unicode=None):
    for item_i in items:
        if(to_unicode==None):
            item_i=decode_digraphs(item_i)
            print(unicode(item_i))
        else:
            print(to_unicode(item_i))

def use_utf8():
    UTF8Writer = codecs.getwriter('utf8')
    sys.stdout = UTF8Writer(sys.stdout)
