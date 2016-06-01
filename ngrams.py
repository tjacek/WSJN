import numpy as np
import pickle,metrics

class NgramMetric(object):
    def __init__(self, ngram_dict):
        self.ngram_dict = ngram_dict       
        self.histograms={}

    def __call__(self,x,y):
        hist_x=self.conversion(y)#self.ngram_dict.get_histogram(x)
        hist_y=self.conversion(x)#self.ngram_dict.get_histogram(y)
        return metrics.l2(hist_x,hist_y)

    def conversion(self,text):
        if(text in self.histograms):
            return self.histograms[text]
        else:
            hist=self.ngram_dict.get_histogram(text)
            self.histograms[text]=hist
            return hist

class NgramDict(object):
    def __init__(self,n=2):
        self.indices={}
        self.n=n

    def __len__(self):
        return len(self.indices.keys())

    def __str__(self):
        return str(self.indices.keys())

    def __getitem__(self, key):
        return self.indices.get(key,0)

    def add_all(self,ngrams):
        for ngram_i in ngrams:
            self.add(ngram_i)

    def add(self,token):
        if(not token in self.indices):
            self.indices[token]=len(self)+1

    def get_histogram(self,text):
        ngrams_text=get_ngrams(text,self.n)
        hist=np.zeros((len(self)+1,),dtype=float)
        for ngram_i in ngrams_text:
            index=self[ngram_i]
            #if(index!=np.inf):
            hist[index]+=1.0
        hist/=np.sum(hist)
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

def make_ngram_metric(text,n=2):
    ngram_dict=make_ngram_dict(text,create_hist=False,n=2)
    return NgramMetric(ngram_dict)

def make_ngram_dict(text,create_hist=True,n=2):
    ngram_dict=NgramDict(n)
    ngrams=get_ngrams(text,n)
    for ngram_i in ngrams:
        ngram_dict.add(ngram_i)
    if(create_hist):
        hist=ngram_dict.get_histogram(text)
        return ngram_dict,hist
    return ngram_dict#,hist

def get_ngrams(text,n=2):
    max_i=len(text)
    ngrams=[text[i-n:i] for i in range(2,max_i)]
    return ngrams