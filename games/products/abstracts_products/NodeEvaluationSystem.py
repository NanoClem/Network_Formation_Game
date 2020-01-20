from abc import ABC, abstractmethod



class NodeEvaluationSystem(ABC):
    """
    """
    
    @abstractmethod
    def evaluateNode(self, node):
        raise NotImplementedError