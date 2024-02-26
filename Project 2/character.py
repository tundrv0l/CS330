'''----------------- 
# Author: Parker Clark
# Date: 2/3/2024
# Description: A class for the 'Character' object.
-----------------'''

#---Imports---#
from utility import Vector
from path import Path
import math

#---Constants---#
CONTINUE = 1
SEEK = 6
FLEE = 7
ARRIVE = 8
FOLLOW_PATH = 11

''' 
The scenario number for the current project.
--------------------------------------------
Program Assignment 1: 26
Program Assignment 2: 27
'''
scenario = 27

#---Timing globals---#
currentTime = 0.0 # Current time in the simulation. Begins at 0.
stopVelocity = 0.02 # The lower velocity limit on which the simulation should stop a character.

class Character:

    def __init__(self, id, steer, position=Vector(0,0), velocity=Vector(0,0), orientation=0, rotation=0, linear=Vector(0,0),
                 angular=0, maxVelocity=0, maxLinear=0, maxRotation=0, maxAngular=0, arriveRadius=0, target=0, 
                 arriveSlow=0, arriveTime=0, colCollided=False, pathToFollow=0, pathOffset=0):
        '''
        Create a character object with default parameters.
        '''
        self.id = id
        self.steer = steer
        self.position = position
        self.velocity = velocity
        self.orientation = orientation
        self.rotation = rotation
        self.linear = linear
        self.angular = angular
        self.maxVelocity = maxVelocity
        self.maxLinear = maxLinear
        self.maxRotation = maxRotation
        self.maxAngular = maxAngular
        self.target = target 
        self.arriveRadius = arriveRadius
        self.arriveSlow = arriveSlow
        self.arriveTime = arriveTime
        self.colCollided = colCollided
        self.pathToFollow = pathToFollow
        self.pathOffset = pathOffset

#---Setup Characters---#


if (scenario == 26):
    #---Character 1---#
    '''
    Character 1 sets up the 'continue' steering behavior.
    May also consider this the 'origin' character that the other characters target.
    '''
    character_26_01 = Character(2601, CONTINUE)

    #---Character 2---#
    '''
    Character 2 sets up the 'flee' steering behavior.
    Its behavior should allow this character to 'fish hook' away from the origin.
    '''
    character_26_02 = Character(2602, FLEE)
    character_26_02.position = Vector(-30, -50)
    character_26_02.velocity = Vector(2, 7)
    character_26_02.orientation = math.pi/4
    character_26_02.maxVelocity = 8
    character_26_02.maxLinear = 1.5
    character_26_02.target = character_26_01

    #---Character 3---#
    '''
    Character 3 sets up the 'seek' steering behavior.
    Its behavior should allow this character to 'orbit' the origin.
    '''
    character_26_03 = Character(2603, SEEK)
    character_26_03.position = Vector(-50, 40)
    character_26_03.velocity = Vector(0, 8)
    character_26_03.orientation = (3*math.pi)/2
    character_26_03.maxVelocity = 8
    character_26_03.maxLinear = 2
    character_26_03.target = character_26_01

    #---Character 4---#
    '''
    Character 4 sets up the 'arrive' steering behavior.
    Its behavior should allow it to 'hit' the origin, by slowing down as it approaches.
    '''
    character_26_04 = Character(2604, ARRIVE)
    character_26_04.position = Vector(50, 75)
    character_26_04.velocity = Vector(-9, 4)
    character_26_04.orientation = math.pi
    character_26_04.maxVelocity = 10
    character_26_04.maxLinear = 2
    character_26_04.target = character_26_01
    character_26_04.arriveRadius = 4
    character_26_04.arriveSlow = 32
    character_26_04.arriveTime = 1

    #---Other Scenario Variables---#
    characterList = [character_26_01, character_26_02, character_26_03, character_26_04]
    characterCount = 4

    #---Simulation Variables---#
    physics = False #True for HS Physics, False for Newton-Euler 1 integration.
    deltaTime = 0.50 # Time step duration (in seconds)
    stopTime = 50 # Time to stop the simulation (in seconds)
    checkCollisions = False

    #---Plot Variables---#

    # Plotting options in order of: Position[0], Velocity[1], Linear[2],  Orientation[3], Paths[4], Collisions[5]
    plotWhat = [True, True, True, False, False, False]
    plotScale = [2.0, 2.0, 20]
    plotCrossRefs = True

elif (scenario == 27):
    #---Character 1---#
    '''
    Character 1 sets up the 'follow path' steering behavior.
    It is the only character in this scenario, and should 'wind' around the plot.
    '''
    character_27_01 = Character(2701, FOLLOW_PATH)
    character_27_01.position = Vector(20, 95)
    character_27_01.velocity = Vector(0, 0)
    character_27_01.orientation = 0
    character_27_01.maxVelocity = 4
    character_27_01.maxLinear = 2
    character_27_01.pathToFollow = 1
    character_27_01.pathOffset = 0.04

    #---Other Scenario Variables---#
    characterList = [character_27_01]
    characterCount = 1

    #---Path Variables---#
    path_27_01 = Path(2701, [0, -20, 20, -40, 40. -60, 60, 0], [90, 65, 40, 15, -10, -35, -60, -85])
    pathList = [path_27_01] # NOTE: Might need to change this

    #---Simulation Variables---#
    physics = False #True for HS Physics, False for Newton-Euler 1 integration.
    deltaTime = 0.50 # Time step duration (in seconds)
    stopTime = 120 # Time to stop the simulation (in seconds)
    checkCollisions = False

    #---Plot Variables---#

    # Plotting options in order of: Position[0], Velocity[1], Linear[2],  Orientation[3], Paths[4], Collisions[5]
    plotWhat = [True, True, True, False, True, False]
    plotScale = [4.0, 4.0, 40]
    plotCrossRefs = True
