import numpy as np
from collections import defaultdict

def create_histogram(ngrams):
    names={}
    names = defaultdict(lambda:0,names)
    for ngram_i in ngrams:
        if(ngram_i in names):
            names[ngram_i]=names[ngram_i]+1.0
        else:
             names[ngram_i]=1.0
    hist_size=len(names.keys())
    hist=np.zeros((hist_size,))
    for i,key in enumerate(names.keys()):
        hist[i]=names[key]
    hist/=np.sum(hist)
    return hist

def get_ngrams(text,n=2):
    assert type(text)==list
    max_i=len(text)-n+1
    print(len(text))
    ngrams=["".join(text[i:i+n]) for i in range(max_i)]
    #assert (len(text)-len(ngrams))==1
    return ngrams

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
    return " ".join(text.split())

path="PJN/pjn_lab1/54.txt"
raw=read_text(path,False)
ngrams=get_ngrams(raw,2)
h=create_histogram(ngrams)
print(h)
#print(raw[0])
#print(ngrams[0])
