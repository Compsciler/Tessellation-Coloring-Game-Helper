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

DEFAULT_ATTRIBUTE_VALUES = {
    COLOR: 'lightgray',  # Uncolored color, can color over
    VALUE: None, 
    PROPS: (),
}

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


def find_solutions(G, color_order=()):
    def dfs(path):
        nonlocal index
        if is_valid_solution(path, G):
            solutions.append(path.copy())
            return

        prev_node = path[-1] if len(path) > 0 else None
        curr_color = get_current_color(index, color_order, G)
        for node in get_travellable_nodes(prev_node, G):
            if is_valid_next_node(node, path, G, color=curr_color):
                old_node_attrs = G.nodes[node].copy()
                node_attrs = get_node_attribute_dict(node, G, color=curr_color)
                G.nodes[node].update(node_attrs)
                path.append(node)
                index += 1
                dfs(path)
                G.nodes[node].update(old_node_attrs)
                path.pop()
                index -= 1

    index = 0
    solutions = []
    dfs([])
    return solutions

def get_current_color(index, color_order, G):
    if color_order == ():
        return None
    return color_order[index % len(color_order)]

def get_node_attribute_dict(node, G, color=None, value=None, props=None):
    attribute_dict = G.nodes[node].copy()
    if color is not None:
        attribute_dict[COLOR] = color
    if value is not None:
        attribute_dict[VALUE] = value
    if props is not None:
        attribute_dict[PROPS] = props
    return attribute_dict

def is_valid_next_node(node, path, G, color=None, value=None):
    if node in path:
        return False
    if color is not None:
        adjacent_nodes_of_color = [node for node in G.neighbors(node) if G.nodes[node][COLOR] == color]
        return len(adjacent_nodes_of_color) == 0
    return True

def get_travellable_nodes(node, G):  # Function in case you can travel to non-adjacent nodes
    if node is None:
        return G.nodes()
    return G.neighbors(node)  # Changed from G.adj[node]

def is_valid_solution(path, G):  # Function in case you don't need to visit all nodes
    return len(path) == len(G.nodes)

solutions = find_solutions(G, color_order=('red', 'blue', 'green'))
print(solutions)
