from abc import ABC, abstractmethod



class TurnSystem(ABC):
    """
    """
    
    @abstractmethod
    def start(self, graph):
        raise NotImplementedError