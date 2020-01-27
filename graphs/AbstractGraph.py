from abc import ABC, abstractmethod
import networkx as nx



class AbstractGraph(ABC, nx.Graph):
    """
    """

    @abstractmethod
    def __init__(self, title=None):
        """
        """
        nx.Graph.__init__(self, name=title)



    @abstractmethod
    def setup(self, nbunch=None):
        """
        """
        raise NotImplementedError



    def getValue(self, node):
        """ Returns the node's value, corresponding to its degree
        
        Parameters
        -----
            node(any): current node which value is returned
            
        Returns
        ----- 
        The node degree
        """
        return self.nodes[node]['value']



    def getScore(self, node):
        """ Returns the score of a node, corresponding to the sum of its neighbors's values
        
        Parameters
        -----
            node(any): current node which score is returned
            
        Returns
        -----
        The score field of the node
        """
        return self.nodes[node]['score']
        
