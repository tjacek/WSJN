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

if __name__ == "__main__":
    print(lev("kot","kot"))
    print(lev("kot","kod"))
    print(lev("telefon","telegraf"))
