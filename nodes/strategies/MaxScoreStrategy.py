from .AbstractStrategy import AbstractStrategy
from random import random



class MaxScoreStrategy(AbstractStrategy):
    """
    """

    def connectingDecision(self, node, nbunch, indicator = ""):
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
        pass