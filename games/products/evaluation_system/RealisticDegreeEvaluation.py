import random
from .AbstractNodeEvaluationSystem import AbstractNodeEvaluationSystem



class RealisticDegreeEvaluation(AbstractNodeEvaluationSystem):
    """
    """

    def evaluateNode(self, graph, node):
        """ Evaluate a node by a distribution between 50% and 150% of its real degree
        Parameters
        -----
            graph(nx.Graph): graph at which the node belongs
            node(any): current node to evaluate

        Returns
        -----
            The degree of the node
        """
        return graph.degree(node) * random.uniform(0.5, 1.5)