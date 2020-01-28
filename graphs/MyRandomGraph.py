from random import random
from .AbstractGraph import AbstractGraph
from nodes import Randomizer



class MyRandomGraph(AbstractGraph):
    """
    This class represents a random graph where each node have 
    a given probability to connect to any other.
    """
    
    def __init__(self, n, p, title=None):
        """ Initialise a random graph with nodes and a probability for them to connect
        
        Parameters
        -----
            (int) n   : number of nodes
            (float) p : probability of a node to connect with another
        """
        super().__init__(title)     # parent constructor
        self.n = n
        self.p = p
        self.setup()



    def setup(self):
        """
        """
        nbunch  = [Randomizer(i, self.p) for i in range(self.n)]    # create nodes with a random strategy
        self.add_nodes_from(nbunch)
        

        
    def _computeNodeScore(self, node):
        """ Compute the score of a node
        
        Parameters
        -----
            node(any): current node which score is computed
            
        Returns
        -----
        The computed score of the node
        """
        score = 0
        neighbors = list(self.neighbors(node))
        for n in neighbors:
            self.nodes[n]['value'] = self._evaluateNode(n)  # assign value to the node
            score += self.getValue(n)
            
        return score
    
    

    def _computeScores(self):
        """ Compute the score of each node of the graph
        """
        nodes = list(self.nodes)
        for n in nodes:
            self.nodes[n]['score'] = self._computeNodeScore(n)

    
    
    def _evaluateNode(self, node):
        """
        Parameters
        -----
            node(any): current node to evaluate

        Returns
        -----
            The value of the node
        """
        return self.degree(node)
        

      
    def generate(self):
        """ Generate edges of the graph
        """
        ebunch  = []                  # graph edges
        temp    = list(self.nodes)    # temporary stock nodes without the current one to avoid self-connection
        
        for node in list(self.nodes):
            temp.remove(node)         # removing current node
            for ni in temp:
                # NODE STRATEGY
               if ni.isConnecting():
                    ebunch.append( (node, ni) )     # add new connexion to ebunch 
            temp.append(node)                       # get current node back
        
        self.add_edges_from(ebunch)     # add edges
        self._computeScores()           # compute scores