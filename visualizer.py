import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from common import *
import solver

def animate_backtracking(G, color_order=(), interval=200):
    graphs = solver.find_solutions(G, color_order=color_order, node_output_type=solver.NodeOutputType.FULL_GRAPH, show_backtracking_process=True)
    fig, ax = plt.subplots()
    plt.axis('off')

    anim = animation.FuncAnimation(fig, _animate, frames=len(graphs), interval=interval, repeat=False, blit=False, fargs=(graphs,))
    plt.show()

def _animate(frame_num, graphs):
    G = graphs[frame_num]
    draw_kwargs = get_draw_kwargs(G)
    if nx.is_planar(G):
        nx.draw_planar(G, **draw_kwargs)
    else:
        nx.draw_spring(G, **draw_kwargs)
    
    plt.gca().text(0.95, 0.95, f'Frame: {frame_num}', transform=plt.gca().transAxes, fontsize=12,
                verticalalignment='top', horizontalalignment='right', bbox=dict(facecolor='white', alpha=1.0))
    # Add part that increments a text box with the number of solutions found so far, and sleep for a another parameter value if this is a solution

def get_draw_kwargs(G):
    return {'with_labels': True, 'node_color': nx.get_node_attributes(G, COLOR).values()}
