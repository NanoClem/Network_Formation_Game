from abc import ABC, abstractmethod



class AbstractStrategy(ABC):
    """
    """

    @abstractmethod
    def connectingDecision(self, node, nbunch):
        """ Establish a connecting strategy among nodes, based or not on a specific indicator.

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
        raise NotImplementedError