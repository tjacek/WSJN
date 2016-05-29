import numpy as np
import lev,tools

def begin_metric(word1,word2):
    size1=len(word1)
    size2=len(word2)
    if(size1==size2):
        return lev.lev_cxt(word1,word2),0
    diff=abs(size1-size2)
    if(size1<size2):
        short_word=word2[0:size1]
        return lev.lev_cxt(word1,short_word),diff
    else:
        short_word=word1[0:size2]
        return lev.lev_cxt(word2,short_word),diff

@tools.clock
def nearest_radius(new_word,keys,eps=3.0,metric=begin_metric):
    #best=[]
    indexes=[]
    for i in xrange(len(keys)):
        key_i=keys[i]
        d,diff=metric(new_word,key_i)  
        if(d<eps):
            indexes.append(i)
    k_words=[ keys[i] for i in indexes]
    return k_words

@tools.clock
def nearest_radius_eff(new_word,keys,eps=3.0,max_diff=3,metric=begin_metric):
    #best=[]
    indexes=[]
    for i in xrange(len(keys)):
        key_i=keys[i]
        if(size_cond(max_diff,new_word,key_i)):
            d,diff=metric(new_word,key_i)  
            if(d<eps):
                indexes.append(i)
    k_words=[ keys[i] for i in indexes]
    return k_words

def size_cond(threshold,word1,word2):
    return np.abs(len(word1)-len(word2))<threshold

def nearest(new_word,keys,metric=lev.lev_cxt):
    dist=[metric(new_word,key_i) for key_i in keys] 
    dist=np.array(dist)
    index=np.argmin(dist)
    return keys[index]

@tools.clock
def nearest_eff(new_word,keys,metric=begin_metric):
    best=np.inf
    best_full=np.inf
    index=0
    for i in xrange(len(keys)):
        key_i=keys[i]
        if(size_cond(best_full,new_word,key_i)):
            d,diff=metric(new_word,key_i)  
            full_dist=d+diff
            if(d<best):
                best=d
                index=i
            if(full_dist<best_full):
                best_full=full_dist
    #k_words=[ keys[i] for i in indexes]
    return [keys[index]]

def nearest_k(new_word,keys,k=10,metric=lev.lev_cxt):
    dists=[metric(new_word,key_i) for key_i in keys] 
    dists=np.array(dists)
    dist_inds=dists.argsort()[0:k]
    k_words=[ keys[i] for i in dist_inds]
    return k_words

def nearest_k_eff(new_word,keys,k=5,metric=begin_metric):
    best=np.full((k,),np.inf)
    indexes=np.zeros(k,dtype=int)
    best_full=np.inf
    for i in xrange(len(keys)):
        key_i=keys[i]
        if(size_cond(best_full,new_word,key_i)):
            d,diff=metric(new_word,key_i)  
            full_dist=d+diff
            update_best(d,i,best,indexes,k)
            if(full_dist<best_full):
                best_full=full_dist
    k_words=[keys[i] for i in indexes]
    return k_words

def update_best(new,new_index,best,best_index,k):
    index=-1
    for i in xrange(k):
        best_i=best[i]
        if(new<best_i):
            index=i
            break
    if(index>=0):
        best[index]=new
        best_index[index]=new_index