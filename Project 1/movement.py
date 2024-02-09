'''----------------- 
# Author: Parker Clark
# Date: 2/3/2024
# Description: A file that contains the movement functions for the characters.
-----------------'''

#---Imports---#
import character
from character import *
import vector
import math

#TODO:Add main time loop. make file handling not nuke everything after its closed. Move niche functions elsewhere. Run a test. Add warnings for update

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
    
    # Create a new steering output object, and return the current values.
    result = SteeringOutput(character.linear, character.angular)
    return result

def dynamicGetSteeringSeek(character: character.Character, target: character.Character) -> SteeringOutput:
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
    result = SteeringOutput(vector.Vector(0,0), 0.0)

    # Calculate the direction to the target, normalize it, and scale it to the max linear speed.
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
    
    # Create a new steering output object
    result = SteeringOutput(vector.Vector(0,0), 0.0)

    # Calculate the direction away from the target, scale and normalize it to the max linear speed.
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
    
    # Create a new steering output object. Normalize a direction vector to the target.
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

def dynamicUpdate(character: character.Character, steering: SteeringOutput, deltaTime: float, physics: bool) -> Character:

    # Check to see what type of physics to use
    if physics: # HS Physics
        half_t_sq = 0.5 * deltaTime * deltaTime
        character.position += character.velocity * deltaTime + steering.linear * half_t_sq
        character.orientation += character.rotation * steering.angular * half_t_sq
    else: # Newton-Euler 1
        character.position += character.velocity * deltaTime
        character.orientation += character.rotation * deltaTime
    
    # Correct character orientation
    character.orientation = character.orientation % (2 * math.pi)

    # Update the velocity and rotation
    character.velocity += steering.linear * deltaTime
    character.rotation += steering.angular * deltaTime

    # Update the linear and angular acceleration
    character.linear = steering.linear
    character.angular = steering.angular

    # Run checks for off-nominal conditions

    # Check to see if the velocity is below tolerance
    if character.velocity.getLength() < stopVelocity:
        character.velocity.null()
    
    # Check to see if linear acceleration is above tolerance
    if character.linear.getLength() > character.maxLinear:
        character.linear.normalize()
        character.linear *= character.maxLinear
    
    # Check to see if rotation is above tolerance
    if character.rotation > character.maxRotation:
        character.rotation = character.maxRotation * getSign(character.rotation)
    
    # Check to see if the angular acceleration is above tolerance
    if character.angular > character.maxAngular:
        character.angular = character.maxAngular * getSign(character.angular)
    
    return character
    

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

    data = f'{time},{character.id},{character.position.x},{character.position.y},{character.velocity.x},{character.velocity.y},{character.linear.x},{character.linear.y},{character.orientation},{character.steer},{character.colCollided}\n'
    return data

#---Write initial trajectory data to file---#
for element in characterList:
    with open('trajectory_data.txt', 'a') as f:
        f.write(returnTrajectory(element, currentTime))

#---Main time loop---#
while currentTime < stopTime:

    # Increment the time
    currentTime += deltaTime

    for element in characterList:
        
        # Check the iterated character's steering behavior
        if element.steer == CONTINUE:
            steering = dynamicGetSteeringContinue(element)
        elif element.steer == SEEK:
            steering = dynamicGetSteeringSeek(element, element.target)
        elif element.steer == FLEE:
            steering = dynamicGetSteeringFlee(element, element.target)
        elif element.steer == ARRIVE:
            steering = dynamicGetSteeringArrive(element, element.target)

        #TODO: Add update function for time loop
            
    for element in characterList:
        with open('trajectory_data.txt', 'a') as f:
            f.write(returnTrajectory(element, currentTime))