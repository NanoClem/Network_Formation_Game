from .AbstractStrategy import AbstractStrategy
from random import random



class MaxScoreStrategy(AbstractStrategy):
    """
    """

    def connectingDecision(self, node, nbunch):
        """ Decides to connect to a node in order to maximize its final score.

        Parameters
        -----
        node (AbstractNode) : node which apply the strategy
        nbunch (list) : nodes which are tested for connection
        indicator (string) : node attribute on which the test is based 

        Returns
        -----
        (ebunch) The differents connections the node decided to make \n
        (ebunch) The differents defections the node decided to make
        """
        # INIT
        connections, defections = [], []
        sortedNodes = sorted(nbunch, key=lambda tup: tup[1], reverse = True)    # ascending sort based on the 

        # CONNECTIONS
        ##TODO : Choose randomly if there is equality
        connections.append( (node, sortedNodes.pop(0)[0] ))  # pop and append the best element

        # DEFECTIONS
        for n in sortedNodes:
            defections.append( (node, n[0]) )  # left elements are not considered worthy

        return connections, defections