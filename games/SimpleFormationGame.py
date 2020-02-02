import networkx as nx
from .factories import AbstractGameFactory
from .factories import SimpleFormationGameFactory
from .AbstractGame import AbstractGame



class SimpleFormationGame(AbstractGame):
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
            super().__init__(graph, SimpleFormationGameFactory() )  # default factory

        # SETUP
        self._setup()

    

    ##TODO : don't overwrite attribute if already existing
    def _setup(self):
        """
        """
        attributes = ['value', 'score']
        for attr in attributes:
            nx.set_node_attributes(self.graph, 0, attr)



    def _update(self, node):
        """ Update the value attribute of a node

        Parameters
        -----
        node (AbstractNode) : node to update
        """
        value = self.nodeEval.evaluateNode(self.graph, node)    # get the new value
        self.graph.setValue(node, value)                        # assign the new value to the node



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
                ebunch  = []   
                temp = nodes
                temp.remove(node)          # removing current node to avoid self-connection

                # APPLY STRATEGY AND 
                results = node[0].applyStrategy(temp)

                # ADD NEW EDGES
                ebunch = ebunch + results[0]        # storing edges
                self.graph.add_edges_from(ebunch)   # add them to the graph

                # UPDATE NODES
                self._update(node[0])   # update only connections
        
        self.initScoring()     # SCORING
        self.initRanking()     # RANKING