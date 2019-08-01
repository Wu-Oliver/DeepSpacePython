from wpilib.command import Subsystem
from wpilib import Encoder
from wpilib import ADXRS450_Gyro
from wpilib import VictorSP
from wpilib import SmartDashboard
from OI import OI
from RobotMap import *
import math

class DriveTrainSubsystem(Subsystem):

    def __init__(self):
        
        #Power output to motors in range of -1 to 1
        self.leftPower = 0
        self.rightPower = 0

        self.leftEncoder = Encoder(leftDriveEncoder1,leftDriveEncoder2,False,
        Encoder.EncodingType.k4X)
        self.rightEncoder = Encoder(rightDriveEncoder1,rightDriveEncoder2,True,
        Encoder.EncodingType.k4X)

        self.gyro = ADXRS450_Gyro()

        self.rightDriveMotor1 = VictorSP(rightDriveMotor1)
        self.rightDriveMotor2 = VictorSP(rightDriveMotor2)
        # self.rightDriveMotor3 = VictorSP(rightDriveMotor3)

        self.leftDriveMotor1 = VictorSP(leftDriveMotor1)
        self.leftDriveMotor2 = VictorSP(leftDriveMotor2)
        # self.leftDriveMotor3 = VictorSP(leftDriveMotor3)
        
        self.leftEncoder.setDistancePerPulse(wheelCircumference / numberOfTicks)
        self.rightEncoder.setDistancePerPulse(wheelCircumference / numberOfTicks)
        self.leftEncoder.setMaxPeriod(5)
        self.rightEncoder.setMaxPeriod(5)
        self.leftEncoder.setMinRate(0)
        self.rightEncoder.setMinRate(0)
        self.leftEncoder.setSamplesToAverage(1)
        self.rightEncoder.setSamplesToAverage(1)

        self.gyro.calibrate()

    # def initDefaultCommand(self):
    #     self.setDefaultCommand(ArcadeDrive())

    def setLeftDrivePower(self,power):
        self.leftPower = power

    def setRightDrivePower(self,power):
        self.rightPower = power

    def updateMotorOutputs(self):
        self.leftDriveMotor1 = -self.leftPower
        self.leftDriveMotor2 = -self.leftPower
        # self.leftDriveMotor3 = -self.leftPower
        
        self.rightDriveMotor1 = self.rightPower
        self.rightDriveMotor2 = self.rightPower
        # self.rightDriveMotor3 = self.rightPower

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
    
    def accelerateDrive(self):
        if self.getSecondaryControllerLeftStickY() > 0:
            return math.pow(self.getSecondaryControllerLeftStickY(), 2)
        else:
            return -math.pow(self.getSecondaryControllerLeftStickY(), 2)