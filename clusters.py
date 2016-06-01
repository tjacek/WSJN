# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np
import tools,ngrams,metrics
from sets import Set

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
    cls_sep='\n##########\n'
    clusters=['\n'.join(cluster_i) for cluster_i in clusters]
    txt=cls_sep.join(clusters)
    return txt 

def clusters_to_sets(clusters):
    sets={}
    for cluster_i in clusters:
        cls_set=Set(cluster_i)
        for line_i in cls_set:
            sets[line_i]=cls_set
    return sets   

def cluster_quality(cls_sets1,cls_sets2):
    results=[]
    for line_i in cls_sets1:
        if not cls_sets2.has_key(line_i):
            results.append([0.0,0.0,0.0])
        else:
            result_i=quality_metrics(cls_sets1[line_i], cls_sets2[line_i])
            results.append(result_i)
    size=float(len(results))
    results=np.array(results,dtype=float)
    print(results.shape)
    quality_total=np.sum(results,axis=0)/size
    print(quality_total)
    return quality_total

def quality_metrics(norm, answer):
    common_positive = norm.intersection(answer)
    print(common_positive)
    precision = float(len(common_positive)) / len(answer)
    recall = float(len(common_positive)) / len(norm)
    f_score=2.0 * (precision * recall) / (precision + recall)
    return [precision,recall,f_score]

def trivial_metric(word1,word2):
    return float(abs(len(word1)-len(word2)))