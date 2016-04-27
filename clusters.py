import numpy as np
#import np.random from  randint

def naive_clusters(lines,metric,eps=10.0):
    print(len(lines))
    line_j=lines[0]
    cluster_j=[]
    for line_i in lines:
        dst_ij=metric(line_i,line_j)
        if(dst_ij<eps):
            print("OK")
            cluster_j.append(dst_ij)
        print(dst_ij)

    