import numpy as np
import ngrams,tools,metrics
import cmd

def knn(vect,dataset,metric):
    inst=[(cat_i,metric(vect,vec_i))
             for cat_i,vec_i in dataset]    
    distances=[ dist_i for cat_i,dist_i in inst]
    cats=[cat_i for cat_i,dist_i in inst]
    distances=np.array(distances)
    i=np.argmin(distances)
    return cats[i]

dataset=tools.read_dataset("lang")
ngram_dict,hist_dataset=ngrams.dataset2ngrams(dataset,2)
vec=hist_dataset.pop(0)
print(knn(vec[1],hist_dataset,metrics.l2))
#input_var = raw_input("Enter sentences ")
#print(input_var)