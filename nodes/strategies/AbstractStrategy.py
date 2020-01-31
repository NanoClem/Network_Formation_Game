from abc import ABC, abstractmethod



class AbstractStrategy(ABC):
    """
    """

    @abstractmethod
    def connectingDecision(self, indicator = None):
        """ Establish a connecting strategy among nodes, based or not on a specific indicator.

        Parameters
        -----
        indicator (any) : crucial element which allows the node to decide if it connects or not
        """
        raise NotImplementedError