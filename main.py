import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from common import *
from solver import Solver
from visualization import SolutionVisualizer

edge_list = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]
G = nx.Graph()
G.add_edges_from(edge_list)
for node in G.nodes:
    for attribute, value in DEFAULT_ATTRIBUTE_VALUES.items():
        G.nodes[node][attribute] = value

# draw_kwargs = SolutionVisualizer.get_draw_kwargs(G)
# if nx.is_planar(G):
#     nx.draw_planar(G, **draw_kwargs)
# else:
#     nx.draw_spring(G, **draw_kwargs)
# plt.show()

solver = Solver(G, color_order=('r', 'g', 'b'))
solutions = solver.find_solutions(node_output_type=Solver.NodeOutputType.NODES_ONLY, show_backtracking_process=False)
print("Solutions:")
print(*solutions, sep='\n')

solution_visualizer = SolutionVisualizer(solver)
solution_visualizer.animate_backtracking(interval=200)
