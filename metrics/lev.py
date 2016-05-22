# -*- coding: utf-8 -*-
import numpy as np

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
    dist=np.zeros((n+1,m+1))
    for i in range(n+1):
        dist[i][0]=i 
    for j in range(m+1):
        dist[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            l1=dist[i-1][j]+1
            l2=dist[i][j-1]+1
            l3=dist[i-1][j-1]+equ(word1[i-1],word2[j-1])
            dist[i][j]=min([l1,l2,l3])
    return dist[n][m]

def equ(l1,l2):
    return int(not l1==l2)

def correct_word(new,words):
    words=eff_heuristic(new,words)
    print(len(words))
    dist=[lev(new,word_i) for word_i in words] 
    index=np.argmin(dist)
    return words[index]

def eff_heuristic(new,words,fact=0.5):
    def prop(word_i):
        return float(len(word_i))/float(len(new))
    new_words=[word_i for word_i in words
                   if prop(word_i)>0.5 and prop(word_i)<1.5]
    return new_words

def curry_correct(words):
    return lambda new:correct_word(new,words)

if __name__ == "__main__":
    print(lev("kot","kot"))
    print(lev("kot","kod"))
    print(lev("telefon","telegraf"))
