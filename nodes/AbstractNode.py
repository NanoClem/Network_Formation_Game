from abc import ABC, abstractmethod
from .strategies import AbstractStrategy



class AbstractNode(ABC):
    """
    """
    
    @abstractmethod
    def __init__(self, id, strategy : AbstractStrategy):
        """
        """
        self._strategy = strategy
        self._id = id



    def __repr__(self):
        """
        """
        return str(self._id)



    def __str__(self):
        """
        """
        return str(self._id)



    @abstractmethod
    def isConnecting(self, node) -> bool:
        """ Decides weither to connect or not to a given node. \n
        If the node is already connected, then it's a matter of defecting of not.

        Parameters
        -----
        node (AbstractNode) : element weither to connect or not

        Returns
        -----
        True if it connect, false either
        """
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