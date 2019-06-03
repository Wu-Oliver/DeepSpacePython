from wpilib.command import Command
from wpilib.smartdashboard import SmartDashboard
from src.python.frc.robot.accessories.PID import PID
from src.python.frc.robot.RobotMap import RobotMap
from src.python.frc.robot.Robot import SpartanRobot
from src.python.frc.robot.OI import OI

class AnalogArmCommand(Command):
    
    def __init__(self):
        
        self.rightTrigger = 0
        self.leftTrigger = 0

        self.error = 0

        self.lastArmAngle = 0

        self.armGravityPID = PID(RobotMap.ArmGravityP,RobotMap.ArmGravityI,RobotMap.ArmGravityD,
        RobotMap.ArmGravityFF)

        self.requires(SpartanRobot.arm)

        self.armGravityPID.setTargetPID(0)
        

    def execute(self):
       
        #SDB halt
        #self.armGravityPID(SmartDashboard.getNumber("ARM GRAVITY P:", RobotMap.ArmGravityP),
        #SmartDashboard.getNumber("ARM GRAVITY I:", RobotMap.ArmGravityP),
        #SmartDashboard.getNumber("ARM GRAVITY D:", RobotMap.ArmGravityP),
        #SmartDashboard.getNumber("ARM GRAVITY FF:", RobotMap.ArmGravityP))
        self.leftTrigger = OI()
        



