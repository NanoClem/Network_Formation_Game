from abc import ABC, abstractmethod
from.factories import AbstractGameFactory



class AbstractGame(object):
    """
    """

    @abstractmethod
    def __init__(self, graph, factory : AbstractGameFactory = None):
        """
        """
        self.nodeEval    = factory.create_NodeEvaluationSystem()
        self.scoring     = factory.create_ScoreComputationSystem()
        self.ranking     = factory.create_RankingSystem()
        self.currentTurn = 0
        self.graph       = graph
        self.ranks       = []



    @abstractmethod
    def _setup(self):
        """
        """
        raise NotImplementedError



    def _update(self, node, attribute):
        """ Update the an attribute of a node

        Parameters
        -----
        node (AbstractNode) : node to update
        attribute (string) : attribute to set
        """
        value = self.nodeEval.evaluateNode(self.graph, node)    # get the new value
        self.graph.setAttribute(node, attribute, value)         # assign the new value to the node



    @abstractmethod
    def start(self, nbturns):
        """
        """
        raise NotImplementedError


    
    @abstractmethod
    def setEvaluationSystem(self, new_evalSystem):
        """
        """
        self.nodeEval = new_evalSystem


    
    



    def getGraph(self):
        """
        """
        return self.graph



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



    def initScoring(self):
        """
        """
        self.scoring.computeAllScores(self.graph, self.nodeEval)     # init score computing


    
    def initRanking(self):
        """
        """
        self.setRanking(self.ranking.getNodesRanking(self.graph))    # set local ranking
        self.ranking.setNodesRank(self.graph, self.ranks)            # set rank for each node