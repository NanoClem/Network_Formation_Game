from .AbstractGameFactory import AbstractGameFactory
from ..products import RealisticDegreeEvaluation, NeighborsSumValue, MaxScore, TurnByTurn



class RealisticFormationGameFactory(AbstractGameFactory):
    """
    """

    def create_NodeEvaluationSystem(self):
        """
        """
        return RealisticDegreeEvaluation()


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