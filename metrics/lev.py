# -*- coding: utf-8 -*-
import numpy as np
import tools
from sets import Set

POLISH_TO_LATIN={u'ą':u'a',u'ę':u'e',u'ó':u'o',
                 u'ś':u's',u'ł':u'l',u'ż':u'z',
                 u'ź':u'z',u'ć':u'c',u'ń':u'n',
                 u'u':u'ó'}

DIGRAPHS={u'ż':u'rz',u'h':u'ch',u'ć':u'ci',
          u'ń':u'ni',u'ś':u'si',u'ź':u'zi'}
          #u'ą':u'om',u'ę':u'em'}

DI_CODES=u'!?&$^*'
DIGRAPHS_TO_SPECIAL={u'rz':DI_CODES[0],u'ch':DI_CODES[1],
                     u'ci':DI_CODES[2],u'ni':DI_CODES[3],
                     u'si':DI_CODES[4],u'zi':DI_CODES[5]}

SPECIAL_TO_DIGRAPH = dict((v,k) for k,v in DIGRAPHS_TO_SPECIAL.iteritems())

def code_digraphs(word):
    for key_i,value_i in DIGRAPHS_TO_SPECIAL.iteritems():
        word=word.replace(key_i,value_i)
    print(word)
    return word

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
            c1,c2=context(i,j,word1,word2)
            l1=dist[i-1][j] + 1.0
            l2=dist[i][j-1]+ 1.0
            l3=dist[i-1][j-1]+ full_cost(word1[i-1],word2[j-1])
            dist[i][j]=min([l1,l2,l3])
    #print(dist)
    return dist[n][m]

def context(i,j,word1,word2):
    c1=None
    c2=None
    if(i<len(word1)-1):
        c1=word1[i]
    if(j<len(word2)):
        c2=word2[j]
    return c1,c2

def full_cost(token1,token2):
    d1=di_correction(token1,token2)
    if(d1!=0.0):
        return d1
    d2=di_correction(token2,token1)
    if(d2!=0.0):
        return d2
    return equ(token1,token2)


def simple_cost(token1,token2):
    d1=orth_correction(token1,token2)
    if(d1!=0.0):
        return d1
    return equ(token1,token2)

def equ(l1,l2):
    return int(not l1==l2)

def di_correction(token1,token2):
    if(token1 in DIGRAPHS):
        di=DIGRAPHS[token1]
        code=DIGRAPHS_TO_SPECIAL[di]
        if(code==token2):
            return 0.1
    #if(token1 in SPECIAL_TO_DIGRAPH):
    #    di=SPECIAL_TO_DIGRAPH[token1]
    #    if(di[0]==token2 or di[1]==token2):
    #        #print("ok")
    #        return 0.1
    return 0.0

def orth_correction(token1,token2):
    if(token1 in POLISH_TO_LATIN):
        if(POLISH_TO_LATIN[token1]==token2):
            return 0.2
    if(token2 in POLISH_TO_LATIN):
        if(POLISH_TO_LATIN[token2]==token1):
            return 0.2
    return 0.0#equ(token1,token2)

@tools.clock
def correct_word(new,raw_words):
    full_words=eff_heuristic(new,raw_words)
    print(len(full_words))
    new=code_digraphs(new)
    words=[code_digraphs(word_i) for word_i in full_words]
    dist=[lev_cxt(new,word_i) for word_i in words] 
    dist=np.array(dist)
    index=np.argmin(dist)
    return full_words[index]

def eff_heuristic(new,words,fact=0.5):
    def prop(word_i):
        return float(len(new))/float(len(word_i))
    new_words=[word_i for word_i in words
                   if prop(word_i)>0.5 and prop(word_i)<1.5]
    return new_words

def curry_correct(words):
    return lambda new:correct_word(new,words)

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
            l1=dist[i-1][j] +1.0
            l2=dist[i][j-1] + 1.0
            l3=dist[i-1][j-1]+simple_ort(word1[i-1],word2[j-1])  
            dist[i][j]=min([l1,l2,l3])
    return dist[n][m]

if __name__ == "__main__":
    print(lev("chak".decode('utf-8'),"cha".decode('utf-8')))
    print(lev("chak".decode('utf-8'),"hak".decode('utf-8')))