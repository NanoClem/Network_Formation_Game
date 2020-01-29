from .AbstractGameFactory import AbstractGameFactory
from ..products import DegreeEvaluation, NeighborsSumValue, MaxScore, TurnByTurn



class SimpleFormationGameFactory(AbstractGameFactory):
    """
    """

    def create_NodeEvaluationSystem(self):
        """
        """
        return DegreeEvaluation()


    def create_ScoreComputationSystem(self):
        """
        """
        return NeighborsSumValue()


    def create_RankingSystem(self):
        """
        """
        return MaxScore()


    def create_TurnSystem(self):
        """
        """
        TurnByTurn()