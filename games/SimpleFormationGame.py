
from .factories import AbstractGameFactory
from .factories import SimpleFormationGameFactory
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
        super().__init__( SimpleFormationGameFactory() )



    def start(self, graph, nbturns):
        """ Begin the game with the given graph and number of turns. \n

        Parameters
        -----
        graph (nx.Graph) : the graph which the game is based on \n
        nbturns (int) : number of turns of the game
        """
        indicator = 'value'
        nodes = list(graph.nodes(data=indicator))

        for i in range(nbturns):
            self.setCurrentTurn(i+1)       # set next turn
            ebunch  = []                   # graph edges
            temp    = []                   # temporaly store graph nodes
            # TESTING ALL NODES
            for node in nodes:
                temp = nodes
                temp.remove(node)          # removing current node to avoid self-connection
                # COMPUTE AND ADDING NEW EDGES
                connections, defections = node[0].isConnecting(temp, indicator)
                ebunch = ebunch + connections    # adding new edges
            
            # ADD EDGES TO THE GRAPH
            graph.add_edges_from(ebunch)  # add edges
        
        self.initScoring(graph)     # SCORING
        self.initRanking(graph)     # RANKING