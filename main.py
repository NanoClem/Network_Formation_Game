import networkx as nx
import matplotlib.pyplot as plt
from random import random
import json

from graphs import MyRandomGraph




if __name__ == "__main__":
    
    #=========================================================
    #   GRAPH
    #=========================================================
    # G = nx.Graph(title='Network formation game')
    # nbunch = ["Google", "Amazon", "Microsoft", "Pampers"]
    
    #=========================================================
    #   RANDOM GRAPH
    #=========================================================
    # PARAMS
    n = 3
    p = 0.1
    G_rand = MyRandomGraph(n, p)
    
    # PRINT
    print("GRAPH")
    print(G_rand.nodes)
    print("EDGES")
    print( dict(G_rand.edges.items()))
    
    # DRAW
    nx.draw(G_rand, with_labels=True, font_weight='bold')
    plt.show()

    #=========================================================
    #   EDGES
    #=========================================================
    # ebunch = [
    #     ("Google", "Amazon",    {'weight' : 5, 'color' : 'blue'}),
    #     ("Google", "Microsoft", {'weight': 10, 'color' : 'orange'}),
    #     ("Amazon", "Microsoft", {'weight': 20, 'color' : 'white'}),
    #     ("Amazon", "Pampers",   {'weight': 10, 'color' : 'yellow'})
    #     ]

    #=========================================================
    #   OPERATIONS
    #=========================================================
    # G = nx.Graph(ebunch)
    # G.add_nodes_from(nbunch)
    # G.add_edges_from(ebunch)

    #=========================================================
    #   TESTS
    #=========================================================
    # print("GRAPH")
    # print(G.graph)
    # print("EDGES")
    # print( dict(G.edges.items()))
    # nx.write_gml(G, 'graph.json')

    #=========================================================
    #   DRAWING
    #=========================================================
    # nx.draw(G, with_labels=True, font_weight='bold')
    # plt.show()
     