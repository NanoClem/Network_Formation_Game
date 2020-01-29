import networkx as nx
import matplotlib.pyplot as plt
from random import random
import json

from graphs import MyRandomGraph
from games import SimpleFormationGame




if __name__ == "__main__":
    
    #=========================================================
    #   GRAPH
    #=========================================================
    # G = nx.Graph(title='Network formation game')
    # nbunch = ["Google", "Amazon", "Microsoft", "Pampers"]
    
    #=========================================================
    #   RANDOM GRAPH
    #=========================================================
    # GRAPH PARAMS
    n = 5
    p = 0.4
    G_rand = MyRandomGraph(n, p, "Random graph")

    # GAME
    nbturns = 1
    game    = SimpleFormationGame()
    game.start(G_rand, nbturns)

    # RESULTS
    scores  = G_rand.nodes(data=True)
    ranking = game.getRanking()
    edges   = G_rand.edges
    
    # PRINT
    print("\nGRAPH")
    print( "{} \n".format(nx.info(G_rand)) )
    print("NODES")
    print( "{} \n".format(scores) )
    print("RANKING")
    print( "{} \n".format(ranking) )
    print("EDGES")
    print("{} \n".format(edges) )
    
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
     