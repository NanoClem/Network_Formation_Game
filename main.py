import networkx as nx
import matplotlib.pyplot as plt
from random import random
import json



def random_graph(n, p):
    """ Create a random graph where each node have a probability to connect to any other
    """
    nbunch  = [i for i in range(n)]   # graph nodes
    ebunch  = []                      # graph edges
    randnum = 0                       # randomly generated number (between 0 and 1 included)
    temp    = nbunch                  # temporary stock nodes without the current one to avoid self-connection
    G = nx.Graph()
    G.add_nodes_from(nbunch)         # add our nodes to the graph
    
    for node in list(G.nodes):
        temp.remove(node)         # removing current node
        for ni in temp:
            randnum = random()
            if randnum <= p:
                ebunch.append( (node, ni) )     # add new connexion to ebunch 
        temp.append(node)                          # get current node back
    
    G.add_edges_from(ebunch)
    return G



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
    G_rand = random_graph(n, p)
    
    # PRINT
    print("GRAPH")
    print(G_rand.graph)
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
     