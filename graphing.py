import pygraphviz as pgv

G=pgv.AGraph()

G.add_node('a') # adds node 'a'
G.add_edge('a','b') # adds edge 'b'-'c' (and also nodes 'b', 'c')
G.add_edge('a', 'c')
G.add_edge('b', 'd')
G.add_edge('b', 'e')

G.layout()
G.draw('output.png')