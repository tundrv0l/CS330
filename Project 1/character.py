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

#---Timing globals---#
currentTime = 0.0 # Current time in the simulation. Begins at 0.
stopVelocity = 0.02 # The lower velocity limit on which the simulation should stop a character.

class Character:

    def __init__(self, id, steer, position=vector.Vector(0,0), velocity=vector.Vector(0,0), orientation=0, rotation=0, linear=vector.Vector(0,0),
                 angular=0, maxVelocity=0, maxLinear=0, maxRotation=0, maxAngular=0, arriveRadius=0, target=0, 
                 arriveSlow=0, arriveTime=0, colCollided=False):
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
character_26_02.position = vector.Vector(-30, -50)
character_26_02.velocity = vector.Vector(2, 7)
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
character_26_03.position = vector.Vector(-50, 40)
character_26_03.velocity = vector.Vector(0, 8)
character_26_03.orientation = (3*math.pi)/4
character_26_03.maxVelocity = 8
character_26_03.maxLinear = 2
character_26_03.target = character_26_01

#---Character 4---#
'''
Character 4 sets up the 'arrive' steering behavior.
Its behavior should allow it to 'hit' the origin, by slowing down as it approaches.
'''
character_26_04 = Character(2604, ARRIVE)
character_26_04.position = vector.Vector(50, 75)
character_26_04.velocity = vector.Vector(-9, 4)
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

