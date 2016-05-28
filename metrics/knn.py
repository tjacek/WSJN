import numpy as np
import lev,tools

def begin_metric(word1,word2):
    size1=len(word1)
    size2=len(word2)
    if(size1<size2):
        short_word=word2[0:size1]
        return lev.lev_cxt(word1,short_word)
    else:
        short_word=word1[0:size2]
        return lev.lev_cxt(word1,short_word)

@tools.clock
def nearest_radius(new_word,keys,eps=3.0,metric=begin_metric):
    #best=[]
    indexes=[]
    for i in xrange(len(keys)):
        key_i=keys[i]
        d=metric(new_word,key_i)  
        if(d<eps):
            indexes.append(i)
    k_words=[ keys[i] for i in indexes]
    return k_words

def size_cond(threshold,word1,word2):
    return np.abs(len(word1)-len(word2))<threshold

@tools.clock
def nearest(new_word,keys,metric=begin_metric):
    best=np.inf
    index=0
    for i in xrange(len(keys)):
        key_i=keys[i]
        if(size_cond(best,new_word,key_i)):
            d=metric(new_word,key_i)  
            if(d<best):
                best=d
                indexe=i
    #k_words=[ keys[i] for i in indexes]
    return [keys[index]]



