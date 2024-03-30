'''----------------- 
# Author: Parker Clark
# Date: 3/29/2024
# Description: A driver file for Program Assignment 3.
-----------------'''


#---Imports---#
from graph import Graph
from astarAlgorithm import AStarAlgorithm

def main():

    # Create an output file to log the results
    outputFile = open("output.txt", "w")


    # Initialize the graph object, pass in the node and connection file
    graph = Graph("nodes.txt","connections.txt")


    # TODO: Debug this,hitting an infinite loop for some reason
    print(len(graph.currentNodes))

    # Define a list of key data points, each sublist is a start and end point respectively 
    dataPoints = [
        [1, 29], 
        [1, 38],
        [11, 1],
        [33, 66],
        [58, 43],
    ]

    for dataPoint in dataPoints:

        # Read in the start and end points
        start, end = dataPoint

        # Initialize the A* Algorithm
        astar = AStarAlgorithm(graph)

        # Find the start and end node path
        astar.findPath(start, end)
        path = astar.retrievePath(start, end)

        # Write the path to the output file
        outputFile.write(f"Path from {start} to {end}: {path}\n")

    # Close the output file
    outputFile.close()

# Run the main function
if __name__ == "__main__":
    main()