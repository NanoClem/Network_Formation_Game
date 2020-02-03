from .AbstractStrategy import AbstractStrategy
from random import random



class RandomStrategy(AbstractStrategy):
    """
    """
    
    def __init__(self, p):
        """
        """
        self._p = p



    def connectingDecision(self, node, nbunch):
        """ Random connection to nodes

        Parameters
        -----
        node (AbstractNode) : node which apply the strategy
        nbunch (list) : nodes which are tested for connection

        Returns
        -----
        (ebunch) The differents connections the node decided to make \n
        (ebunch) The differents defections the node decided to make
        """
        connections, defections = [], []
        for n in nbunch:
            randnum = random()
            if randnum <= self._p:
                connections.append( (node, n[0]) )
            else:
               defections.append( (node, n[0]) ) 
        
        return connections, defections