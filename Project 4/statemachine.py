'''----------------- 
# Author: Parker Clark
# Date: 1/25/2024
# Description: A program that simulates a simple state machine.
-----------------'''

#---Imports---#
import random
from typing import TextIO # For type hinting

#---File Constants---#
SCENARIO = 2 # Scenario to run with (Can be 1 or 2).
FOLLOW = 0
PULL_OUT = 1
ACCELERATE = 2
PULL_IN_AHEAD = 3
PULL_IN_BEHIND = 4
DECELERATE = 5
DONE = 6
OUTPUT_FILE = f"Scenario{SCENARIO}Output.txt"

#---Script Variables---#
iterations = [100, 1000000][SCENARIO-1]
transitionProbability = [[0.8, 0.4, 0.3, 0.4, 0.3, 0.3, 0.8, 0.8, 0.8],
                         [0.9, 0.6, 0.3, 0.2, 0.2, 0.4, 0.7, 0.9, 0.7]][SCENARIO-1]
stateCount = [0, 0, 0, 0, 0, 0, 0]
transitionCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]
scenarioTrace = True if SCENARIO == 1 else False

#---Sequences---#
stateSequence = [[i for i in range(1, 8)], [7] + [i for i in range(1, 7)]][SCENARIO - 1]
transitionSequence = [[i for i in range(1, 10)], [9] + [i for i in range(1, 9)]][SCENARIO - 1]



#---State Functions---#
def followAction(file : TextIO):
    '''
        Update the stateCount list for the FOLLOW state. 
        Optionally write to file if trace is true.

        Parameters
        ----------  
        file: TextIO
            The output file to write to if trace is true.

        Returns
        ----------
        None
        '''
    if scenarioTrace:
        file.write("state = 1 FOLLOW\n")
    stateCount[FOLLOW] += 1

def pullOutAction(file : TextIO):
    '''
        Update the stateCount list for the PULL_OUT state. 
        Optionally write to file if trace is true.

        Parameters
        ----------  
        File: file
            The output file to write to if trace is true.

        Returns
        ----------
        None
        '''
    if scenarioTrace:
        file.write("state = 2 PULL OUT\n")
    stateCount[PULL_OUT] += 1

def accelerateAction(file : TextIO):
    '''
        Update the stateCount list for the ACCELERATE state. 
        Optionally write to file if trace is true.

        Parameters
        ----------  
        file: TextIO
            The output file to write to if trace is true.

        Returns
        ----------
        None
        '''
    if scenarioTrace:
        file.write("state = 3 ACCELERATE\n")
    stateCount[ACCELERATE] += 1

def pullInAheadAction(file : TextIO):
    '''
        Update the stateCount list for the PULL_IN_AHEAD state. 
        Optionally write to file if trace is true.

        Parameters
        ----------  
        file: TextIO
            The output file to write to if trace is true.

        Returns
        ----------
        None
        '''
    if scenarioTrace:
        file.write("state = 4 PULL IN AHEAD\n")
    stateCount[PULL_IN_AHEAD] += 1

def pullInBehindAction(file : TextIO):
    '''
        Update the stateCount list for the PULL_IN_BEHIND state. 
        Optionally write to file if trace is true.

        Parameters
        ----------  
        file: TextIO
            The output file to write to if trace is true.

        Returns
        ----------
        None
        '''
    if scenarioTrace:
        file.write("state = 5 PULL_IN_BEHIND\n")
    stateCount[PULL_IN_BEHIND] += 1

def decelerateAction(file : TextIO):
    '''
        Update the stateCount list for the DECELERATE state. 
        Optionally write to file if trace is true.

        Parameters
        ----------  
        file: TextIO
            The output file to write to if trace is true.

        Returns
        ----------
        None
        '''
    if scenarioTrace:
        file.write("state = 6 DECELERATE\n")
    stateCount[DECELERATE] += 1

def doneAction(file : TextIO):
    '''
        Update the stateCount list for the DONE state. 
        Optionally write to file if trace is true.

        Parameters
        ----------  
        file: TextIO
            The output file to write to if trace is true.

        Returns
        ----------
        None
        '''
    if scenarioTrace:
        file.write("state = 7 DONE\n\n")
    stateCount[DONE] += 1


#---Main Function---#
def main():

    # Open the output file
    with open(OUTPUT_FILE, 'w') as file:
        if scenarioTrace:
            file.write("----Begin Simulation----\n\n")

        # Create a list of states
        for i in range(1, iterations+1):
            
            # Write the iteration number to the file if trace is true
            if scenarioTrace:
                file.write(f"iteration = {i}\n")

            # Initialize the default state to FOLLOW
            state = FOLLOW
            followAction(file)

            while state != DONE:

                # Generate a uniformly random number between 0 and 1
                randomNum = random.uniform(0, 1)

                # Determine the next state based on the current state and the random number
                if state == FOLLOW:
                    if randomNum < transitionProbability[0]:
                        transitionCount[0] += 1
                        state = PULL_OUT
                        pullOutAction(file)
                    else:
                        state = FOLLOW
                        followAction(file)
                
                elif state == PULL_OUT:
                    if randomNum < transitionProbability[1]:
                        transitionCount[1] += 1
                        state = ACCELERATE
                        accelerateAction(file)
                    elif randomNum < transitionProbability[1] + transitionProbability[3]:
                        transitionCount[3] += 1
                        state = PULL_IN_BEHIND
                        pullInBehindAction(file)
                    else:
                        state = PULL_OUT
                        pullOutAction(file)

                elif state == ACCELERATE:
                    if randomNum < transitionProbability[2]:
                        transitionCount[2] += 1
                        state = PULL_IN_AHEAD
                        pullInAheadAction(file)
                    elif randomNum < transitionProbability[2] + transitionProbability[4]:
                        transitionCount[4] += 1
                        state = PULL_IN_BEHIND
                        pullInBehindAction(file)
                    elif randomNum < transitionProbability[2] + transitionProbability[4] + transitionProbability[5]:
                        transitionCount[5] += 1
                        state = DECELERATE
                        decelerateAction(file)
                    else:
                        state = ACCELERATE
                        accelerateAction(file)
                
                elif state == PULL_IN_AHEAD:
                    if randomNum < transitionProbability[8]:
                        transitionCount[8] += 1
                        state = DONE
                        doneAction(file)
                    else:
                        state = PULL_IN_AHEAD
                        pullInAheadAction(file)
                
                elif state == PULL_IN_BEHIND:
                    if randomNum < transitionProbability[6]:
                        transitionCount[6] += 1
                        state = FOLLOW
                        followAction(file)
                    else:
                        state = PULL_IN_BEHIND
                        pullInBehindAction(file)

                elif state == DECELERATE:
                    if randomNum < transitionProbability[7]:
                        transitionCount[7] += 1
                        state = PULL_IN_BEHIND
                        pullInBehindAction(file)
                    else:
                        state = DECELERATE
                        decelerateAction
                
                elif state == DONE:
                    print("Error: unexpected state=" + str(state), "\n")
                    break
                else:
                    print("Error: unexpected state=" + str(state), "\n")
                    break

        # Calculate state/transitions frequency
        total_count = sum(stateCount)
        stateFrequency = [(count / total_count) for count in stateCount]
        stateFrequency = [stateFrequency[i-1] for i in stateSequence]

        total_count = sum(transitionCount)
        transitionFrequency = [(count / total_count) for count in transitionCount]
        transitionFrequency = [transitionFrequency[i-1] for i in transitionSequence]

        # Write the end-of-simulation statisitics to the file
        # Note: Frequencies are rounded to the 3rd decimal place
        if scenarioTrace:
            file.write("\n----End Simulation----\n\n")
        file.write(f"scenario = {SCENARIO} \n")
        file.write(f"trace = {scenarioTrace} \n")
        file.write(f"iterations = {iterations} \n")
        file.write(f"transition probabilities = {transitionProbability} \n")
        file.write(f"state counts = {stateCount} \n")
        file.write(f"state frequency = {[round(freq, 3) for freq in stateFrequency]} \n")
        file.write(f"transition counts = {transitionCount} \n")
        file.write(f"transition frequency = {[round(freq, 3) for freq in transitionFrequency]} \n")

        file.close()


if __name__ == "__main__":
    main()