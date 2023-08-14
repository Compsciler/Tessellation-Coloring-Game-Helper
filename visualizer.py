import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from common import *
import solver

def animate_backtracking(G, color_order=(), interval=200, valid_solution_pause_time_ms=1000):
    graphs = solver.find_solutions(G, color_order=color_order, node_output_type=solver.NodeOutputType.FULL_GRAPH, show_backtracking_process=True)
    paths = solver.find_solutions(G, color_order=color_order, node_output_type=solver.NodeOutputType.NODES_ONLY, show_backtracking_process=True)
    fig, ax = plt.subplots()
    plt.axis('off')

    solutions_count = 0

    def animate(frame_num):
        nonlocal solutions_count
        ax.clear()
        G = graphs[frame_num]
        path = paths[frame_num]
        is_valid_solution = solver.is_valid_solution(path, G)
        if is_valid_solution:
            solutions_count += 1

        draw_graph(G)
        
        plt.text(0.0, 1.0, f'Frame: {frame_num}', transform=plt.gca().transAxes, fontsize=12,
                verticalalignment='top', horizontalalignment='left', bbox=dict(facecolor='white', alpha=1.0))
        plt.text(0.0, 0.9, f'Solutions found: {solutions_count}', transform=plt.gca().transAxes, fontsize=12,
                verticalalignment='top', horizontalalignment='left', bbox=dict(facecolor='white', alpha=1.0))
        
        if is_valid_solution:
            old_interval = anim.event_source.interval
            anim.event_source.interval = valid_solution_pause_time_ms
            plt.pause(valid_solution_pause_time_ms / 1000)
            anim.event_source.interval = old_interval
        

    anim = animation.FuncAnimation(fig, animate, frames=len(graphs), interval=interval, repeat=False, blit=False)
    plt.show()

def draw_graph(G):
    def get_draw_kwargs(G):
        return {
            'with_labels': True,
            'node_color': nx.get_node_attributes(G, COLOR).values(),
            'edge_color': nx.get_edge_attributes(G, COLOR).values(),
            'width': list(nx.get_edge_attributes(G, WIDTH).values()),
        }
    
    draw_kwargs = get_draw_kwargs(G)
    nx.draw_spectral(G, **draw_kwargs)
    # if nx.is_planar(G):
    #     nx.draw_planar(G, **draw_kwargs)
    # else:
    #     nx.draw_spectral(G, **draw_kwargs)
