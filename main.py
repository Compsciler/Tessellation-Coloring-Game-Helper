import networkx as nx

from common import *
import solver
import visualizer

edge_list = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]
G = nx.Graph()
G.add_edges_from(edge_list)
for node in G.nodes:
    for attribute, value in DEFAULT_ATTRIBUTE_VALUES.items():
        G.nodes[node][attribute] = value

# draw_kwargs = visualizer.get_draw_kwargs(G)
# if nx.is_planar(G):
#     nx.draw_planar(G, **draw_kwargs)
# else:
#     nx.draw_spring(G, **draw_kwargs)
# plt.show()

color_order = ('r', 'g', 'b')
solutions = solver.find_solutions(G, color_order=color_order, node_output_type=solver.NodeOutputType.NODES_ONLY, show_backtracking_process=False)
print("Solutions:")
print(*solutions, sep='\n')

visualizer.animate_backtracking(G, color_order=color_order, interval=200)
