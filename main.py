import networkx as nx
import matplotlib.pyplot as plt

from common import *
import solver
import visualizer

edge_list = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]
G = nx.Graph()
G.add_edges_from(edge_list)
for node in G.nodes:
    for attribute, value in DEFAULT_NODE_ATTRIBUTE_VALUES.items():
        G.nodes[node][attribute] = value
for edge in G.edges:
    for attribute, value in DEFAULT_EDGE_ATTRIBUTE_VALUES.items():
        G.edges[edge][attribute] = value

# visualizer.draw_graph(G)
# plt.show()

color_order = ('r', 'g', 'b')
solutions = solver.find_solutions(G, color_order=color_order, node_output_type=solver.NodeOutputType.NODES_ONLY, show_backtracking_process=False)
print("Solutions:")
print(*solutions, sep='\n')

visualizer.animate_backtracking(G, color_order=color_order, interval=1/12 * 1000, valid_solution_pause_time_ms=1000)
