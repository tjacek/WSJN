import numpy as np

class TrivialMC(object):
	def __init__(self,states,alphabet="qwertyuiopasdfghjklzxcvbnm"):
		self.alphabet=alphabet
		self.states = states

    def generate(self,cxt):
        if(cxt in self.states):
        	ngram=self.states[ctx]
            return self.sample(ngram)
        else:
        	n=len(self.alphabet)
            return np.random.random_integers(0,n)