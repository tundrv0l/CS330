'''----------------- 
# Author: Parker Clark
# Date: 2/3/2024
# Description: A file that contains the movement functions for the characters.
-----------------'''

#---Imports---#
import character
from character import *
from utility import *
import math

#---Constants---#
dataFile = 'trajectory_data.txt'

#---Define return structure class---#
class SteeringOutput:
    '''
    A class that contains the return linear and angular acceleration from a movement function.
    '''
    def __init__(self, linear = Vector(0,0), angular= 0):
        '''
        Create a steering output object with default parameters.
        '''
        self.linear = linear
        self.angular = angular


#---Movement Functions---#
def dynamicGetSteeringContinue(character: Character) -> SteeringOutput:
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
    
    # Create a new steering output object, and return the current values.
    result = SteeringOutput(character.linear, character.angular)
    return result

def dynamicGetSteeringSeek(character: Character, target: Character) -> SteeringOutput:
    '''
        A function that implements the 'Seek' Algorithm.

        Parameters
        ----------
        character: Character
            The character object that is  the 'seeker'.

        target: Character
            The target character object to seek.

        Returns
        ----------
        result: SteeringOutput
            A structure with the updated linear and angular acceleration.
        '''
    
    # Create a new steering output object
    result = SteeringOutput()

    # Calculate the direction to the target, normalize it, and scale it to the max linear speed.
    result.linear = target.position - character.position
    result.linear.normalize()
    result.linear *=  character.maxLinear

    # Set angular to 0 and return the steering output
    result.angular = 0
    return result

def dynamicGetSteeringFlee(character: Character, target: Character) -> SteeringOutput:
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
    
    # Create a new steering output object
    result = SteeringOutput()

    # Calculate the direction away from the target, scale and normalize it to the max linear speed
    result.linear = character.position - target.position
    result.linear.normalize()
    result.linear *= character.maxLinear

    # Set angular to 0 and return the steering output
    result.angular = 0
    return result
    
def dynamicGetSteeringArrive(character: Character, target: Character) -> SteeringOutput:
    '''
        A function that implements the 'Arrive' algorithm.

        Parameters
        ----------
        character: Character
            The character object that is arriving.

        target: Character, optional
            The target character object that the character is 'arriving' at.
            Default value is character_26_01.

        Returns
        ----------
        result: SteeringOutput
            A structure with the updated linear and angular acceleration.
    '''
    
    # Create a new steering output object
    result = SteeringOutput()

    # Calculate the direction to the target
    direction = target.position - character.position
    distance = direction.getLength()

    # Check to see if the character is within the arrive radius
    if distance < character.arriveRadius:
        targetSpeed = 0
    elif distance > character.arriveSlow:
        targetSpeed = character.maxVelocity
    else:
        targetSpeed = character.maxVelocity * distance / character.arriveSlow
    
    # Scale the direction to the target to the target speed
    direction.normalize()
    targetVelocity = direction * targetSpeed

    # calculate the linear acceleration
    result.linear = targetVelocity - character.velocity
    result.linear /= character.arriveTime

    # Check to see if the linear acceleration is above the max linear speed
    if result.linear.getLength() > character.maxLinear:
        result.linear.normalize()
        result.linear *= character.maxLinear
    
    # Return the steering output
    result.angular = 0
    return result


#---Support functions---#

def getSign(value: float) -> int:
    '''
        A function that returns the sign of a value.

        Parameters
        ----------
        value: float
            The value to check the sign of.

        Returns
        ----------
        sign: int
            An int representing the sign of the value.
    '''

    return 0 if value == 0 else int(math.copysign(1, value))

def dynamicUpdate(character: Character, steering: SteeringOutput, deltaTime: float, physics: bool) -> Character:
    '''
        A function that returns the sign of a value.

        Parameters
        ----------
        character: Character
            The character object to update.

        steering: SteeringOutput
            The steering output object to update the character with.
        
        deltaTime: float
            The current time step for the simulation.
        
        physics: bool
            A boolean value to determine which physics model to use. True for HS Physics, False for Newton-Euler 1.

        Returns
        ----------
        character: Character
            An updated character object.
    '''

    # Check to see what type of physics to use
    if physics: # HS Physics
        half_t_sq = 0.5 * deltaTime * deltaTime
        character.position += (character.velocity * deltaTime) + (steering.linear * half_t_sq)
        character.orientation += (character.rotation * deltaTime) + (steering.angular * half_t_sq)
    else: # Newton-Euler 1
        character.position += (character.velocity * deltaTime)
        character.orientation += (character.rotation * deltaTime)
    
    # Correct character orientation
    character.orientation = character.orientation % (2 * math.pi)

    # Update the velocity and rotation
    character.velocity += (steering.linear * deltaTime)
    character.rotation += (steering.angular * deltaTime)

    # Update the linear and angular acceleration
    character.linear = steering.linear
    character.angular = steering.angular

    # Run checks for off-nominal conditions

    if character.velocity.getLength() > character.maxVelocity:
        character.velocity.normalize()
        character.velocity *= character.maxVelocity

    # Check to see if the velocity is below tolerance
    if character.velocity.getLength() < stopVelocity:
        character.velocity.null()
    
    # Check to see if linear acceleration is above tolerance
    if character.linear.getLength() > character.maxLinear:
        character.linear.normalize()
        character.linear *= character.maxLinear
    
    # Check to see if rotation is above tolerance
    if character.rotation < 0.01:
        character.rotation = 0
    
    # Check to see if the angular acceleration is above tolerance
    if character.angular > character.maxAngular:
        character.angular = character.maxAngular * getSign(character.angular)
    
    return character
    

def returnTrajectory(character: Character, time: float) -> str:
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

    data = f'{time},{character.id},{character.position.x},{character.position.y},{character.velocity.x},{character.velocity.y},{character.linear.x},{character.linear.y},{character.orientation},{character.steer},{character.colCollided}\n'
    return data

#---Write initial trajectory data to file---#
outputFile = open(dataFile, 'w')

for character in characterList:
    outputFile.write(returnTrajectory(character, currentTime))

#---Main time loop---#
while currentTime < stopTime:

    # Increment the time
    currentTime += deltaTime

    for character in characterList:
        
        # Check the iterated character's steering behavior
        if character.steer == CONTINUE:
            steering = dynamicGetSteeringContinue(character)
        elif character.steer == SEEK:
            steering = dynamicGetSteeringSeek(character, character.target)
        elif character.steer == FLEE:
            steering = dynamicGetSteeringFlee(character, character.target)
        elif character.steer == ARRIVE:
            steering = dynamicGetSteeringArrive(character, character.target)

        # Update the character's position and velocity
            
        # Write the character's trajectory to the file
        character = dynamicUpdate(character, steering, deltaTime, physics)

        outputFile.write(returnTrajectory(character, currentTime))

outputFile.close()