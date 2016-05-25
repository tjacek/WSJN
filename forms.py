# -*- coding: utf-8 -*-
import tools

class Forms(object):
    def __init__(self,endings):
        self.endings=endings

def build_forms(begin_file,end_file):
    begin_lines=tools.read_lines(begin_file,clean_text=False)
    begin=parse_begin(begin_lines)
    end_lines=tools.read_lines(end_file,clean_text=False)
    end=parse_end(end_lines)
    print(end[begin['a']])

def parse_begin(lines):
    lines=[line_i.split(u':') for line_i in lines]
    lines=[(line_i[0],int(line_i[1])) for line_i in lines
                            if len(line_i)==2]
    return dict(lines)

def parse_end(lines):
    lines=[line_i.split(u';') for line_i in lines]
    def sub_parse(endings):
    	endings=endings.split(u':')
    	endings=[end_i for end_i in endings
    	               if len(end_i)>0]
    	return endings
    lines=[(int(line_i[0]), sub_parse(line_i[2]) ) 
                   for line_i in lines]
    return dict(lines)



build_forms(u'resources/lab2/pocz.dat',
	         u'resources/lab2/konc.dat')