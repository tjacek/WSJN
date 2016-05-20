import numpy as np
import ngrams,tools,metrics
import cmd,sys

DATASET_SOURCE="resources/lang_utf8"

class Cls(object):
    def __init__(self,ngram_dict,dataset):
        self.ngram_dict=ngram_dict
        self.dataset = dataset

    def predict(self,raw_text):
        text=tools.clean(raw_text)
        ngrams_text=ngrams.get_ngrams(text,self.ngram_dict.n)        
        hist=self.ngram_dict.get_histogram(ngrams_text)
        cat=knn(hist,self.dataset,metrics.l2)
        return cat

def make_cls(path,n):
    dataset=tools.read_dataset(path)
    ngram_dict,hist_dataset=ngrams.dataset2ngrams(dataset,n)
    print(len(ngram_dict))
    return Cls(ngram_dict,hist_dataset)

def knn(vect,dataset,metric):
    inst=[(cat_i,metric(vect,vec_i))
             for cat_i,vec_i in dataset]    
    distances=[ dist_i for cat_i,dist_i in inst]
    cats=[cat_i for cat_i,dist_i in inst]
    distances=np.array(distances)
    i=np.argmin(distances)
    return cats[i]

def main_loop(n):
    cls=make_cls(DATASET_SOURCE,n)
    while(True):
        if(not cls_lang(cls)):
            break

def cls_lang(cls):
    raw_text = raw_input("Enter sentences ").decode('utf-8')
    print("\n \n")
    if(raw_text=="quit"):
        return False
    cat=cls.predict(raw_text)
    print(cat)
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        n=2
    else:
        n=int(sys.argv[1])
    main_loop(n)