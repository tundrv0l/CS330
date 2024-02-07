'''----------------- 
# Author: Parker Clark
# Date: 2/3/2024
# Description: A file that contains the movement functions for the characters.
-----------------'''

import character
import vector

#TODO: Add more movement functions. Fix the returnTrajectory function. Add main time loop.

#---Define return structure class---#
class SteeringOutput:
    '''
    A class that contains the return linear and angular acceleration from a movement function.
    '''
    def __init__(self, linear: vector.Vector, angular: float):
        '''
        Create a steering output object with default parameters.
        '''
        self.linear = linear
        self.angular = angular


#---Movement Functions---#
def dynamicGetSteeringContinue(character: character.Character) -> SteeringOutput:
    '''
        A function that returns the current linear and angular acceleration.

        Parameters
        ----------
        character: Character
            The character object to return.

        Returns
        ----------
        result: SteeringOutput
            A structure with the current linear and angular acceleration.
        '''
    result = SteeringOutput(character.linear, character.angular)
    return result

def dynamicGetSteeringSeek(character: character.Character, target: character.Character) -> SteeringOutput:
    '''
        A function that implements the 'Seek' Algorithm.

        Parameters
        ----------
        character: Character
            The character object that is seeking.

        target: Character
            The target character object to seek.

        Returns
        ----------
        result: SteeringOutput
            A structure with the updated linear and angular acceleration.
        '''
    result = SteeringOutput(vector.Vector(0,0), 0.0)
    result.linear = target.position - character.position
    result.linear.normalize()
    result.linear = result.linear * character.maxLinear
    result.angular = 0.0
    return result

def dynamicGetSteeringFlee(character: character.Character, target: character.Character) -> SteeringOutput:
    '''
        A function that implements the 'Flee' algorithm.

        Parameters
        ----------
        character: Character
            The character object that is fleeing.

        target: Character
            The target character object to flee from.

        Returns
        ----------
        result: SteeringOutput
            A structure with the updated linear and angular acceleration.
        '''
    result = SteeringOutput(vector.Vector(0,0), 0.0)
    result.linear = character.position - target.position
    result.linear.normalize()
    result.linear = result.linear * character.maxLinear
    result.angular = 0.0
    return result
    
def dynamicGetSteeringArrive(character: character.Character, target: character.Character) -> SteeringOutput:
    '''
        A function that implements the 'Arrive' algorithm.

        Parameters
        ----------
        character: Character
            The character object that is arriving.

        target: Character
            The target character object that the character is 'arriving' at.

        Returns
        ----------
        result: SteeringOutput
            A structure with the updated linear and angular acceleration.
        '''
    
    result = SteeringOutput(vector.Vector(0,0), 0.0)
    direction = target.position - character.position
    distance = direction.normalize()
    # Check the to see if the character is within the arrive radius
    if distance < character.arriveRadius:
        targetSpeed = 0
    elif distance > character.arriveSlow:
        targetSpeed = character.maxVelocity
    else:
        targetSpeed = character.maxVelocity * (distance / character.arriveSlow)
    
    #Calculate target velocity
    targetVelocity = direction
    targetVelocity.normalize()
    targetVelocity *= targetSpeed

    #Accelerate up torwards the target
    result.linear = targetVelocity - character.velocity
    result.linear /= character.arriveTime

    # Run a check to see if the acceleration is too fast
    if result.linear.getLength() > character.maxLinear:
        result.linear.normalize()
        result.linear *= character.maxLinear
    
    #Set the angular to 0
    result.angular = 0.0
    return result

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