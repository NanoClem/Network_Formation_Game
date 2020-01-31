
from .factories import AbstractGameFactory
from .factories import BadKarmaGameFactory
from .AbstractGame import AbstractGame



class SimpleFormationGame(AbstractGame):
    """
    """

    def __init__(self, factory : AbstractGameFactory = None):
        """ CONSTRUCTOR

        Parameters
        ------
        factory (AbstractGameFactory) : the game factory used to build the game
        """
        if factory:
            super().__init__(factory)   # init parent
        else:
            self.defaultFactory()



    def defaultFactory(self):
        """ Set a default game factory to the parent constructor
        """
        super().__init__( BadKarmaGameFactory() )



    def start(self, graph, nbturns):
        """ Begin the game with the given graph and number of turns. \n

        Parameters
        -----
        graph (nx.Graph) : the graph which the game is based on \n
        nbturns (int) : number of turns of the game
        """
        nodes = list(graph.nodes)
        for i in range(nbturns):
            self.setCurrentTurn(i+1)       # set next turn
            ebunch  = []                   # graph edges
            temp    = nodes                # temporary stock nodes without the current one to avoid self-connection
            
            # TESTING ALL NODES
            for node in nodes:
                temp.remove(node)         # removing current node
                for ni in temp:
                    # NODE STRATEGY
                    if ni.isConnecting():
                        ebunch.append( (node, ni) )     # add new connexion to ebunch 
                temp.append(node)                       # get current node back
            
            # ADD EDGES
            graph.add_edges_from(ebunch)  # add edges
        
        self.initScoring(graph)     # SCORING
        self.initRanking(graph)     # RANKING