from random import random
from .AbstractGraph import AbstractGraph
from nodes import Node
from nodes.strategies import AbstractStrategy



class EmptyGraph(AbstractGraph):
    """
    This class represents an empty graph without nodes or edges
    """
    

    def __init__(self, nbunch, title = None):
        """ Initialise a random graph with nodes and a probability for them to connect
        
        Parameters
        -----
            (list) nbunch : nodes composing the graph
        """
        super().__init__(title)     # parent constructor
        self.setup(nbunch)



    def setup(self, nbunch):
        """
        """
        self.add_nodes_from(nbunch)