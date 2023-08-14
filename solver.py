import networkx as nx
from enum import Enum, auto

from common import *

class Solver:
    def __init__(self, G, color_order=()):
        self.G = G
        self.color_order = color_order

    class NodeOutputType(Enum):
        NODES_ONLY = auto()
        NODES_WITH_COLORING = auto()
        FULL_GRAPH = auto()

    def find_solutions(self, node_output_type=NodeOutputType.NODES_ONLY, show_backtracking_process=False):
        def dfs(path):  # Backtracking
            nonlocal index
            is_valid_solution = self.is_valid_solution(path)
            if is_valid_solution or show_backtracking_process:
                if node_output_type == self.NodeOutputType.NODES_ONLY:
                    solutions.append(path.copy())
                elif node_output_type == self.NodeOutputType.NODES_WITH_COLORING:
                    solutions.append([(node, self.G.nodes[node][COLOR]) for node in path])
                elif node_output_type == self.NodeOutputType.FULL_GRAPH:
                    solutions.append(self.G.copy())
            if is_valid_solution:
                return

            prev_node = path[-1] if len(path) > 0 else None
            curr_color = self.get_current_color(index)
            for node in self.get_travellable_nodes(prev_node):
                if self.is_valid_next_node(node, path, color=curr_color):
                    old_node_attrs = self.G.nodes[node].copy()
                    node_attrs = self.get_node_attribute_dict(node, color=curr_color)

                    self.G.nodes[node].update(node_attrs)
                    path.append(node)
                    index += 1

                    dfs(path)

                    self.G.nodes[node].update(old_node_attrs)
                    path.pop()
                    if show_backtracking_process:
                        if node_output_type == self.NodeOutputType.NODES_ONLY:
                            solutions.append(path.copy())
                        elif node_output_type == self.NodeOutputType.NODES_WITH_COLORING:
                            solutions.append([(node, self.G.nodes[node][COLOR]) for node in path])
                        elif node_output_type == self.NodeOutputType.FULL_GRAPH:
                            solutions.append(self.G.copy())
                    index -= 1

        old_G = self.G.copy()
        index = 0
        solutions = []
        dfs([])
        self.G = old_G  # G should equal old_G, but just in case
        return solutions

    def get_current_color(self, index):
        if self.color_order == ():
            return None
        return self.color_order[index % len(self.color_order)]

    def get_node_attribute_dict(self, node, color=None, value=None, props=None):
        attribute_dict = self.G.nodes[node].copy()
        if color is not None:
            attribute_dict[COLOR] = color
        if value is not None:
            attribute_dict[VALUE] = value
        if props is not None:
            attribute_dict[PROPS] = props
        return attribute_dict

    def is_valid_next_node(self, node, path, color=None, value=None):
        if node in path:
            return False
        if color is not None:
            adjacent_nodes_of_color = [node for node in self.G.neighbors(node) if self.G.nodes[node][COLOR] == color]
            return len(adjacent_nodes_of_color) == 0
        return True

    def get_travellable_nodes(self, node):  # Function in case you can travel to non-adjacent nodes
        if node is None:
            return self.G.nodes()
        return self.G.neighbors(node)  # Changed from self.G.adj[node]

    def is_valid_solution(self, path):  # Function in case you don't need to visit all nodes
        return len(path) == len(self.G.nodes)
