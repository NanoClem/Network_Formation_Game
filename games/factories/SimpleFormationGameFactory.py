from .AbstractGameFactory import AbstractGameFactory
from ..products import DegreeEvaluation, NeighborsSumValue, MaxScore, TurnByTurn



class SimpleFormationGameFactory(AbstractGameFactory):
    """
    """

    def create_NodeEvaluationSystem(self):
        pass

    def create_ScoreComputationSystem(self):
        pass

    def create_TurnSystem(self):
        pass