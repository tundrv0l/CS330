'''----------------- 
# Author: Parker Clark
# Date: 2/3/2024
# Description: A file that contains the movement functions for the characters.
-----------------'''

import character
import vector

#TODO: Add more movement functions. Fix the returnTrajectory function. Add main time loop.


#---Movement Functions---#
def dynamicGetSteeringContinue(character: character.Character) -> dict:
    '''
        A function that returns the current linear and angular acceleration.

        Parameters
        ----------
        character: Character
            The character object to return.

        Returns
        ----------
        result: dict
            A dictionary with the current linear and angular acceleration.
        '''
    return {'Current Linear Acceleration': character.linear, 'Current Angular Acceleration': character.angular}

#---Main time loop---#

def returnTrajectory(character: character.Character, time: float) -> str:
    '''
        A function that returns the trajectory of the character in a comma separated string.

        Parameters
        ----------
        character: Character
            The character object to write to the string.

        time: float
            The current time of the simulation.

        Returns
        ----------
        data: str
            A formatted string for the trajectory data file.
    '''

    data = f'{time},{character.id},{character.position[0]},{character.position[1]},{character.velocity.x},{character.velocity.y},{character.orientation[0]},{character.linear.x},{character.linear.y},{character.orientation},{character.steer},{character.colCollided}\n'