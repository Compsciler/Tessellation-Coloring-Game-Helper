import networkx as nx
import matplotlib.pyplot as plt
import itertools
import pprint

from common import *
import isomorph
import solver
import visualizer

# edge_list = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]
# edge_list = [
#     ('00', '01'), ('01', '02'), ('02', '03'),
#     ('10', '00'), ('10', '11'), ('11', '01'), ('11', '12'), ('12', '02'), ('12', '13'), ('13', '03'),
#     ('20', '10'), ('20', '21'), ('21', '11'), ('21', '22'), ('22', '12'), ('22', '23'), ('23', '13'),
#     ('30', '20'), ('30', '31'), ('31', '21'), ('31', '32'), ('32', '22'), ('32', '33'), ('33', '23'),
# ]
# edge_list = [
#     ('00', '10'), ('10', '20'), ('20', '30'),
#     ('01', '00'), ('01', '11'), ('11', '10'), ('11', '21'), ('21', '20'), ('21', '31'), ('31', '30'),
#     ('02', '01'), ('02', '12'), ('12', '11'), ('12', '22'), ('22', '21'), ('22', '32'), ('32', '31'),
#     ('03', '02'), ('03', '13'), ('13', '12'), ('13', '23'), ('23', '22'), ('23', '33'), ('33', '32'),
# ]

# Axial coordinates: https://www.redblobgames.com/grids/hexagons/#coordinates-axial
# edge_list = [('0 0', '0 1'), ('0 0', '1 -1'), ('0 1', '1 0'), ('0 1', '1 -1'), ('0 1', '1 1'), ('1 -1', '1 0'), ('1 -1', '2 -2'), ('1 0', '2 -1'), ('1 0', '1 1'), ('1 1', '2 0'), ('1 1', '2 1'), ('2 -2', '2 -1'), ('2 -1', '2 0'), ('2 0', '2 1')]
# edge_list = [
#     ('O', 'A1'), ('O', 'B1'), ('O', 'C1'), ('O', 'D1'), ('O', 'E1'), ('O', 'F1'),
#     ('A1', 'B1'), ('B1', 'C1'), ('C1', 'D1'), ('D1', 'E1'), ('E1', 'F1'), ('F1', 'A1'),
# ]
edge_list = [
    ('O', 'A1'), ('O', 'C1'), ('O', 'E1'), ('O', 'G1'), ('O', 'I1'), ('O', 'K1'),
    ('A1', 'C1'), ('C1', 'E1'), ('E1', 'G1'), ('G1', 'I1'), ('I1', 'K1'), ('K1', 'A1'),
    
    ('A2', 'A1'), ('A2', 'B2'), ('B2', 'A1'), ('B2', 'C1'), ('B2', 'C2'),
    ('C2', 'C1'), ('C2', 'D2'), ('D2', 'C1'), ('D2', 'E1'), ('D2', 'E2'),
    ('E2', 'E1'), ('E2', 'F2'), ('F2', 'E1'), ('F2', 'G1'), ('F2', 'G2'),
    ('G2', 'G1'), ('G2', 'H2'), ('H2', 'G1'), ('H2', 'I1'), ('H2', 'I2'),
    ('I2', 'I1'), ('I2', 'J2'), ('J2', 'I1'), ('J2', 'K1'), ('J2', 'K2'),
    ('K2', 'K1'), ('K2', 'L2'), ('L2', 'K1'), ('L2', 'A1'), ('L2', 'A2'),
]

G = nx.Graph()
G.add_edges_from(edge_list)
for node in G.nodes:
    for attribute, value in DEFAULT_NODE_ATTRIBUTE_VALUES.items():
        G.nodes[node][attribute] = value
for edge in G.edges:
    for attribute, value in DEFAULT_EDGE_ATTRIBUTE_VALUES.items():
        G.edges[edge][attribute] = value

automorphically_equivalent_nodes = isomorph.get_automorphically_equivalent_nodes(G)

# visualizer.draw_graph(G)
# plt.show()

color_order = ('r', 'g', 'b')
# color_order = ('1', '2', '3', '4', '2', '3')
solutions = solver.find_solutions(G, color_order=color_order, node_output_type=solver.NodeOutputType.FULL_GRAPH, 
                                  show_backtracking_process=False, start_nodes=automorphically_equivalent_nodes.keys())
print("Solutions:")
print(*solutions, sep='\n')

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(isomorph.get_isomorphism_counts(solutions))

visualizer.animate_backtracking(G, color_order=color_order, interval=1/60 * 1000, valid_solution_pause_time_ms=1000)
