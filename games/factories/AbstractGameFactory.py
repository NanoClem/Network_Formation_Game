from abc import ABC, abstractmethod



class AbstractGameFactory(ABC):
    """
    """

    @abstractmethod
    def create_NodeEvaluationSystem(self):
        raise NotImplementedError

    @abstractmethod
    def create_ScoreComputationSystem(self):
        raise NotImplementedError

    @abstractmethod
    def create_RankingSystem(self):
        raise NotImplementedError

    @abstractmethod
    def create_TurnSystem(self):
        raise NotImplementedError