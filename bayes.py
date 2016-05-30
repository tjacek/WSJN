# -*- coding: utf-8 -*-
import tools,histogram
import metrics.lev as distance

class CondProb(object):
    def __init__(self, model,priori):
        self.model=model
        self.priori=priori
		
def build_cond_p(model_path,priori_path):
    model=build_distance_histogram(model_path)
    priori=histogram.build_word_histogram(priori_path)
    return CondProb(model,priori)

def build_distance_histogram(filename):
    pairs=tools.read_pairs(filename)
    dist=[normalized_lev(word1,word2)
             for word1,word2 in pairs]
    return histogram.build_histogram(dist)

def normalized_lev(word1,word2):
    return int(4.0*distance.lev_cxt(word1,word2))

hist=build_cond_p('resources/lab3/bledy.txt','resources/lab3/proza.iso.utf8')
#print(hist.words.keys())