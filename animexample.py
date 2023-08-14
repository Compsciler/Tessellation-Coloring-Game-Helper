# Source: https://ankurankan.github.io/plotting-and-animating-networkx-graphs.html
import networkx as nx
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import random

# Graph initialization
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
G.add_edges_from([(1,2), (3,4), (2,5), (4,5), (6,7), (8,9), (4,7), (1,7), (3,5), (2,7), (5,8), (2,9), (5,7)])

# Animation function
def animate(frame_num):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']  # https://matplotlib.org/stable/gallery/color/named_colors.html
    nx.draw_circular(G, node_color=[random.choice(colors) for j in range(9)])
    # return []  # Uncomment if using blit=True

fig, ax = plt.subplots()
plt.axis('off')

# Animator call
anim = animation.FuncAnimation(fig, animate, frames=5, interval=200, blit=False)

plt.show()  # Display the animation in an interactive window
