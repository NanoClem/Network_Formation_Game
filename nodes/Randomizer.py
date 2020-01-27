from .AbstractNode import AbstractNode
from .strategies import RandomStrategy



class Randomizer(AbstractNode):
    """
    """

    def __init__(self, p):
        """ CONSTRUCTOR

        Parameters:
        -----
        p (float) : probability for the node to connect to another
        """
        self.setStrategy( RandomStrategy(p) )