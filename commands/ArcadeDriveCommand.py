from wpilib.command import Command
from wpilib.smartdashboard import SmartDashboard
from accessories.PID import PID
from robot import SpartanRobot
import RobotMap

class ArcadeDriveCommand(Command):

    def __init__(self):
        self.robot = SpartanRobot.getRobotObject(self)
        self.requires(self.robot.driveTrain)

        self.leftJoyY = 0
        self.rightJoyX = 0

        self.error = 0
        self.gain = 0

        self.straightPID = PID(RobotMap.DriveStraightP, RobotMap.DriveStraightI, RobotMap.DriveStraightD, RobotMap.DriveStraightFF)
        self.robot.driveTrain.resetEncoders()
    
    def execute(self):

        self.error = self.robot.driveTrain.getLeftDistance() - self.robot.driveTrain.getRightDistance()


        self.leftJoyY = self.robot.oi.xBoxController.getRawAxis(1)
        self.rightJoyX = self.robot.oi.xBoxController.getRawAxis(4)

        if self.leftJoyY > -RobotMap.joystickDeadzone and self.leftJoyY < RobotMap.joystickDeadzone:
            self.leftJoyY = 0

        if self.rightJoyX > -RobotMap.joystickDeadzone and self.rightJoyX < RobotMap.joystickDeadzone:
            self.rightJoyX = 0
        
        if self.rightJoyX != 0:
            self.robot.driveTrain.setLeftDrivePower(self.robot.driveTrain.accelerateDrive() - self.rightJoyX)
            self.robot.driveTrain.setRightDrivePower(self.robot.driveTrain.accelerateDrive() + self.rightJoyX)    

        elif self.rightJoyX == 0  and self.leftJoyY != 0:
            self.straightPID.updatePID(self.error)  
            self.gain = self.straightPID.getOutput()
            self.robot.driveTrain.setLeftDrivePower(self.robot.driveTrain.accelerateDrive() - self.gain)
            self.robot.driveTrain.setRightDrivePower(self.robot.driveTrain.accelerateDrive() + self.gain)  

        else:
            self.robot.driveTrain.setLeftDrivePower(0.0)
            self.robot.driveTrain.setRightDrivePower(0.0)
    
    def isFinished(self):
        return False

    def end(self):
        pass
    
    def interrupted(self):
        pass