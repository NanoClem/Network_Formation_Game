from abc import ABC, abstractmethod



class AbstractRankingSystem(object):
    """
    """
    
    @abstractmethod
    def getGlobalRanking(self, graph):
        raise NotImplementedError