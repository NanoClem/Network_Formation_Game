from abc import ABC, abstractmethod



class AbstractTurnSystem(ABC):
    """
    """
    
    @abstractmethod
    def start(self, graph):
        raise NotImplementedError