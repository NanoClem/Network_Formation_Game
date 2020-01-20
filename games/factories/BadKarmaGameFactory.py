from .AbstractGameFactory import AbstractGameFactory
from ..products import KarmaEvaluation, NeighborsMeanValue, MinScore, TurnByTurn



class BadKarmaGameFactory(AbstractGameFactory):
    """
    """

    def create_NodeEvaluationSystem(self):
        pass

    def create_ScoreComputationSystem(self):
        pass

    def create_TurnSystem(self):
        pass