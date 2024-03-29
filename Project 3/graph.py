'''----------------- 
# Author: Parker Clark
# Date: 3/28/2024
# Description: A file that contains the Graph class. Used in programming assignment 3.
-----------------'''

#---Imports---#
import math
from pathfinding import Node
from pathfinding import Connection

class Graph:

    def __init__(self, nodeFile, connectionFile):
        '''
        Constructor: Creates a graph object that builds a structure based on the node/connection file.
                     Implements the functionality starting at line 281 in the R file.

        Members
        ----------
        nodeFile: str
            The file containing the node data.

        connectionFile: str
            The file containing the connection data.
        '''

        # Open the node file and read in each line.
        nodeFile = open(nodeFile, 'r')
        nodeFileRead = nodeFile.readlines()
        nodeFile.close()

        # Create a list of default nodes.
        self.currentNodes = [Node()]

        # Iterate through read data and instantiate nodes.
        for i in nodeFileRead:

            # Ignore comments in the node file.
            if i[0] == '#':
                continue

            # Split the current row delimted by a comma.
            currentRow = i.split(',')

            # Create a new node from the read in data, append it to the list

            self.currentNodes.append(Node("N", int(currentRow[1]), int(currentRow[2]), float(currentRow[3]), float(currentRow[4]),\
                                      float(currentRow[5]), float(currentRow[6]), float(currentRow[7]), float(currentRow[8])))
            
        
        # Open the connection file and read in each line.
        connectionFile = open(connectionFile, 'r')
        connectionFileRead = connectionFile.readlines()
        connectionFile.close()

        # Create a list of default connections.
        self.currentConnections = [Connection()]

        # Iterate through read data and instantiate connections.
        for i in connectionFileRead:

            # Ignore comments in the connections file.
            if i[0] == '#':
                continue
            
            # Split the current row delimted by a comma.
            currentRow = i.split(',')

            # Create a new connection from the read in data, append it to the list
            self.currentConnections.append(Connection("C", int(currentRow[1]), int(currentRow[2]), int(currentRow[3]), \
                                                      float(currentRow[4]), int(currentRow[6])))
    







