'''----------------- 
# Author: Parker Clark
# Date: 1/25/2024
# Description: A class that holds stub states.
-----------------'''


class State:

    def __init__(self, id):
        '''
        Constructor: Creates a state object. 

        Members
        ----------
        name: const int
            The state's identifier.
        '''

        self.id = id

    
    def action(self, stateCount : list):
        '''
        Stub function that prints the name of the state.
        '''
        stateCount[self.id-1] += 1
        return stateCount[self.id-1]
