import networkx as nx
from .factories import AbstractGameFactory
from .factories import RealisticFormationGameFactory
from .AbstractGame import AbstractGame



class RealisticFormationGame(AbstractGame):
    """
    """

    def __init__(self, graph, factory : AbstractGameFactory = None):
        """ CONSTRUCTOR

        Parameters
        ------
        factory (AbstractGameFactory) : the game factory used to build the game
        """
        # GRAPH
        self.graph = graph

        # FACTORY
        if factory:
            super().__init__(graph, factory)   # init parent
        else:
            super().__init__(graph, RealisticFormationGameFactory() )  # default factory

        # SETUP
        self._setup()

    

    def _setup(self):
        """
        """
        attributes = ['value', 'score']
        for attr in attributes:
            nx.set_node_attributes(self.graph, 0, attr)



    def start(self, nbturns):
        """ Begin the game with the given graph and number of turns. \n

        Parameters
        -----
        graph (nx.Graph) : the graph which the game is based on \n
        nbturns (int) : number of turns of the game
        """
        indicator = 'value'     # game's indicator on which nodes base their strategy
        nodes = list(self.graph.nodes(data = indicator))
        temp  = []                   # temporaly store graph nodes

        for i in range(nbturns):
            self.setCurrentTurn(i+1)       # set next turn

            # TESTING ALL NODES
            for node in nodes:
                temp = list(self.graph.nodes(data = indicator))
                temp.remove(node)          # removing current node to avoid self-connection

                # APPLY STRATEGY AND 
                results = node[0].applyStrategy(temp)

                # ADD NEW EDGES
                self.graph.add_edges_from(results[0])   # add them to the graph

                # UPDATE NODES
                self._update(node[0], indicator)   # update only connections
                temp.append(node)
        
        self.initScoring()     # SCORING
        self.initRanking()     # RANKING