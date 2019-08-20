from wpilib.command import Command
from wpilib.smartdashboard import SmartDashboard
from accessories.PID import PID
from RobotMap import *
from robot import SpartanRobot
import OI

class AnalogArmCommand(Command):
    
    def __init__(self):
        
        self.rightTrigger = 0
        self.leftTrigger = 0

        self.error = 0
        
        self.lastArmAngle = 0

        self.armGravityPID = PID(ArmGravityP,ArmGravityI,ArmGravityD,
        ArmGravityFF)

        self.requires(SpartanRobot.arm)

        self.armGravityPID.setTargetPID(0)
        

    def execute(self):
       
        #SDB halt
        #self.armGravityPID(SmartDashboard.getNumber("ARM GRAVITY P:", ArmGravityP),
        #SmartDashboard.getNumber("ARM GRAVITY I:", ArmGravityP),
        #SmartDashboard.getNumber("ARM GRAVITY D:", ArmGravityP),
        #SmartDashboard.getNumber("ARM GRAVITY FF:", ArmGravityP))
        self.leftTrigger = OI()
        



