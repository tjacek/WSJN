import numpy as np
import pickle

class NgramDict(object):
    def __init__(self,n=2):
        self.indices={}
        self.n=n

    def __len__(self):
        return len(self.indices.keys())

    def __str__(self):
        return str(self.indices.keys())

    def __getitem__(self, key):
        return self.indices[key]

    def add(self,token):
        if(not token in self.indices):
            self.indices[token]=len(self)

    def get_histogram(self,text):
        hist=np.zeros((len(self),),dtype=float)
        ngrams=get_ngrams(text)
        for ngram_i in ngrams:
            hist[self[ngram_i]]+=1.0
        return hist

def make_ngram_dict(text,n=2):
    ngram_dict=NgramDict(n)
    ngrams=get_ngrams(text,n)
    for ngram_i in ngrams:
        ngram_dict.add(ngram_i)
    hist=ngram_dict.get_histogram(text)
    return ngram_dict,hist

def get_ngrams(text,n=2):
    max_i=len(text)-n+1
    ngrams=[text[i:i+n] for i in range(max_i)]
    return ngrams

ngram_dict,hist=make_ngram_dict("przetwarzanie")
print(str(hist))
print(str(ngram_dict.indices))