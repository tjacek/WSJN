import sys
import graphviz as gv

class SemEdge(object):
    def __init__(self,e_a,e_b,w):
        self.a=e_a
        self.b=e_b
        self.w=w

    def __str__(self):
        return self.a +"->" + self.b 

def graph_viz(path):
    edges=parse_edges(path)
    graph=create_graph(edges)
    filename = graph.render(filename="a")

def create_graph(edges):
    g1 = gv.Graph(format='svg')
    g1.node(edges[0].a)
    for edge in edges:
        print(edge.b)
        g1.node(edge.b)
        g1.edge(edge.a,edge.b)
    return g1

def parse_edges(path):
    name=get_name(path)
    raw=read_file(path)
    def parse_line(line):
        line=line.split(",")
        line[1]=line[1].strip()
        return SemEdge(name,line[1],int(line[0]))
    return [parse_line(line) for line in raw ]

def read_file(path):
    file_object = open(path,'r')
    lines=file_object.readlines()  
    file_object.close()
    return lines

def get_name(path):
    return path.replace(".csv","")

if __name__ == "__main__":
    graph_viz(sys.argv[1])
