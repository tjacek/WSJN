def lev_cont(word1,word2):
    n=len(word1)
    m=len(word2)
    dist=np.zeros((n,m))
    for i in range(n):
        dist[i][0]=i 
    for j in range(m):
        dist[0][j]=j
    for i in range(1,n):
        for j in range(1,m):
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
    dist=np.zeros((n,m))
    for i in range(n):
        dist[i][0]=i 
    for j in range(m):
        dist[0][j]=j
    for i in range(1,n):
        for j in range(1,m):
            l1=dist[i-1][j]+1
            l2=dist[i][j-1]+1
            l3=dist[i-1][j-1]+equ(word1[i],word2[j])
            dist[i][j]=min([l1,l2,l3])
    return dist[n-1][m-1]

def equ(l1,l2):
    return int(not l1==l2)

def correct_word(new,words):
    dist=[lev(new,word_i) for word_i in words] 
    index=np.argmax(dist)
    return dist[index]

def curry_correct(words):
    return lambda new:correct_word(new,words)

if __name__ == "__main__":
    print(lev("kot","kot"))
    print(lev("kot","kod"))
    print(lev("telefon","telegraf"))
