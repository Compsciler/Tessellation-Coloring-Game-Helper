import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from common import *
import isomorph
import solver

def animate_backtracking(G, color_order=(), interval=200, valid_solution_pause_time_ms=1000):
    graphs_and_paths = solver.find_solutions(G, color_order=color_order, node_output_type=solver.NodeOutputType.FULL_GRAPH_AND_NODE_LIST, show_backtracking_process=True)
    graphs, paths = zip(*graphs_and_paths)
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
        

    anim = animation.FuncAnimation(fig, animate, frames=len(graphs), 
                                   interval=interval, repeat=False, blit=False)
    plt.show()

# This lags the more solutions you view somehow
def show_solutions(G, color_order=(), interval=200, animate=True, remove_isomorphic_solutions=True):
    solution_path_graphs = solver.find_solutions(G, color_order=color_order, node_output_type=solver.NodeOutputType.FULL_GRAPHS_FOR_PATH, show_backtracking_process=False)
    solution_graphs = [path_graphs[-1] for path_graphs in solution_path_graphs]
    if not animate:
        solution_path_graphs = [[solution_graph] for solution_graph in solution_graphs]
    
    isomorphic_graphs = isomorph.get_isomorphic_graphs(solution_graphs)
    if remove_isomorphic_solutions:
        solution_graphs = list(isomorphic_graphs.keys())
        solution_path_graphs = [path_graphs for path_graphs in solution_path_graphs if path_graphs[-1] in solution_graphs]
        print(len(solution_graphs), len(solution_path_graphs))

    fig, ax = plt.subplots()
    plt.axis('off')

    class SolutionIndex:
        solution_index = 0
        anim = None

        def next(self, event):
            self.solution_index = (self.solution_index + 1) % len(solution_graphs)
            self.update_plot()

        def prev(self, event):
            self.solution_index = (self.solution_index - 1) % len(solution_graphs)
            self.update_plot()

        def update_plot(self):
            # plt.clf()
            self.anim = animation.FuncAnimation(fig, self.animate, frames=len(solution_graphs[self.solution_index]) + 1, 
                                                interval=interval, repeat=False, blit=False)
            plt.show()

        def animate(self, frame_num):
            # ax.clear()
            ax_graph = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax_graph.axis('off')
            draw_graph(solution_path_graphs[self.solution_index][frame_num])
            plt.text(0.0, 1.0, f'Solution number: {self.solution_index + 1}/{len(solution_graphs)}', transform=plt.gca().transAxes, fontsize=12,
                     verticalalignment='top', horizontalalignment='left', bbox=dict(facecolor='white', alpha=1.0))
            isomorphic_graph = get_key_by_list_value(isomorphic_graphs, solution_graphs[self.solution_index])
            plt.text(0.0, 0.9, f'Isomorphic solutions: {len(isomorphic_graphs[isomorphic_graph])}', transform=plt.gca().transAxes, fontsize=12,
                     verticalalignment='top', horizontalalignment='left', bbox=dict(facecolor='white', alpha=1.0))

    callback = SolutionIndex()
    
    plt.subplots_adjust(bottom=0.2)
    axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
    axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
    bnext = plt.Button(axnext, 'Next')
    bnext.on_clicked(callback.next)
    bprev = plt.Button(axprev, 'Previous')
    bprev.on_clicked(callback.prev)

    callback.update_plot()


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
