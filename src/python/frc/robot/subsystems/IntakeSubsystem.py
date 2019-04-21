from wpilib.command import Subsystem
from wpilib import VictorSP
from src.python.frc.robot.RobotMap import RobotMap

class IntakeSubsystem(Subsystem):
    
    def __init__(self):

        self.intakeLeft = VictorSP(RobotMap.intakeLeft)   
        self.intakeRight = VictorSP(RobotMap.intakeRight)
  
    #def initDefaultCommand(self):
        #self.setDefaultCommand(AnalogIntakeCommand())

    def setIntakePower(self,power):
        self.intakeLeft.set(power)
        self.intakeRight.set(power)