import numpy as np
import pickle

class NgramDict(object):
    def __init__(self,n=2):
        self.indices={}
        self.n=n
        self.size=0

    def __len__(self):
        return len(self.indices.keys())

    def __str__(self):
        return str(self.indices.keys())

    def __getitem__(self, key):
        return self.indices[key]

    def add_all(self,ngrams):
        for ngram_i in ngrams:
            self.add(ngram_i)

    def add(self,token):
        if(not token in self.indices):
            self.indices[token]=len(self)

    def get_histogram(self,ngrams_text):
        hist=np.zeros((len(self),),dtype=float)
        for ngram_i in ngrams_text:
            hist[self[ngram_i]]+=1.0
        hist/=sum(hist)
        return hist

def dataset2ngrams(dataset,n=2):
    ngram_dict=NgramDict(n)
    ngram_dataset=[ (cat_i,get_ngrams(text_i,n))  
                    for cat_i,text_i in dataset]
    for cat_i,ngrams_i in ngram_dataset:    
        print(cat_i)
        ngram_dict.add_all(ngrams_i)
    hist_dataset=[ (cat_i,ngram_dict.get_histogram(ngrams_i)) 
           for cat_i,ngrams_i in ngram_dataset]    
    return ngram_dict,hist_dataset

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

#ngram_dict,hist=make_ngram_dict("przetwarzanie")
#print(str(hist))
#print(str(ngram_dict.indices))