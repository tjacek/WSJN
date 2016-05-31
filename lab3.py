# -*- coding: utf-8 -*-
import forms,tools
import metrics.lev as distance
import bayes
from metrics.lev import decode_digraphs

def main_loop():
    correction=bayes.build_spellchecker(u'resources/lab3/pocz.dat',u'resources/lab3/konc.dat',
    u'resources/lab3/bledy.txt',u'resources/lab3/proza.iso.utf8')
    tools.ui_loop(correction,get_word)

def get_word(correction):
    raw_text = raw_input("Enter sentences ").decode('utf-8')
    if(raw_text=="quit"):
        return False
    #new_word=distance.code_digraphs(raw_text)
    prob_pairs=correction.correct(raw_text)
    n=15
    if(len(prob_pairs)>n):
        prob_pairs=prob_pairs[0:n]
    tools.print_unicode(prob_pairs,to_unicode=lambda p: decode_digraphs(p[0]) +' ' + unicode(p[1]))
    return True
    
if __name__ == "__main__":
    main_loop()