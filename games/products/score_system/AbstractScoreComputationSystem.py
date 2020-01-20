from abc import ABC, abstractmethod



class AbstractScoreComputationSystem(object):
    """
    """
    
    @abstractmethod
    def computeNodeScore(self, node):
        raise NotImplementedError

    @abstractmethod
    def _computeAllScores(self, nodes):
        raise NotImplementedError