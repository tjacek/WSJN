import numpy as np
import os,re
import codecs
from collections import defaultdict

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
    lines = txt.readlines()
    if(clean_text):
        lines=[clean(line_i) for line_i in lines]
    lines=" ".join(lines)
    return lines

def read_text(filename,clean_txt=True):
    txt = open(filename)
    txt=txt.read()
    if(clean_text):
        txt=clean(txt)
    return text

def clean(text):
    text=text.lower()
    tabu=["\"",",",".","(",")","{","}","!","?"]
    for token in tabu:
        text=text.replace(token,"") 
    text = re.sub("\d+", "", text)
    return " ".join(text.split())

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