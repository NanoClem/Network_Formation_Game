import networkx as nx
from abc import ABC, abstractmethod



class AbstractRankingSystem(object):
    """
    """
    
    @abstractmethod
    def getNodesRanking(self, graph):
        raise NotImplementedError


    def setNodesRank(self, graph, ranking):
        """ Set rank attribute for each node in the graph.
        This function does modify nodes attributes in the graph.

        Parameters
        -----
        graph (networkx.Graph): graph on which we set a rank attribute for each node
        ranking (nbunch): nbunch of ranked nodes
        """
        rankedNodes = ranking
        for i in range(len(rankedNodes)):
            rankedNodes[i][1] = {'rank': i+1}   # keep only the rank attribute and set its value
            
        nx.set_node_attributes(graph, dict(rankedNodes))