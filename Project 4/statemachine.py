'''----------------- 
# Author: Parker Clark
# Date: 1/25/2024
# Description: A program that simulates a simple state machine.
-----------------'''

#---Imports---#
import random
from state import State

#---File Constants---#
FOLLOW = 1
PULL_OUT = 2
ACCELERATE = 3
PULL_IN_AHEAD = 4
PULL_IN_BEHIND = 5
DECELERATE = 6
DONE = 7

#---Script Variables---#
SCENARIO = 1
iterations = [100, 1000000][SCENARIO-1]
transitionProbability = [[0.8, 0.4, 0.3, 0.4, 0.3, 0.8, 0.8],
                         [0.9, 0.6, 0.3, 0.2, 0.4, 0.7, 0.9, 0.7]][SCENARIO-1]
stateCount = [0, 0, 0, 0, 0, 0, 0]
transitionCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]


# Main function
def main():


    # Create a list of states
    for i in range(1, iterations+1):
        state = FOLLOW
        State(FOLLOW).action(stateCount)

        while state != DONE:
            randomNum = random.uniform(0, 1)

            if state == FOLLOW:
                if randomNum < transitionProbability[0]:
                    transitionCount[0] += 1
                    state = PULL_OUT
                    State(PULL_OUT).action(stateCount)
                else:
                    state = FOLLOW
                    State(FOLLOW).action(stateCount)
            
            elif state == PULL_OUT:
                if randomNum < transitionProbability[1]:
                    transitionCount[1] += 1
                    state = ACCELERATE
                    State(ACCELERATE).action(stateCount)
                elif randomNum < transitionProbability[1] + transitionProbability[3]:
                    transitionCount[2] += 1
                    state = PULL_IN_BEHIND
                    State(PULL_IN_BEHIND).action(stateCount)
                else:
                    state = PULL_OUT
                    State(PULL_OUT).action(stateCount)

            elif state == ACCELERATE:
                if randomNum < transitionProbability[2]:
                    transitionCount[2] += 1
                    state = PULL_IN_AHEAD
                    State(PULL_IN_AHEAD).action(stateCount)
                elif randomNum < transitionProbability[2] + transitionProbability[4]:
                    transitionCount[4] += 1
                    state = PULL_IN_BEHIND
                    State(PULL_IN_BEHIND).action(stateCount)
                elif randomNum < transitionProbability[2] + transitionProbability[4] + transitionProbability[5]:
                    transitionCount[5] += 1
                    state = DECELERATE
                    State(DECELERATE).action(stateCount)
                else:
                    state = ACCELERATE
                    State(ACCELERATE).action(stateCount)
            
            elif state == PULL_IN_AHEAD:
                if randomNum < transitionProbability[8]:
                    transitionCount[8] += 1
                    state = DONE
                    State(DONE).action(stateCount)
                else:
                    state = PULL_IN_AHEAD
                    State(PULL_IN_AHEAD).action(stateCount)
            
            elif state == PULL_IN_BEHIND:
                if randomNum < transitionProbability[6]:
                    transitionCount[6] += 1
                    state = FOLLOW
                    State(FOLLOW).action(stateCount)
                else:
                    state = PULL_IN_BEHIND
                    State(PULL_IN_BEHIND).action(stateCount)

            elif state == DECELERATE:
                if randomNum < transitionProbability[7]:
                    transitionCount[7] += 1
                    state = PULL_IN_BEHIND
                    State(PULL_IN_BEHIND).action(stateCount)
                else:
                    state = DECELERATE
                    State(DECELERATE).action(stateCount)
            
            elif state == DONE:
                print("Error: unexpected state=" + str(state), "\n")
                break
            else:
                print("Error: unexpected state=" + str(state), "\n")
                break

    # Calculate state/transitions frequency









if __name__ == "__main__":
    main()