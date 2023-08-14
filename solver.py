import networkx as nx
from enum import Enum, auto

from common import *

class NodeOutputType(Enum):
    NODES_ONLY = auto()
    NODES_WITH_COLORING = auto()
    EDGES_ONLY = auto()
    FULL_GRAPH = auto()

def find_solutions(G, color_order=(), node_output_type=NodeOutputType.NODES_ONLY, show_backtracking_process=False):
    def dfs(path, index):  # Backtracking
        is_valid_solution_ = is_valid_solution(path, G)
        if is_valid_solution_ or show_backtracking_process:
            append_solution(path)
        if is_valid_solution_:
            return

        prev_node = path[-1] if len(path) > 0 else None
        curr_color = get_current_color(index, color_order)
        for node in get_travellable_nodes(prev_node, G):
            if is_valid_next_node(node, path, color=curr_color, G=G):
                old_node_attrs = G.nodes[node].copy()
                node_attrs = get_node_attribute_dict(node, color=curr_color, G=G)

                G.nodes[node].update(node_attrs)
                path.append(node)
                if prev_node is not None:
                    edge_travelled = (prev_node, node)
                    edges_travelled.append(edge_travelled)
                    update_edge(edge_travelled, True)
                index += 1

                dfs(path, index)

                G.nodes[node].update(old_node_attrs)
                path.pop()
                if len(edges_travelled) > 0:
                    edge_removed = edges_travelled.pop()
                    update_edge(edge_removed, False)
                if show_backtracking_process:
                    append_solution(path)
                index -= 1

    def append_solution(path):
        if node_output_type == NodeOutputType.NODES_ONLY:
            solutions.append(path.copy())
        elif node_output_type == NodeOutputType.NODES_WITH_COLORING:
            solutions.append([(node, G.nodes[node][COLOR]) for node in path])
        elif node_output_type == NodeOutputType.EDGES_ONLY:
            solutions.append(edges_travelled.copy())
        elif node_output_type == NodeOutputType.FULL_GRAPH:
            solutions.append(G.copy())
    
    def update_edge(edge, is_travelled):
        edge_color = TRAVELLED_EDGE_ATTRIBUTE_VALUES[COLOR] if is_travelled else DEFAULT_EDGE_ATTRIBUTE_VALUES[COLOR]
        edge_width = TRAVELLED_EDGE_ATTRIBUTE_VALUES[WIDTH] if is_travelled else DEFAULT_EDGE_ATTRIBUTE_VALUES[WIDTH]
        G.edges[edge][COLOR] = edge_color
        G.edges[edge][WIDTH] = edge_width

    old_G = G.copy()
    index = 0
    solutions = []
    edges_travelled = []
    dfs([], index)
    G = old_G  # G should equal old_G, but just in case
    return solutions

def get_current_color(index, color_order):
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

def is_valid_next_node(node, path, G, color=None, value=None, props=()):
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
