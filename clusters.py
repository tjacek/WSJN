# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np
import tools,ngrams,metrics
 
def clustering(filename):
    lines=tools.read_lines(filename,clean_text=True)
    text=" ".join(lines)
    ngram_metric=ngrams.make_ngram_metric(text,n=2)
    return cluster_lines(lines,metric=ngram_metric)
    
def read_clusters(filename):
    txt=tools.read_text(filename,clean_txt=False)
    raw_clusters=txt.split("##########")
    clusters=[parse_clusters(raw_i) for raw_i in raw_clusters]
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
    #print(save_cluster(clusters))
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

def save_cluster(clusters):
    txt='##########'
    for cluster_i in clusters:
        cls_txt='##########\n'
        for line_i in cluster_i:
            cls_txt+=line_i+'\n'
        txt+=cls_txt
    return txt 

def trivial_metric(word1,word2):
    return float(abs(len(word1)-len(word2)))