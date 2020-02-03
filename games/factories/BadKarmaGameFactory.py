from .AbstractGameFactory import AbstractGameFactory
from ..products import KarmaEvaluation, NeighborsMeanKarma, MinScore, TurnByTurn



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
        return NeighborsMeanKarma()


    def create_RankingSystem(self):
        """
        """
        return MinScore()


    def create_TurnSystem(self):
        """
        """
        TurnByTurn()