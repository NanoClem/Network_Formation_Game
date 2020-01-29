from abc import ABC, abstractmethod
from ..evaluation_system import AbstractNodeEvaluationSystem



class AbstractScoreComputationSystem(ABC):
    """
    """
    
    @abstractmethod
    def computeNodeScore(self, graph, node, evalSytem : AbstractNodeEvaluationSystem):
        raise NotImplementedError


    def computeAllScores(self, graph, evalSystem : AbstractNodeEvaluationSystem):
        """ Compute the score of each node of the graph and set nodes "score" attribute

        Parameters
        -----
        graph(nx.Graph) : graph at which the score of each node is computed
        """
        nodes = list(graph.nodes)
        for n in nodes:
            graph.nodes[n]['score'] = self.computeNodeScore(graph, n, evalSystem)