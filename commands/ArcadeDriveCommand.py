from wpilib.command import Command
from wpilib.smartdashboard import SmartDashboard
from accessories.PID import PID
from RobotMap import *
from robot import SpartanRobot

class ArcadeDriveCommand(Command):

    def __init__(self):

        self.requires(SpartanRobot.drivetrain)

        self.leftJoyY = 0
        self.rightJoyX = 0

        self.error = 0
        self.gain = 0

        self.straightPID = PID(DriveStraightP, DriveStraightI, DriveStraightD, DriveStraightFF)
        SpartanRobot.drivetrain.resetEncoders()
    
    def execute(self):

        self.error = SpartanRobot.drivetrain.getLeftDistance() - SpartanRobot.drivetrain.getRightDistance()


        self.leftJoyY = SpartanRobot.oi.getSecondaryControllerLeftStickY()
        self.rightJoyX = SpartanRobot.oi.getSecondaryControllerRightStickX()

        if self.leftJoyY > -joystickDeadzone and self.leftJoyY < joystickDeadzone:
            self.leftJoyY = 0

        if self.rightJoyX > -joystickDeadzone and self.rightJoyX < joystickDeadzone:
            self.rightJoyX = 0
        
        if self.rightJoyX != 0:
            SpartanRobot.drivetrain.setLeftDrivePower(SpartanRobot.drivetrain.accelerateDrive() - self.rightJoyX)
            SpartanRobot.drivetrain.setRightDrivePower(SpartanRobot.drivetrain.accelerateDrive() + self.rightJoyX)    

        elif rightJoyX == 0  and leftJoyY != 0:
            self.straightPID.updatePID(self.error)  
            self.gain = self.straightPID.getOutput()
            SpartanRobot.drivetrain.setLeftDrivePower(SpartanRobot.drivetrain.accelerateDrive() - self.gain)
            SpartanRobot.drivetrain.setRightDrivePower(SpartanRobot.drivetrain.accelerateDrive() + self.gain)  

        else:
            SpartanRobot.drivetrain.setLeftDrivePower(0.0)
            SpartanRobot.drivetrain.setRightDrivePower(0.0)
    
    def isFinished():
        return False

    def end():
        pass
    
    def interrupted():
        pass