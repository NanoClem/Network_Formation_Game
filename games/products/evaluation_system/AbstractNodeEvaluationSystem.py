from abc import ABC, abstractmethod



class AbstractNodeEvaluationSystem(ABC):
    """
    """
    
    @abstractmethod
    def evaluateNode(self, graph, node):
        raise NotImplementedError