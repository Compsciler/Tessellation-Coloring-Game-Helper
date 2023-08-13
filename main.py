import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
color: node color string
val: node additional value (such as a number or letter)
props: tuple of special node properties
"""
COLOR = 'color'
VALUE = 'value'
PROPS = 'props'

DEFAULT_COLOR = 'lightgray'  # Uncolored color, can color over

edge_list = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
G = nx.Graph()
G.add_edges_from(edge_list)
nx.set_node_attributes(G, DEFAULT_COLOR, COLOR)

draw_kwargs = {'with_labels': True, 'node_color': nx.get_node_attributes(G, COLOR).values()}
if nx.is_planar(G):
    nx.draw_planar(G, **draw_kwargs)
else:
    nx.draw_spring(G, **draw_kwargs)

plt.show()
