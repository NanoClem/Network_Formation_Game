import networkx as nx
from .factories import AbstractGameFactory
from .factories import BadKarmaGameFactory
from .AbstractGame import AbstractGame



class BadKarmaGame(AbstractGame):
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
            super().__init__(graph, BadKarmaGameFactory() )  # default factory

        # SETUP
        self._setup()

    

    ##TODO : don't overwrite attribute if already existing
    def _setup(self):
        """
        """
        attributes = ['value', 'score', 'karma']
        for attr in attributes:
            nx.set_node_attributes(self.graph, 0, attr)



    def _applyKarma(self, node, karma):
        """
        """
        self.graph.nodes[node]['karma'] += karma



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
                connections, defections = node[0].applyStrategy(temp)

                # ADD NEW EDGES
                self.graph.add_edges_from(connections)   # add them to the graph

                # APPLY KARMA
                self._applyKarma(node[0], len(defections))   # add the amount of defections to the karma value
                self.graph.remove_edges_from(defections)

                # UPDATE NODES
                self._update(node[0], indicator)   # update only connections
                temp.append(node)
        
        self.initScoring()     # SCORING
        self.initRanking()     # RANKING