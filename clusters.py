# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np
import tools,ngrams,metrics
 
def clustering(filename):
    lines=tools.read_lines(filename,clean_text=True)
    text=" ".join(lines)
    ngram_dict=ngrams.make_ngram_dict(text,create_hist=False,n=2)
    vectors=[ ngram_dict.get_histogram(line_i) for line_i in lines]
    cluster_lines(vectors)

def read_clusters(filename):
    txt=tools.read_text(filename,clean_txt=False)
    raw_clusters=txt.split("##########")
    clusters=[parse_clusters(raw_i) for raw_i in raw_clusters]
    print(len(raw_clusters))
    return clusters

def parse_clusters(raw_cluster):
    lines=raw_cluster.split('\n')
    cluster=filter(lambda line_i:len(line_i)>0,lines)
    return cluster

def cluster_lines(lines,metric=metrics.l2,eps=0.1):
    clusters=[]
    unclustered=lines
    while(len(unclustered)!=0):
        print(len(unclustered))
        cluster,outside=get_cluster(unclustered[0],unclustered,metric,eps)
        unclustered=outside
        clusters.append(cluster)
    print(len(clusters))
    return clusters
    
def get_cluster(cls_center,lines,metric,eps=10.0):
    inside=[]
    outside=[]
    for line_i in lines:
        #print(line_i)
        if(metric(cls_center,line_i)<eps):
            inside.append(line_i)
        else:
            outside.append(line_i)
    return inside,outside

def trivial_metric(word1,word2):
    return float(abs(len(word1)-len(word2)))

LINES_FILE=u'resources/lab4/lines.txt'
CLUSTER_FILE=u'resources/lab4/clusters.txt'
#clustering(LINES_FILE)
read_clusters(CLUSTER_FILE)