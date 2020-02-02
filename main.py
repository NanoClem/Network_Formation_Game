import networkx as nx
import matplotlib.pyplot as plt
from random import random
import json

from graphs import MyRandomGraph
from graphs import EmptyGraph

from nodes import Node
from nodes.strategies import MaxScoreStrategy
from nodes.strategies import RandomStrategy

from games import SimpleFormationGame




def play(game, nbturns):
    """ Play a game with a given graph, composed by nodes with their own strategy \n
    Games available : "simple", "bad_karma"

    Parameters
    ------
    game (AbstractGame) : game which should be played

    Returns
    -----
    Resulting game ranking (nbunch)
    """
    game.start(nbturns)



def printResults(game):
    """
    """
    # RESULTS
    scores  = game.getGraph().nodes(data=True)
    ranking = game.getRanking()
    edges   = game.getGraph().edges(data=True)
    
    # PRINT
    print("\nGRAPH")
    print( "{} \n".format(nx.info(game.getGraph())) )
    print("NODES")
    print( "{} \n".format(scores) )
    print("RANKING")
    print( "{} \n".format(ranking) )
    print("EDGES")
    print("{} \n".format(edges) )



def plotResults(graph):
    """ Plot the resulting graph

    Parameters
    -----
    graph (nx.Graph) : the graph to plot
    """
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()



def simple_formation_simulation(n):
    """ Start a simulation of SimpleFormationGame, where nodes connect to those who will maximize their value.

    (int) n : number of nodes
    """
    nodes = [Node(i, MaxScoreStrategy()) for i in range(n)]
    graph = EmptyGraph(nodes, "Max score startegy simulation")
    game = SimpleFormationGame(graph)

    play(game, 1)
    printResults(game)
    plotResults(game.getGraph())
    return game.getRanking(), game.getGraph()



def realistic_formation_simulation():
    """
    """
    pass



def karma_formation_simulation():
    """
    """
    pass

    


if __name__ == "__main__":
   
    # GRAPH
    n = 5
    p = 0.8
    nbturns = 1

    # GRAPH
    # G = MyRandomGraph(n, p, "Random graph")
    # game  = SimpleFormationGame(G)

    # play(game, 1)
    # printResults(game)
    # plotResults(game.getGraph())

    # SIMULATIONS
    simple_formation_simulation(n)
    
     