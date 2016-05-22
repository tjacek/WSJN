# -*- coding: utf-8 -*-
import tools
import metrics.lev as distance

FORMS_SOURCE="resources/formy.utf8"

def main(new_word):
    words=tools.read_lines(FORMS_SOURCE,clean_text=False)
    correct_word=distance.curry_correct(words)
    print(correct_word(new_word))

if __name__ == "__main__":
    new_word="zolc".decode('utf-8')
    main(new_word)