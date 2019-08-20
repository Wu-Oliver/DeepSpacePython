from wpilib.command import Command
from wpilib.smartdashboard import SmartDashboard
from accessories.PID import PID
from RobotMap import *
from robot import SpartanRobot

class ArcadeDriveCommand(Command):

    def __init__(self):

        self.requires(SpartanRobot.driveTrain)

        self.leftJoyY = 0
        self.rightJoyX = 0

        self.error = 0
        self.gain = 0

        self.straightPID = PID(DriveStraightP, DriveStraightI, DriveStraightD, DriveStraightFF)
        SpartanRobot.driveTrain.resetEncoders()
    
    def execute(self):

        self.error = SpartanRobot.driveTrain.getLeftDistance() - SpartanRobot.driveTrain.getRightDistance()


        self.leftJoyY = SpartanRobot.oi.xBoxController.getRawAxis(1)
        self.rightJoyX = SpartanRobot.oi.xBoxController.getRawAxis(4)

        if self.leftJoyY > -joystickDeadzone and self.leftJoyY < joystickDeadzone:
            self.leftJoyY = 0

        if self.rightJoyX > -joystickDeadzone and self.rightJoyX < joystickDeadzone:
            self.rightJoyX = 0
        
        if self.rightJoyX != 0:
            SpartanRobot.driveTrain.setLeftDrivePower(SpartanRobot.driveTrain.accelerateDrive() - self.rightJoyX)
            SpartanRobot.driveTrain.setRightDrivePower(SpartanRobot.driveTrain.accelerateDrive() + self.rightJoyX)    

        elif rightJoyX == 0  and leftJoyY != 0:
            self.straightPID.updatePID(self.error)  
            self.gain = self.straightPID.getOutput()
            SpartanRobot.driveTrain.setLeftDrivePower(SpartanRobot.driveTrain.accelerateDrive() - self.gain)
            SpartanRobot.driveTrain.setRightDrivePower(SpartanRobot.driveTrain.accelerateDrive() + self.gain)  

        else:
            SpartanRobot.driveTrain.setLeftDrivePower(0.0)
            SpartanRobot.driveTrain.setRightDrivePower(0.0)
    
    def isFinished():
        return False

    def end():
        pass
    
    def interrupted():
        pass