from abc import ABC, abstractmethod



class AbstractScoreComputationSystem(object):
    """
    """
    
    @abstractmethod
    def computeNodeScore(self, node):
        raise NotImplementedError


    def computeAllScores(self, graph):
        """ Compute the score of each node of the graph and set nodes "score" attribute

        Parameters
        -----
        graph (networkx.Graph) :
        node (any) :
        """
        nodes = list(graph.nodes)
        for n in nodes:
            graph.nodes[n]['score'] = self.computeNodeScore(n)