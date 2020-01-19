import networkx as nx
from random import random



class MyRandomGraph(nx.Graph):
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
        nx.Graph.__init__(self, name=title)     # parent constructor
        self.n = n
        self.p = p
        self.generate()
        
        
        
    def getValue(self, node):
        """ Returns the node's value, corresponding to its degree
        
        Parameters
        -----
            node(any): current node to evaluate
            
        Returns
        ----- 
        The node degree
        """
        return self.degree(node)
    
    
    
    def getScore(self, node):
        """ Returns the score of a node, corresponding to the sum of its neighbors's values
        
        Parameters
        -----
            node(any): current node to evaluate
            
        Returns
        -----
        The score field of the node
        """
        return self.nodes[node]['score']
        
        
        
    def _computeNodeScore(self, node):
        """ Compute the score of a node
        
        Parameters
        -----
            node(any): current node to evaluate
            
        Returns
        -----
        The computed score of the node
        """
        score = 0
        neighbors = list(self.neighbors(node))
        for n in neighbors:
            score += self.getValue(n)
            
        return score
    
    
    
    def _computeScores(self):
        """ Compute the score of each node of the graph
        """
        nodes = list(self.nodes)
        for n in nodes:
            self.nodes[n]['score'] = self._computeNodeScore(n)
      
      
        
    def generate(self):
        """ Generate edges of the graph
        """
        nbunch  = [i for i in range(self.n)]   # graph nodes
        ebunch  = []                           # graph edges
        randnum = 0                            # randomly generated number (between 0 and 1 included)
        temp    = nbunch                       # temporary stock nodes without the current one to avoid self-connection
        self.add_nodes_from(nbunch, score=0)   # add our nodes to the graph with a default score
        
        for node in list(self.nodes):
            temp.remove(node)         # removing current node
            for ni in temp:
                randnum = random()
                if randnum <= self.p:
                    ebunch.append( (node, ni) )     # add new connexion to ebunch 
            temp.append(node)                       # get current node back
        
        self.add_edges_from(ebunch)     # add edges
        self._computeScores()           # compute scores