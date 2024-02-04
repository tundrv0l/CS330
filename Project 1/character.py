'''----------------- 
# Author: Parker Clark
# Date: 2/3/2024
# Description: A class for the 'Character' object.
-----------------'''
import vector
import math

#TODO: Make this file more dynamic for upcoming projects. Maybe rework init. Add better comments.

#---Constants---#
CONTINUE = 1
SEEK = 6
FLEE = 7
ARRIVE = 8

class Character:

    def __init__(self, id, steer, position=None, velocity=None, orientation=None, linear=None,
                 angular = None, maxVelocity=None, maxLinear=None, target=None, arriveRadius=None, 
                 arriveSlow=None, arriveTime=None, colCollided=False):
        '''
        Create a character object with default parameters.
        '''
        self.id = id
        self.steer = steer
        self.position = position
        self.velocity = velocity
        self.orientation = orientation
        self.linear = linear
        self.angular = angular
        self.maxVelocity = maxVelocity
        self.maxLinear = maxLinear
        self.target = target
        self.arriveRadius = arriveRadius
        self.arriveSlow = arriveSlow
        self.arriveTime = arriveTime
        self.colCollided = colCollided

    

#---Setup Characters---#

#---Character 1---#
'''
Character 1 sets up the 'continue' steering behavior.
May also consider this the 'origin' character.
'''
character_26_01 = Character(2601, CONTINUE)

#---Character 2---#
'''
Character 2 sets up the 'flee' steering behavior.
Its behavior should allow this character to 'fish hook' away from the origin.
'''
character_26_02 = Character(2602, FLEE)
character_26_02.position = [-30, -50]
character_26_02.velocity = vector.Vector(2, 7)
character_26_02.orientation = math.pi/4
character_26_02.maxVelocity = 8
character_26_02.maxLinear = 1.5
character_26_02.target = 1

#---Character 3---#
'''
Character 3 sets up the 'seek' steering behavior.
Its behavior should allow this character to 'orbit' the origin.
'''
character_26_03 = Character(2603, SEEK)
character_26_03.position = [-50, 40]
character_26_03.velocity = vector.Vector(0, 8)
character_26_03.orientation = (3*math.pi)/4
character_26_03.maxVelocity = 8
character_26_03.maxLinear = 2
character_26_03.target = 1

#---Character 4---#
'''
Character 4 sets up the 'arrive' steering behavior.
Its behavior should allow it to 'hit' the origin, by slowing down as it approaches.
'''
character_26_04 = Character(2604, ARRIVE)
character_26_04.position = [50, 75]
character_26_04.velocity = vector.Vector(-9, 4)
character_26_04.orientation = math.pi
character_26_04.maxVelocity = 10
character_26_04.maxLinear = 2
character_26_04.target = 1
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

# Plotting optins in order of: Position[0], Velocity[1], Linear[2],  Orientation[3], Paths[4], Collisions[5]
plotWhat = [True, True, True, False, False, False]
plotScale = [2.0, 2.0, 20]
plotCrossRefs = True

