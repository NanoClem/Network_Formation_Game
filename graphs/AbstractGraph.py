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
        print(self.nodes[node])
        return self.nodes[node]['value']



    def getScore(self, node):
        """ Returns the score of a node
        
        Parameters
        -----
            node(any): current node which score is returned
            
        Returns
        -----
        The score field of the node
        """
        return self.nodes[node]['score']



    def getAllScores(self):
        """ Returns all scores for each node in the graph

        Returns
        -----
        Nbunch of the graph nodes with only the "score" field
        """
        return dict(self.nodes(data='score'))



    def getAllValues(self):
        """ Returns all values for each node in the graph

        Returns
        -----
        Nbunch of the graph nodes with only the "value" field
        """
        return dict(self.nodes(data='value'))


    
    def setValue(self, node, new_value):
        """
        """
        self.nodes[node]['value'] = new_value
        
