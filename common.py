from collections import defaultdict
import networkx as nx
import networkx.algorithms.isomorphism as iso

"""
color: node color string
val: node additional value (such as a number or letter)
props: tuple of special node properties
"""
COLOR = 'color'
VALUE = 'value'
PROPS = 'props'

DEFAULT_NODE_ATTRIBUTE_VALUES = {
    COLOR: 'lightgray',  # Uncolored color, can color over
    VALUE: None, 
    PROPS: (),
}


WIDTH = 'width'

DEFAULT_EDGE_ATTRIBUTE_VALUES = {
    COLOR: 'gray',
    WIDTH: 1.0,
}
TRAVELLED_EDGE_ATTRIBUTE_VALUES = {
    COLOR: 'black',
    WIDTH: 3.0,
}

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
