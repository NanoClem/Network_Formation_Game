from .AbstractStrategy import AbstractStrategy
from random import random



class RandomStrategy(AbstractStrategy):
    """
    """
    
    def __init__(self, p):
        """
        """
        self._p = p



    def connectingDecision(self, indicator = None):
        """
        """
        randnum = random()
        if randnum <= self._p:
            return True

        return False