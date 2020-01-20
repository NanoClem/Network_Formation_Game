from .AbstractNodeEvaluationSystem import AbstractNodeEvaluationSystem


class DegreeEvaluation(AbstractNodeEvaluationSystem):
    """
    """

    def evaluateNode(self, graph, node):
        """ Evaluate a node by its degree in the graph
        Parameters
        -----
            graph(nx.Graph): graph at which the node belongs
            node(any): current node to evaluate

        Returns
        -----
            The degree of the node
        """
        return graph.degree(node)