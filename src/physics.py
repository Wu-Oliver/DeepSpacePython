from hal_impl.data import hal_data as hal_data
from pyfrc.physics.core import PhysicsEngine
from pyfrc.physics.core import PhysicsInitException
from pyfrc.physics.core import PhysicsInterface 

class PhysicsInterface:
    
    def __init__(self):
        pass

    def add_analog_gyro_channel(self, ch):
        pass 

    def add_device_gyro_channel(self, angle_key):
        pass 

    def distance_drive(self, update_sim, x, y, angle):
        pass 

    

class PhysicsEngine:

    def __init__(self):
        self.TheEngine = PhysicsInterface()

    def initialize(self, hal_data):
        pass

    def cmToFeet(self, cm):
        feet = 0.3947 * cm
        return feet
    
            
    def update_sim(self , hal_data, now, tm_diff):
       
         
        self.TheEngine.distance_drive(5,2,4)

        
    




    

                