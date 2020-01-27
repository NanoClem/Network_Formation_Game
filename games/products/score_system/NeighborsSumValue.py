from .AbstractScoreComputationSystem import AbstractScoreComputationSystem
from ..evaluation_system import AbstractNodeEvaluationSystem



class NeighborsSumValue(AbstractScoreComputationSystem):
    """
    """
 
    def computeNodeScore(self, graph, node, evalSystem : AbstractNodeEvaluationSystem):
        """ Compute the score of a node by adding its neighbors value

        Parameters
        -----
        graph(nx.Graph) : graph at which the score the node is computed
        node(any) : current node belonging to the graph, whose score is computed
        """
        score = 0
        neighbors = list(graph.neighbors(node))
        for n in neighbors:
            graph.nodes[n]['value'] = evalSystem.evaluateNode(graph, n)  # assign value to the node
            score += graph.getValue(n)
            
        return score