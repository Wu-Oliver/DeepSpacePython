from wpilib.command import Subsystem
from src.python.frc.robot.RobotMap import RobotMap
from wpilib import PWMTalonSRX


class WristSubsystem(Subsystem):

    def __init__(self):
        
        self.encoderUnit = 4096
        self.gearRatio = 183.33333333
        
        self.lowerAngleLimit = -10
        self.topAngleLimit = 170
        
        self.wristPower = 0
        self.wristMotor = PWMTalonSRX(RobotMap.wristMotor)
    #def initDefaultCommand(self):
     #   self.setDefaultCommand(AnalogWristCommand())
    
