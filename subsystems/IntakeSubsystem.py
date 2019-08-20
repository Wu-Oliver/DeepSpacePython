from wpilib.command import Subsystem
from wpilib import VictorSP
from RobotMap import *

class IntakeSubsystem(Subsystem):
    
    def __init__(self):

        self.intakeLeft = VictorSP(intakeLeft)   
        self.intakeRight = VictorSP(intakeRight)
  
    #def initDefaultCommand(self):
        #self.setDefaultCommand(AnalogIntakeCommand())

    def setIntakePower(self, power):
        self.intakeLeft.set(power)
        self.intakeRight.set(power)