import numpy as np

def check_numpy(func):
    def inner_func(text1,text2):
        assert_np(text1)
        assert_np(text2)
        return func(text1,text2)
    return inner_func

def assert_np(vect):
    assert(type(vect)==np.ndarray)

@check_numpy
def l1(text1,text2):
    return np.linalg.norm((text1 - text2), ord=1)

@check_numpy
def l2(text1,text2):
    return np.linalg.norm((text1 - text2), ord=2)

@check_numpy
def l_inf(text1,text2):
    return np.linalg.norm((text1 - text2), ord=np.inf)

@check_numpy
def cos_metric(text1,text2):
    cs=np.dot(text1,text2)
    cs/=np.dot(text1,text1)*np.dot(text1,text1)
    return 1.0 - cs

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