from .AbstractScoreComputationSystem import AbstractScoreComputationSystem



class NeighborsSumValue(AbstractScoreComputationSystem):
    """
    """

    def __init__(self, evalSystem):
        """ CONSTRUCTOR
        -----
        Init the neighbors sum value computation system
        """
        self.nodeEval = evalSystem

    
    def computeNodeScore(self, graph, node):
        """ Compute the score of a node by adding its neighbors value

        Parameters
        -----
        graph(nx.Graph) : graph at which the score the node is computed
        node(any) : current node belonging to the graph, whose score is computed
        """
        score = 0
        neighbors = list(graph.neighbors(node))
        for n in neighbors:
            graph.nodes[n]['value'] = self.nodeEval.evaluateNode(graph, n)  # assign value to the node
            score += graph.getValue(n)
            
        return score