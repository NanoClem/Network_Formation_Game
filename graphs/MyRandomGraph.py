from random import random
from .AbstractGraph import AbstractGraph
from nodes.strategies import RandomStrategy
from nodes import Node



class MyRandomGraph(AbstractGraph):
    """
    This class represents a random graph where each node have 
    a given probability to connect to any other.
    """
    
    def __init__(self, n, p, title=None):
        """ Initialise a random graph with nodes and a probability for them to connect
        
        Parameters
        -----
            (int) n   : number of nodes
            (float) p : probability of a node to connect with another
        """
        super().__init__(title)     # parent constructor
        self.n = n
        self.p = p
        self.setup()



    def setup(self, nbunch = None):
        """
        """
        nbunch  = [Node(i, RandomStrategy(self.p)) for i in range(self.n)]    # create nodes with a random strategy
        self.add_nodes_from(nbunch)



    def getProbability(self):
        """ Return the chance a node has to connect to another

        Returns
        -----
        (float) : probability of connection
        """
        return self.p