import numpy as np
import os,re
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

def read_lines(filename):
    txt = open(filename)
    lines = txt.readlines()
    lines=[clean(line_i) for line_i in lines]
    return lines

def read_text(filename,words=False):
    txt = open(filename)
    txt=txt.read()
    txt=clean(txt)
    if(words):
        text=txt.split(" ")
    else:
        text=[s_i for s_i in txt] 
    return text

def clean(text):
    text=text.lower()
    text=text.replace(",","")
    text=text.replace("\"","")
    text = re.sub("\d+", "", text)
    return " ".join(text.split())

read_dataset("lang")