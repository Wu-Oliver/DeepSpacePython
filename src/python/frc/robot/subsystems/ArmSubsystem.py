from wpilib.command import Subsystem
from rev._impl import CANEncoder
from rev._impl.autogen.sim import MotorType
from rev import CANSparkMax
from wpilib import DigitalInput
from src.python.frc.robot.RobotMap import RobotMap
import math

class ArmSubsystem(Subsystem):
    
    def __init__(self):

        self.encoderUnit = 4096
        self.gearRatio = 93.33

        self.armSpeedMultiplier = 1

        self.armBottomLimit = 5
        self.armUpperLimit = 200

        self.resetValue = 0

        self.bottomLimitSwitch = DigitalInput(RobotMap.ArmLimitSwitch)

        self.armMotor1 = CANSparkMax(RobotMap.armBaseMotor1,MotorType.kBrushless)
        self.armMotor2 = CANSparkMax(RobotMap.armBaseMotor2,MotorType.kBrushless)

        self.armEncoder1 = CANEncoder(armMotor1)
        self.armEncoder2 = CANEncoder(armMotor2)

        self.currentArmPower = 0
        self.isOverride = False

    #def initDefaultCommand(self):
     #   self.setDefaultCommand(AnalogArmCommand())
    
    def getDistanceTicks(self):
        return ((self.armEncoder1.getPosition() + self.armEncoder2.getPosition()) / 2) - resetValue

    def getArmMotor1Pos(self):
        return self.armEncoder1.getPosition
    
    def getArmMotor2Pos(self):
        return self.armEncoder2.getPosition

    def getRotationAngle(self):
        return (getDistanceTicks()/108) * -360

    def updateBottomLimit(self):
        if not self.bottomLimitSwitch.get():
            self.armBottomLimit = getRotationAngle()

    def isArmAtBottom(self):
        updateBottomLimit()
        if (getRotationAngle() >= (armBottomLimit - 2) and getRotationAngle() <= (armBottomLimit + 2):
            return True
        else:
            return False

    def isArmAtTop(self):
        return False

    def getLimitSwitch(self):
        return not self.bottomLimitSwitch.get()

    def setArmPower(self,power):
        if isArmAtBottom() and power > 0:
            self.currentArmPower = 0
        else:
            self.currentArmPower = power
    
    def setArmPowerOverride(self,power):
        if isOverride:
            self.currentArmPower = power

    def updateOutputs(self):
        self.armMotor1.set(currentArmPower * RobotMap.armSpeedMultiplier)
        self.armMotor2.set(currentArmPower * RobotMap.armSpeedMultiplier)

    def getGravityCompensation(self):
        if getRotationAngle() <= 3: return 0
        else: return math.sin(getRotationAngle() + 25)