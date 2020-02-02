from .AbstractScoreComputationSystem import AbstractScoreComputationSystem
from ..evaluation_system import AbstractNodeEvaluationSystem



class NeighborsSumValue(AbstractScoreComputationSystem):
    """
    """
 
    def computeNodeScore(self, graph, node, evalSystem : AbstractNodeEvaluationSystem):
        """ Compute the score of a node by adding its neighbors value

        Parameters
        -----
        graph(nx.Graph) : graph at which the score the node is computed \n
        node(any) : current node belonging to the graph, whose score is computed \n
        evalSystem(AbstractNodeEvaluationSystem) : node evaluation system 

        Returns
        -----
        The score of the node
        """
        score = graph.nodes[node]['score']
        print(graph.nodes[node]['value'])
        neighbors = list(graph.neighbors(node))
        for n in neighbors:
            score += graph.getValue(n)
            
        return score