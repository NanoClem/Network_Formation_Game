from abc import ABC, abstractmethod



class AbstractStrategy(ABC):
    """
    """

    @abstractmethod
    def connectingDecision(self):
        raise NotImplementedError