# -*- coding: utf-8 -*-
import numpy as np
import tools
from sets import Set

POLISH_TO_LATIN={'ą':'a','ę':'e','ó':'o',
                 'ś':'s','ł':'l','ż':'z',
                 'ź':'z','ć':'c','ń':'n'}

def lev_cont(word1,word2):
    n=len(word1)
    m=len(word2)
    dist=np.zeros((n+1,m+1))
    for i in range(n+1):
        dist[i][0]=i 
    for j in range(m+1):
        dist[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            l1=dist[i-1][j]+1
            l2=dist[i][j-1]+1
            c1,c2=context(i,j,word1,word2)
            l3=dist[i-1][j-1]+equ(word1[i],word2[j],c1,c2)
            dist[i][j]=min([l1,l2,l3])
    return dist[n-1][m-1]

def context(i,j,word1,word2):
    c1=None
    c2=None
    if(i+1<len(word1)):
        c1=word1[i]
    if(j+1<len(word2)):
        c2=word1[j]
    return c1,c2

def lev(word1,word2):
    n=len(word1)
    m=len(word2)
    dist=np.zeros((n+1,m+1),dtype=float)
    for i in range(n+1):
        dist[i][0]=i 
    for j in range(m+1):
        dist[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            l1=dist[i-1][j]+1.0
            l2=dist[i][j-1]+1.0
            l3=dist[i-1][j-1]+orth_correction(word1[i-1],word2[j-1])  
            #l3=dist[i-1][j-1]+equ(word1[i-1],word2[j-1])
            dist[i][j]=min([l1,l2,l3])
    return dist[n][m]

def equ(l1,l2):
    return int(not l1==l2)

def orth_correction(token1,token2):
    if(token1 in POLISH_TO_LATIN):
        if(POLISH_TO_LATIN[token1]==token2):
            return 0.1
    if(token2 in POLISH_TO_LATIN):
        if(POLISH_TO_LATIN[token2]==token1):
            return 0.1
    return equ(token1,token2)

@tools.clock
def correct_word(new,words):
    words=eff_heuristic(new,words)
    print(len(words))
    dist=[lev(new,word_i) for word_i in words] 
    dist=np.array(dist)
    index=np.argmin(dist)
    return words[index]

def eff_heuristic(new,words,fact=0.5):
    def prop(word_i):
        return float(len(new))/float(len(word_i))
    new_words=[word_i for word_i in words
                   if prop(word_i)>0.5 and prop(word_i)<1.5]
    return new_words

def curry_correct(words):
    return lambda new:correct_word(new,words)

if __name__ == "__main__":
    print(lev("żółć".decode('utf-8'),"zolc".decode('utf-8')))
    #print(lev("żółć".decode('utf-8'),"zol".decode('utf-8')))    
    print(lev("zolc".decode('utf-8'),"zol".decode('utf-8')))