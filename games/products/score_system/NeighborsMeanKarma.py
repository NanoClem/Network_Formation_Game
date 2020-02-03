from .AbstractScoreComputationSystem import AbstractScoreComputationSystem
from ..evaluation_system import AbstractNodeEvaluationSystem



class NeighborsMeanKarma(AbstractScoreComputationSystem):
    """
    """

    def computeNodeScore(self, graph, node, evalSystem : AbstractNodeEvaluationSystem):
        """ Compute the score of a node by getting the mean of defection among its neighbors. \n
        If the node doesn't have any neighbors, its score corresponds to its own value

        Parameters
        -----
        graph (nx.Graph) : graph at which the score the node is computed \n
        node (any) : current node belonging to the graph, whose score is computed \n
        evalSystem (AbstractNodeEvaluationSystem) : node evaluation system 

        Returns
        -----
        The score of the node
        """
        score = graph.nodes[node]['score']
        neighbors = list(graph.neighbors(node))

        # IF THE NODE HAS NEIGHBORS
        if len(neighbors) >= 0:
            for n in neighbors:
                score += evalSystem.evaluateNode(graph, n)
                score /= len(neighbors)   # mean of neighbors's defection percentage
                
        return score