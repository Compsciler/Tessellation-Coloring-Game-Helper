import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from common import *
from solver import Solver

edge_list = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]
G = nx.Graph()
G.add_edges_from(edge_list)
for node in G.nodes:
    for attribute, value in DEFAULT_ATTRIBUTE_VALUES.items():
        G.nodes[node][attribute] = value

draw_kwargs = {'with_labels': True, 'node_color': nx.get_node_attributes(G, COLOR).values()}
if nx.is_planar(G):
    nx.draw_planar(G, **draw_kwargs)
else:
    nx.draw_spring(G, **draw_kwargs)

plt.show()

solver = Solver(G)
solutions = solver.find_solutions(color_order=('red', 'green', 'blue'))
print("Solutions:")
print(*solutions, sep='\n')
