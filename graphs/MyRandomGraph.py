import networkx as nx
from random import random



class MyRandomGraph(nx.Graph):
    """
    This class represents a random graph where each node have 
    a given probability to connect to any other.
    """
    
    def __init__(self, n, p):
        """ CONSTRUCTOR of MyRandomGraph class
        Parameters:
            (int) n   : number of nodes in the graph
            (float) p : probability of the nodes's connexion
        """
        nx.Graph.__init__(self)     # parent constructor
        self.n = n
        self.p = p
        self.generate()
        
        
    def generate(self):
        """ Generate connexions of the random graph
        """
        nbunch  = [i for i in range(self.n)]   # graph nodes
        ebunch  = []                           # graph edges
        randnum = 0                            # randomly generated number (between 0 and 1 included)
        temp    = nbunch                       # temporary stock nodes without the current one to avoid self-connection
        self.add_nodes_from(nbunch)            # add our nodes to the graph
        
        for node in list(self.nodes):
            temp.remove(node)         # removing current node
            for ni in temp:
                randnum = random()
                if randnum <= self.p:
                    ebunch.append( (node, ni) )     # add new connexion to ebunch 
            temp.append(node)                       # get current node back
        
        self.add_edges_from(ebunch)     # add edges