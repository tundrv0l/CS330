'''----------------- 
# Author: Parker Clark
# Date: 3/28/2024
# Description: A file that contains the A* Algorithm. Used in programming assignment 3.
-----------------'''

from graph import Graph
from pathfinding import Node


class AStarAlgorithm:

    def __init__(self, graph : Graph):
        '''
        Constructor: Creates an A* Algorithm object. This is a static class.

        Members
        ----------
        graph: Graph
            The graph object that the A* algorithm will be applied to.
        '''

        self.graph = graph

    def getConnections(self, currentNode):
        '''
        Get the connections from the current node.

        Parameters
        ----------  
        currentNode: Node
            The current node object.

        Returns
        ----------
        connections: list
            A list of connections from the current node.
        '''

        connections = []

        for i in self.graph.currentConnections:
            if i.fromNode == currentNode:
                connections.append(i)

        return connections
    
    def findLowest(self, openList):
        '''
        Find the node with the lowest total cost in the open list.

        Parameters
        ----------  
        openList: list
            A list of nodes that are open.

        Returns
        ----------
        result: Node
            The node with the lowest total cost in the open list.
        '''

        lowest = float('inf')

        for i in openList:
           node = self.graph.currentNodes[i]

           if node.total < lowest:
               lowest = node.total
               result = i

        return result
    
    def retrievePath(self, first, last):
        '''
        Utilize A* to retrieve the path between two nodes.

        Parameters
        ----------  
        first: int
            The starting node.
        
        last: int
            The ending node

        Returns
        ----------
        path: list
            The list of nodes that form the path.
        '''

        path = []
        current = last

        # Iterate through the graph and find the path.
        while (current != first) and (current != 0):
            path.append(current)
            current = self.graph.currentNodes[current].previous
        
        # Found the path, append the first node to the list.
        if current == first:
            path.append(first)
        
        # Otherwise, the path is empty.
        else:
            path = []

        return path