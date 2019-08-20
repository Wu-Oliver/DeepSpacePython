from wpilib.command import Subsystem
from RobotMap import *
from wpilib import Compressor
from wpilib import Solenoid

class PneumaticsSubsystem(Subsystem):

    def __init__(self):
        
        self.mainCompressor = Compressor(PCMID)
        self.intakeSolenoid = Solenoid(PCMID, intakeSolenoidChannel)
        self.isExtended = False

        self.mainCompressor.start()

    def initDefaultCommand(self):
        pass

    def flipSolenoid(self):
        if self.isExtended == False:
            self.isExtended = True
        else:
            self.isExtended == False
        
        self.intakeSolenoid.set(isExtended)

    def getIsExtended(self):
        return self.isExtended



    