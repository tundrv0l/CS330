'''----------------- 
# Author: Parker Clark
# Date: 3/29/2024
# Description: A driver file for Program Assignment 3.
-----------------'''

#---Imports---#
from graph import Graph
from astarAlgorithm import AStarAlgorithm

#---File Constants---#
# Note for the grader: Change these constants to the proper node/connections file paths.
OUTPUT_FILE = "output.txt"
NODES_FILE = "pathfindingData/nodes.txt"
CONNECTIONS_FILE = "pathfindingData/connections.txt"

def main():

    # Create an output file to log the results
    outputFile = open(OUTPUT_FILE, "w")

    outputFile.write("-------Begin Input Data-------\n\n")

    # Print the nodes and connections to the output file
    outputFile.write("Nodes:\n")
    with open(NODES_FILE, "r") as file:
        for line in file:

            # Skip the comment line
            if line.startswith("#"):
                continue

            outputFile.write(line)

    outputFile.write("\nConnections:\n")
    with open(CONNECTIONS_FILE, "r") as file:
        for line in file:

            # Skip the comment line
            if line.startswith("#"):
                continue

            outputFile.write(line)

    outputFile.write("-------End Input Data-------\n\n")

    # Initialize the graph object, pass in the node and connection file
    graph = Graph(NODES_FILE, CONNECTIONS_FILE)

    # Define a list of key data points, each sublist is a start and end point respectively 
    dataPoints = [
        [1, 59],
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

        # Write a debugger header for the first iteration of data point
        if dataPoint == dataPoints[0]:
            outputFile.write("-------This is a Test Path-------\n\n")

        # Write the path to the output file
        outputFile.write(f"Path from {start} to {end}: {path[::-1]}\n")
        
        # Write the total cost to the output file
        outputFile.write(f"Total Cost: {astar.totalCost}\n\n")

        if dataPoint == dataPoints[0]:
            outputFile.write("-------End of Test Path-------\n\n")

    # Close the output file
    outputFile.close()

# Run the main function
if __name__ == "__main__":
    main()