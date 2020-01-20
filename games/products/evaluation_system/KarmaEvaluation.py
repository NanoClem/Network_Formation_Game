from .AbstractNodeEvaluationSystem import AbstractNodeEvaluationSystem


class KarmaEvaluation(AbstractNodeEvaluationSystem):
    """
    """

    def evaluateNode(self, graph, node):
        """ Evaluate a node by the percentage of time it has defected
        Parameters
        -----
            graph(nx.Graph): graph at which the node belongs
            node(any): current node to evaluate

        Returns
        -----
            Percentage of time the node has defected
        """
        return graph.nodes[node]['karma'] / 100