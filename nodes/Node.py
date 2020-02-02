from .AbstractNode import AbstractNode
from .strategies import AbstractStrategy



class Node(AbstractNode):
    """
    """
    
    def __init__(self, id, strategy : AbstractStrategy):
        """ Constructor \n
        Calls parent constructor (AbstractNode)
        """
        super().__init__(id, strategy)



    def __repr__(self):
        """
        """
        return str(self._id)



    def __str__(self):
        """
        """
        return str(self._id)



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