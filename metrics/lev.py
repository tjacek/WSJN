# -*- coding: utf-8 -*-
import numpy as np
import tools
from sets import Set

POLISH_TO_LATIN={'ą':'a','ę':'e','ó':'o',
                 'ś':'s','ł':'l','ż':'z',
                 'ź':'z','ć':'c','ń':'n',
                 'u':'ó'}

DIGRAPHS={'ż':'rz','h':'ch','ć':'ci',
          'ń':'ni','ś':'si','ź':'zi',
          'ą':'om','ę':'em'}

def lev_cxt(word1,word2):
    n=len(word1)
    m=len(word2)
    dist=np.zeros((n+1,m+1))
    for i in range(n+1):
        dist[i][0]=i 
    for j in range(m+1):
        dist[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):   
            c1,c2=context(i-1,j-1,word1,word2)
            l1=dist[i-1][j]+ 1
            l2=dist[i][j-1]+ 1
            l3=dist[i-1][j-1]+di_ctx(word1[i-1],word2[j-1],c1,c2)
            dist[i][j]=min([l1,l2,l3])
    return dist[n-1][m-1]

def context(i,j,word1,word2):
    c1=None
    c2=None
    if(i>0):
        c1=word1[i-1]
    if(j>0):
        c2=word2[j-1]
    return c1,c2

def di_ctx(word1,word2,c1,c2):
    d1=di_correction(word1,c2,word2)
    d2=di_correction(word2,c1,word1)
    return d1+d2

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
            l1=dist[i-1][j] + 1.0
            l2=dist[i][j-1] + 1.0
            l3=dist[i-1][j-1]+orth_correction(word1[i-1],word2[j-1])  
            dist[i][j]=min([l1,l2,l3])
    return dist[n][m]

def equ(l1,l2):
    return int(not l1==l2)

def di_correction(token1,prev,token2):
    if(prev==None):
        return 1.0
    #print(token1+'-'+token2+next)
    if(token1 in DIGRAPHS):
        di=prev+token2      
        if(DIGRAPHS[token1]==di):
            return 0.2
    return equ(token1,token2)

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
    dist=[lev_cxt(new,word_i) for word_i in words] 
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
    print(lev("chak".decode('utf-8'),"cha".decode('utf-8')))
    print(lev("chak".decode('utf-8'),"hak".decode('utf-8')))