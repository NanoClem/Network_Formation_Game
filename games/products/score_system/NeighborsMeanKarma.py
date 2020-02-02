from .AbstractScoreComputationSystem import AbstractScoreComputationSystem
from ..evaluation_system import AbstractNodeEvaluationSystem



class NeighborsMeanKarma(AbstractScoreComputationSystem):
    """
    """

    def computeNodeScore(self, graph, node, evalSystem : AbstractNodeEvaluationSystem):
        """ Compute the score of a node by getting the mean of defection among its neighbors

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
        for n in neighbors:
            graph.nodes[n]['value'] = evalSystem.evaluateNode(graph, n)  # percentage of a neighbor's defection
            score += graph.getValue(n)
            
        return score / len(neighbors)   # mean of neighbors's defection percentage