from wpilib.command import Subsystem
from ctre.basemotorcontroller import BaseMotorController
from ctre.talonsrx import TalonSRX
from src.python.frc.robot.RobotMap import RobotMap
class WristSubsystem(Subsystem):

    def __init__(self):
        
        self.encoderUnit = 4096
        self.gearRatio = 183.33333333
        
        self.lowerAngleLimit = -10
        self.topAngleLimit = 170
        
        self.wristPower = 0
        self.wristMotor = TalonSRX(RobotMap.wristMotor)

        self.wristMotor.configSelectedFeedbackSensor(wristMotor.FeedbackDevice.CTRE_MagEncoder_Relative,0,0)
        self.wristMotor.setSensorPhase(False)
    #def initDefaultCommand(self):
     #   self.setDefaultCommand(AnalogWristCommand())
    
    def getWristDistanceTicks(self):
        return self.wristMotor.getSelectedSensorPosition()
    
    def getRotationAngle(self):
        return ((self.wristMotor.getSelectedSensorPosition()/self.encoderUnit)*(1/self.gearRatio)*360)
    
    #def isWristTopLimit(self):

    #def isWristBottomLimit(self):

    def setWristPower(self,power):
        if getRotationAngle() >= self.topAngleLimit or getRotationAngle() <= self.lowerAngleLimit:
            wristPower = 0
        else:
            wristPower = power

    def updateOutputs(self):
        self.wristMotor.set(BaseMotorController.ControlMode.PercentOutput, self.wristPower * 
        RobotMap.wristSpeedMultiplier)