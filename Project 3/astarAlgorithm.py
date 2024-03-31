'''----------------- 
# Author: Parker Clark
# Date: 3/28/2024
# Description: A file that contains the A* Algorithm. Used in programming assignment 3.
-----------------'''

from graph import Graph


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
        currentNode: int
            The current node.

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
    
    def findPath(self, first, last):
        '''
        Utilize A* to find the path between two nodes.

        Parameters
        ----------  
        first: int
            The starting node.
        
        last: int
            The ending node
        '''

        # Reset the nodes in the graph.
        for i in range(1, len(self.graph.currentNodes)):
            self.graph.currentNodes[i].status = 0
            self.graph.currentNodes[i].costSoFar = float('inf')
            self.graph.currentNodes[i].previous = 0

        # Set the node status to open and the cost to 0.
        self.graph.currentNodes[first].status = 2
        self.graph.currentNodes[first].costSoFar = 0

        # Initialize the open list with the first node, and a control variable.
        iteration = 0
        openList = [first]

        # Iterate through the graph and find the path.
        while len(openList) > 0:
            iteration += 1

            # Find the node with the lowest total cost in the open list.
            currentNode = self.findLowest(openList)

            # If the current node is the last node, break the loop.
            if currentNode == last:
                break

            # Get the connections from the current node.
            currentConnections = self.getConnections(currentNode)

            # Iterate through the connections and update the nodes.
            for connection in currentConnections:

                # Get the next node on the connection and the cost.
                nextNode = connection.toNode
                nextCost = self.graph.currentNodes[currentNode].costSoFar + connection.cost

                # If the next node has a lower cost, update the node.
                if nextCost < self.graph.currentNodes[nextNode].costSoFar:
                    
                    # Open the next node on the path, and update the previous node.
                    self.graph.currentNodes[nextNode].status = 2
                    self.graph.currentNodes[nextNode].previous = currentNode
                    
                    # Update the cost, heuristic, and total values.
                    self.graph.currentNodes[nextNode].costSoFar = nextCost
                    self.graph.currentNodes[nextNode].heuristic = self.graph.currentNodes[nextNode].heuristicDistance(self.graph.currentNodes[last])
                    self.graph.currentNodes[nextNode].total = self.graph.currentNodes[nextNode].costSoFar + self.graph.currentNodes[nextNode].heuristic

                    # Add the next node to the open list.
                    if nextNode not in openList:
                        openList.append(nextNode)

            # Close the current node.        
            self.graph.currentNodes[currentNode].status = 3
            openList.remove(currentNode)

            # Set an attribute to return the last node's total cost.
            self.totalCost = self.graph.currentNodes[last].costSoFar