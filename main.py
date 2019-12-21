import networkx as nx
import matplotlib.pyplot as plt
import json


if __name__ == "__main__":
    
    #=========================================================
    #   GRAPH
    #=========================================================
    G = nx.Graph(title='Network formation game')
    nbunch = ["Google", "Amazon", "Microsoft", "Pampers"]

    #=========================================================
    #   EDGES
    #=========================================================
    ebunch = [
        ("Google", "Amazon",    {'weight' : 5, 'color' : 'blue'}),
        ("Google", "Microsoft", {'weight': 10, 'color' : 'orange'}),
        ("Amazon", "Microsoft", {'weight': 20, 'color' : 'white'}),
        ("Amazon", "Pampers",   {'weight': 10, 'color' : 'yellow'})
        ]

    #=========================================================
    #   OPERATIONS
    #=========================================================
    # G = nx.Graph(ebunch)
    G.add_nodes_from(nbunch)
    G.add_edges_from(ebunch)

    #=========================================================
    #   TESTS
    #=========================================================
    print("GRAPH")
    print(G.graph)
    print("EDGES")
    print( dict(G.edges.items()))
    # nx.write_gml(G, 'graph.json')

    #=========================================================
    #   DRAWING
    #=========================================================
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
     