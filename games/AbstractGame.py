from abc import ABC, abstractmethod
from.factories import AbstractGameFactory



class AbstractGame(object):
    """
    """

    @abstractmethod
    def __init__(self, factory : AbstractGameFactory = None):
        """
        """
        self.nodeEval    = factory.create_NodeEvaluationSystem()
        self.scoring     = factory.create_ScoreComputationSystem()
        self.ranking     = factory.create_RankingSystem()
        self.currentTurn = 0
        self.ranks       = []



    @abstractmethod
    def defaultFactory(self):
        """
        """
        raise NotImplementedError



    @abstractmethod
    def start(self, graph, nbturns):
        """
        """
        raise NotImplementedError



    def getRanking(self):
        """
        """
        return self.ranks



    def setRanking(self, new_ranking):
        """
        """
        self.ranks = new_ranking



    def getCurrentTurn(self):
        """
        """
        return self.currentTurn



    def setCurrentTurn(self, turn):
        """
        """
        self.currentTurn = turn



    def initScoring(self, graph):
        """
        """
        self.scoring.computeAllScores(graph, self.nodeEval)     # init score computing


    
    def initRanking(self, graph):
        """
        """
        self.setRanking(self.ranking.getNodesRanking(graph))    # set local ranking
        self.ranking.setNodesRank(graph, self.ranks)            # set rank for each node