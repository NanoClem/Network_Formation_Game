from .AbstractGameFactory import AbstractGameFactory
from ..products import KarmaEvaluation, NeighborsMeanValue, MinScore, TurnByTurn



class BadKarmaGameFactory(AbstractGameFactory):
    """
    """

    def create_NodeEvaluationSystem(self):
        """
        """
        return KarmaEvaluation()


    def create_ScoreComputationSystem(self):
        """
        """
        return NeighborsMeanValue()


    def create_RankingSystem(self):
        """
        """
        return MinScore()


    def create_TurnSystem(self):
        """
        """
        TurnByTurn()