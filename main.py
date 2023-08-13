import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Node:
    default_color = 'white'
    
    """
    key: unique name shown in the graph
    color: node color string
    val: node additional value (such as a number or letter)
    props: tuple of special node properties
    """
    def __init__(self, key, color=default_color, val=None, props=()):
        self.key = key
        self.color = color
        self.val = val
        self.props = props
    
    def __str__(self):
        return str(self.key)
    
    # These allow edges_keys_to_nodes to use node keys as keys
    def __hash__(self):
        return hash(self.key)
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.key == other.key
        return False
    
    @staticmethod
    def edge_list_keys_to_nodes(edges):
        return [Node.edge_key_to_nodes(edge) for edge in edges]
    @staticmethod
    def edge_key_to_nodes(edge):
        return (Node(edge[0]), Node(edge[1]))

edge_key_list = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
edge_list = Node.edge_list_keys_to_nodes(edge_key_list)
G = nx.Graph()
G.add_edges_from(edge_list)

if nx.is_planar(G):
    nx.draw_planar(G, with_labels=True)
else:
    nx.draw_spring(G, with_labels=True)

plt.show()
