from abc import ABC, abstractmethod
from .AbstractRankingSystem import AbstractRankingSystem



class MaxScore(AbstractRankingSystem):
    """
    """
    
    ##TODO : define what to do when there is a tie case
    def getNodesRanking(self, graph):
        """ Sorts nodes in descending mode based on their 'score' field.
        A rank of a node corresponds to its position in the returned result.
        This function does not modify nodes attributes on the graph.

        Parameters
        -----
            graph (networkx.Graph): current graph on which we apply the ranking method

        Returns
        -----
        A nbunch of a all ranked nodes
        """
        scores  = dict(graph.nodes.data())
        ranking = sorted(scores.items(), key=lambda x: x[1]['score'], reverse=True)  # sort on 'score' key in descending mode

        return ranking