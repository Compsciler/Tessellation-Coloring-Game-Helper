from collections import defaultdict
import networkx as nx
import networkx.algorithms.isomorphism as iso

from common import *

nm = iso.categorical_node_match(list(DEFAULT_NODE_ATTRIBUTE_VALUES.keys()), list(DEFAULT_NODE_ATTRIBUTE_VALUES.values()))
em = iso.categorical_edge_match(list(DEFAULT_EDGE_ATTRIBUTE_VALUES.keys()), list(DEFAULT_EDGE_ATTRIBUTE_VALUES.values()))
def is_solution_isomorphic(G1, G2):
    return nx.is_isomorphic(G1, G2, node_match=nm, edge_match=em)

def get_isomorphism_counts(graphs):
    isomorphism_counts = defaultdict(int)
    for graph in graphs:
        for iso_graph in isomorphism_counts.keys():
            if is_solution_isomorphic(graph, iso_graph):
                isomorphism_counts[iso_graph] += 1
                break
        else:
            isomorphism_counts[graph] = 1
    return dict(isomorphism_counts)

# Automorphic equivalence: https://faculty.ucr.edu/~hanneman/nettext/C14_Automorphic_Equivalence.html
def get_automorphically_equivalent_nodes(G):
    isomorphic_nodes = defaultdict(list)
    G_copy1 = G.copy()
    G_copy2 = G.copy()

    for node in G.nodes():
        assert(G.nodes[node][COLOR] == DEFAULT_NODE_ATTRIBUTE_VALUES[COLOR])
        for iso_node in isomorphic_nodes.keys():
            G_copy1.nodes[node][COLOR] = 'r'
            G_copy2.nodes[iso_node][COLOR] = 'r'
            is_solution_isomorphic_ = is_solution_isomorphic(G_copy1, G_copy2)
            G_copy1.nodes[node][COLOR] = DEFAULT_NODE_ATTRIBUTE_VALUES[COLOR]
            G_copy2.nodes[iso_node][COLOR] = DEFAULT_NODE_ATTRIBUTE_VALUES[COLOR]

            if is_solution_isomorphic_:
                isomorphic_nodes[iso_node].append(node)
                break
        else:
            isomorphic_nodes[node] = [node]
    return dict(isomorphic_nodes)
