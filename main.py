import networkx as nx
import matplotlib.pyplot as plt
from random import random
import json

from graphs import MyRandomGraph
from games import SimpleFormationGame




def play(game, graph, nbturns):
    """ Play a game with a given graph, composed by nodes with their own strategy \n
    Games available : "simple", "bad_karma"

    Parameters
    ------
    game (AbstractGame) : game which should be played
    graph (AbstractGraph) : graph to play with

    Returns
    -----
    Resulting game ranking (nbunch)
    """
    #=========================================================
    #   SOME INIT SETTINGS
    #=========================================================

    #=========================================================
    #   PLAY
    #=========================================================
    game.start(graph, nbturns)

    #=========================================================
    #   RESULTS
    #=========================================================
    scores  = graph.nodes(data=True)
    ranking = game.getRanking()
    edges   = graph.edges
    
    #=========================================================
    #   PRINT
    #=========================================================
    print("\nGRAPH")
    print( "{} \n".format(nx.info(graph)) )
    print("NODES")
    print( "{} \n".format(scores) )
    print("RANKING")
    print( "{} \n".format(ranking) )
    print("EDGES")
    print("{} \n".format(edges) )
    
    return ranking



def showResults(graph):
    """ Plot the resulting graph

    Parameters
    -----
    graph (nx.Graph) : the graph to plot
    """
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()

    


if __name__ == "__main__":
    
    # GRAPH
    n = 5
    p = 0.4
    nbturns = 1

    # GAME ELEMENTS
    G_rand = MyRandomGraph(n, p, "Random graph")
    game   = SimpleFormationGame()

    # PLAY
    results = play(game, G_rand, nbturns)
    showResults(G_rand)
    
     