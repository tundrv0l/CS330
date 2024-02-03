'''----------------- 
# Author: Parker Clark
# Date: 2/3/2024
# Description: A class for the 'Character' object.
-----------------'''

class Character:

    def __init__(self, id, steer, position=None, velocity=None, orientation=None, 
                 max_velocity=None, max_linear=None, target=None, arrive_radius=None, 
                 arrive_slow=None, arrive_time=None):
        '''
        Create a character object with default parameters.
        '''
        self.id = id
        self.steer = steer
        self.position = position
        self.velocity = velocity
        self.orientation = orientation
        self.max_velocity = max_velocity
        self.max_linear = max_linear
        self.target = target
        self.arrive_radius = arrive_radius
        self.arrive_slow = arrive_slow
        self.arrive_time = arrive_time