import numpy as np
#import np.random from  randint

def cluster_lines(lines,metric,eps=10.0):
	clusters=[]
    outside=lines
    while(len(outside)!=0):
    	 inside,outside=get_cluster(outside[0],lines,metric,eps)
         clusters.append(inside)
    return clusters
    
def get_cluster(cls_center,lines,metric,eps=10.0):
    inside=[]
    outside=[]
    for line_i in lines:
    	if(metric(cls_center,line_i)<eps):
    	    inside.append(line_i)
        else:
            outside.append(line_i)
    return inside,outside