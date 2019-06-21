from wpilib.command import Subsystem
from wpilib import Encoder
from wpilib import ADXRS450_Gyro
from wpilib import VictorSP
from wpilib import SmartDashboard
import RobotMap
import math

class DriveTrainSubsystem(Subsystem):

    def __init__(self):
        
        #Power output to motors in range of -1 to 1
        self.leftPower = 0
        self.rightPower = 0

        self.numberOfTicks = 2048
        self.wheelCircumference = 6*math.pi

        self.leftEncoder = Encoder(RobotMap.leftDriveEncoder1,RobotMap.leftDriveEncoder2,False,
        Encoder.EncodingType.k4X)
        self.rightEncoder = Encoder(RobotMap.rightDriveEncoder1,RobotMap.rightDriveEncoder2,True,
        Encoder.EncodingType.k4X)

        self.gyro = ADXRS450_Gyro()

        self.rightDriveMotor1 = VictorSP(RobotMap.rightDriveMotor1)
        self.rightDriveMotor2 = VictorSP(RobotMap.rightDriveMotor2)
        self.rightDriveMotor3 = VictorSP(RobotMap.rightDriveMotor3)

        self.leftDriveMotor1 = VictorSP(RobotMap.leftDriveMotor1)
        self.leftDriveMotor2 = VictorSP(RobotMap.leftDriveMotor2)
        self.leftDriveMotor3 = VictorSP(RobotMap.leftDriveMotor3)
        
        self.leftEncoder.setDistancePerPulse(wheelCircumference / numberOfTicks)
        self.rightEncoder.setDistancePerPulse(wheelCircumference / numberOfTicks)
        self.leftEncoder.setMaxPeriod(5)
        self.rightEncoder.setMaxPeriod(5)
        self.leftEncoder.setMinRate(0)
        self.rightEncoder.setMinRate(0)
        self.leftEncoder.setSamplesToAverage(1)
        self.rightEncoder.setSamplesToAverage(1)

        self.gyro.calibrate()

    #def initDefaultCommand(self):
        #self.setDefaultCommand(ArcadeDrive())

    def setLeftDrivePower(self,power):
        self.leftPower = power

    def setRightDrivePower(self,power):
        self.rightPower = power

    def updateMotorOutputs(self):
        self.leftDriveMotor1 = -leftPower
        self.leftDriveMotor2 = -leftPower
        self.leftDriveMotor3 = -leftPower
        
        self.rightDriveMotor1 = rightPower
        self.rightDriveMotor1 = rightPower
        self.rightDriveMotor1 = rightPower

    def putEncoderValues(self):
        self.SmartDashboard.putNumber("Left Encoder Raw", leftEncoder.getRaw())
        self.SmartDashboard.putNumber("Right Encoder Raw", rightEncoder.getRaw())
        self.SmartDashboard.putNumber("Left Encoder Dist Per Pulse", leftEncoder.getDistancePerPulse())
        self.SmartDashboard.putNumber("Right Encoder Dist Per Pulse", rightEncoder.getDistancePerPulse())

    def getLeftDistance(self):
        return self.leftEncoder.getDistance()

    def getRightDistance(self):
        return self.rightEncoder.getDistance()

    def resetGyro(self):
        self.gyro.reset()

    def resetEncoders(self):
        self.leftEncoder.reset()
        self.rightEncoder.reset()
    
    #def accelerateDrive(self):
        #if getLogitechLeftStickY() > 0:
            #return math.pow(getLogitechLeftStickY(),2)
        #else:
            #return -math.pow(getLogitechLeftStickY(),2)