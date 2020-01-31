from .AbstractNode import AbstractNode
from .strategies import RandomStrategy



class Randomizer(AbstractNode):
    """
    """

    def __init__(self, id, p):
        """ CONSTRUCTOR

        Parameters
        -----
        p (float) : probability for the node to connect to another
        """
        super().__init__(id, RandomStrategy(p))     # init parent attributes
        self._p = p



    def isConnecting(self, nbunch, indicator = ""):
        """
        """
        return self.getStrategy().connectingDecision(self, nbunch, indicator)



    def getProbability(self):
        """ Return the probability of the node to connect

        Returns
        -----
        (float)
        """
        return self._p



    def setProbability(self, new_p):
        """ Set a new connecting probability

        Parameters
        -----
        new_p (float) : new connecting probability
        """
        self._p = new_p