from wpilib.command import Subsystem
from wpilib import Encoder
from wpilib import ADXRS450_Gyro
from wpilib import VictorSP
import accessories
from wpilib import SmartDashboard
from commands.ArcadeDriveCommand import ArcadeDriveCommand
from robot import SpartanRobot
import RobotMap
import math

class DriveTrainSubsystem(Subsystem):

    def __init__(self):
        self.robot = SpartanRobot.getRobotObject(self)
        
        #Power output to motors in range of -1 to 1
        self.leftPower = 0
        self.rightPower = 0

        self.leftEncoder = Encoder(RobotMap.leftDriveEncoder1, RobotMap.leftDriveEncoder2, False,
        Encoder.EncodingType.k4X)
        self.rightEncoder = Encoder(RobotMap.rightDriveEncoder1, RobotMap.rightDriveEncoder2, True,
        Encoder.EncodingType.k4X)

        self.gyro = ADXRS450_Gyro()

        self.rightDriveMotor1 = VictorSP(RobotMap.rightDriveMotor1)
        self.rightDriveMotor2 = VictorSP(RobotMap.rightDriveMotor2)
        # self.rightDriveMotor3 = VictorSP(rightDriveMotor3)

        self.leftDriveMotor1 = VictorSP(RobotMap.leftDriveMotor1)
        self.leftDriveMotor2 = VictorSP(RobotMap.leftDriveMotor2)
        # self.leftDriveMotor3 = VictorSP(leftDriveMotor3)
        
        self.leftEncoder.setDistancePerPulse(RobotMap.wheelCircumference / RobotMap.numberOfTicks)
        self.rightEncoder.setDistancePerPulse(RobotMap.wheelCircumference / RobotMap.numberOfTicks)
        self.leftEncoder.setMaxPeriod(5)
        self.rightEncoder.setMaxPeriod(5)
        self.leftEncoder.setMinRate(0)
        self.rightEncoder.setMinRate(0)
        self.leftEncoder.setSamplesToAverage(1)
        self.rightEncoder.setSamplesToAverage(1)

        self.gyro.calibrate()

    def initDefaultCommand(self):
        self.setDefaultCommand(ArcadeDriveCommand())
        
    def setLeftDrivePower(self, power):
        self.leftPower = power

    def setRightDrivePower(self, power):
        self.rightPower = power

    def updateMotorOutputs(self):
        self.leftDriveMotor1 = -self.leftPower
        self.leftDriveMotor2 = -self.leftPower
        # self.leftDriveMotor3 = -self.leftPower
        
        self.rightDriveMotor1 = self.rightPower
        self.rightDriveMotor2 = self.rightPower
        # self.rightDriveMotor3 = self.rightPower

    def putEncoderValues(self):
        SmartDashboard.putNumber("Left Encoder Raw", self.leftEncoder.getRaw())
        SmartDashboard.putNumber("Right Encoder Raw", self.rightEncoder.getRaw())
        SmartDashboard.putNumber("Left Encoder Dist Per Pulse", self.leftEncoder.getDistancePerPulse())
        SmartDashboard.putNumber("Right Encoder Dist Per Pulse", self.rightEncoder.getDistancePerPulse())

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
        if self.robot.oi.xBoxController.getRawAxis(1) > 0:
            return math.pow(self.robot.oi.xBoxController.getRawAxis(1), 2)
        else:
            return -math.pow(self.robot.oi.xBoxController.getRawAxis(1), 2)
            