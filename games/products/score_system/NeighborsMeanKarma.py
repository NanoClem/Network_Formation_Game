from .AbstractScoreComputationSystem import AbstractScoreComputationSystem



class NeighborsMeanKarma(AbstractScoreComputationSystem):
    """
    """

    def __init__(self, evalSystem):
        """ CONSTRUCTOR
        -----
        Init the neighbors mean of karma computation system
        """
        self.nodeEval = evalSystem

    
    def computeNodeScore(self, graph, node):
        """ Compute the score of a node by getting the mean of defection among its neighbors

        Parameters
        -----
        graph(nx.Graph) : graph at which the score the node is computed
        node(any) : current node belonging to the graph, whose score is computed
        """
        score = 0
        neighbors = list(graph.neighbors(node))
        for n in neighbors:
            graph.nodes[n]['value'] = self.nodeEval.evaluateNode(graph, n)  # percentage of a neighbor's defection
            score += graph.getValue(n)
            
        return score / len(neighbors)   # mean of neighbors's defection percentage