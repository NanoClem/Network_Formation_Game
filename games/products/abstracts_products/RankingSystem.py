from abc import ABC, abstractmethod



class RankingSystem(object):
    """
    """
    
    @abstractmethod
    def getGlobalRanking(self, graph):
        raise NotImplementedError