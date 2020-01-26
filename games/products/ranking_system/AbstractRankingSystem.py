import networkx as nx
from abc import ABC, abstractmethod



class AbstractRankingSystem(object):
    """
    """
    
    @abstractmethod
    def getNodesRanking(self, graph):
        raise NotImplementedError


    def setNodesRank(self, graph, ranking, drawMode=False):
        """ Set rank attribute for each node in the graph.
        This function does modify nodes attributes in the graph.

        Parameters
        -----
        graph (networkx.Graph): graph on which we set a rank attribute for each node
        ranking (nbunch): nbunch of ranked nodes
        drawMode (bool) : consider equals scores in ranking or not
        """
        rankedNodes = ranking
        for i in range(len(rankedNodes)):
            if drawMode:
                if rankedNodes[i][1]['score'] == rankedNodes[i-1][1]['score']:    # BEWARE : first element will compare to the last
                    rankedNodes[i][1]['rank'] = rankedNodes[i-1][1]['rank']      # Assign an equal rank if both nodes are ex-aequo
            else:
                rankedNodes[i][1] = {'rank': i+1}   # keep only the rank attribute and set its value
            
        nx.set_node_attributes(graph, dict(rankedNodes))