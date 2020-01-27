from .AbstractNode import AbstractNode
from .strategies import MaxScoreStrategy



class Maximizer(AbstractNode):
    """
    """

    def __init__(self):
        """
        """
        self.setStrategy( MaxScoreStrategy() )