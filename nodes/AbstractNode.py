from abc import ABC, abstractmethod
from .strategies import AbstractStrategy



class AbstractNode(ABC):
    """
    """

    @abstractmethod
    def __init__(self, strategy : AbstractStrategy):
        self._strategy = strategy



    @abstractmethod
    def isConnecting(self):
        raise NotImplementedError



    def getStrategy(self) -> AbstractStrategy:
        """ Returns the node current strategy

        Returns
        -----
        Node current strategy
        """
        return self._strategy



    def setStrategy(self, new_strategy : AbstractStrategy):
        """ Set a new startegy for the node

        Parameters
        -----
        new_strategy (AbstractConnectionStrategy) : new node strategy
        """
        self._strategy = new_strategy