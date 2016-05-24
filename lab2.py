# -*- coding: utf-8 -*-
import tools
import metrics.lev as distance

FORMS_SOURCE="resources/formy.utf8"

def main(new_word):
    words=tools.read_lines(FORMS_SOURCE,clean_text=False)
    #words=distance.eff_heuristic(new_word,words)
    correct_word=distance.curry_correct(words)
    print(correct_word(new_word))

def main_loop():
    full_words=tools.read_lines(FORMS_SOURCE,clean_text=False)
    words=[distance.code_digraphs(word_i) 
            for word_i in full_words]
    correct_word=distance.curry_correct(words,full_words)
    tools.ui_loop(correct_word,get_word)

def get_word(correct_word):
    raw_text = raw_input("Enter sentences ").decode('utf-8')
    if(raw_text=="quit"):
        return False
    print(correct_word(raw_text))
    return True
    
if __name__ == "__main__":
    #new_word=u'chak'
    main_loop()
    #print(distance.lev_cxt(u'?ak',u'?a'))
    #print(distance.lev_cxt(u'?ak',u'hak'))
    #print(distance.lev_cxt(u'?ak',u'?ał'))