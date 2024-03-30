'''----------------- 
# Author: Parker Clark
# Date: 3/28/2024
# Description: A file that contains classes for both connections and nodes. Used in programming assignment 3.
-----------------'''

#---Imports---#
import math

class Node:

    def __init__(self, id="N", nodeNum=0, status=0, costSoFar=0, heuristic=0, total=0, previous=0, positionX=0, positionY=0):
        '''
        Constructor: Creates a node object. Initializes and holds all constants
                     from line 60-66 in the R file.

        Members
        ----------
        id: const char
            The unique identifier of the node.
        
        nodeNum: int
            The number of the node in sequence.

        status: int
            The status of the node. Valid inputs are undefined (0), unvisted (1), open (2), or closed (3).
        
        costSoFar: float
            The cost of shortest path found so far to this node.
        
        heuristic: float
            The estimated heuristic cost.
        
        total: float
            The estimated cost total.
        
        previous: int
            The prior node object on path to which this one was reached.
        
        positionX: int
            The x-coordinate of the node's position.
        
        positionY: int
            The y-coordinate of the node's position.
        '''

        self.id = id
        self.nodeNum = nodeNum
        self.status = status
        self.costSoFar = costSoFar
        self.heuristic = heuristic
        self.total = total
        self.previous = previous
        self.positionX = positionX
        self.positionY = positionY

    def heuristicDistance(self, node):
        '''
        Calculate the heuristic value using std Euclidena 2D Distance.

        Parameters
        ----------
        node: Node
            The node to which the heuristic distance is calculated.

        Returns
        ----------
        float
            The heuristic distance between the two nodes.
        '''
        return math.sqrt((self.positionX - node.positionX)**2 + (self.positionY - node.positionY)**2)
    
    def reset(self):
        '''
        Reset the given node object.

        Parameters
        ----------
        self: Node
            The node object being reset.
        '''
        self.status = 0
        self.costSoFar = float('inf')
        self.previous = 0
    

class Connection:
    
    def __init__(self, id="C", connectionNum=0, fromNode=0, toNode=0, cost=0, totalCost=0, type=0):
        '''
        Constructor: Creates a connection object. Initializes and holds all constants
                 from line 74-78 in the R file.

        Members
        ----------
        id: const char
            The unique identifier of the connection.
        
        connectionNum: int
            The number of the connection in sequence.

        fromNode: int
            The node where the connection starts.

        toNode: int
            The node where the connection ends.

        cost: float
            The cost of the connection.

        totalCost: float
            The estimated total cost of the connection.

        type: int
           The previous node in path from start to this node.
        '''

        self.id = id
        self.connectionNum = connectionNum
        self.fromNode = fromNode
        self.toNode = toNode
        self.cost = cost
        self.totalCost = totalCost
        self.type = type