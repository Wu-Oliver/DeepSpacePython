from wpilib.command import Command
from wpilib.smartdashboard import SmartDashboard
from accessories.PID import PID
from RobotMap import *
import subsystems

class ArcadeDriveCommand(Command):

    def __init__(self):

        self.requires(subsystems.drivetrain)

        self.leftJoyY = 0
        self.rightJoyX = 0

        self.error = 0
        self.gain = 0

        self.straightPID = PID(DriveStraightP, DriveStraightI, DriveStraightD, DriveStraightFF)
        subsystems.drivetrain.resetEncoders()
    
    def execute(self):

        self.error = subsystems.drivetrain.getLeftDistance() - subsystems.drivetrain.getRightDistance()


        self.leftJoyY = subsystems.oi.xBoxController.getLeftStickY()
        self.rightJoyX = subsystems.oi.xBoxController.getRightStickX()

        if self.leftJoyY > -joystickDeadzone and self.leftJoyY < joystickDeadzone:
            self.leftJoyY = 0

        if self.rightJoyX > -joystickDeadzone and self.rightJoyX < joystickDeadzone:
            self.rightJoyX = 0
        
        if self.rightJoyX != 0:
            subsystems.drivetrain.setLeftDrivePower(subsystems.drivetrain.accelerateDrive() - self.rightJoyX)
            subsystems.drivetrain.setRightDrivePower(subsystems.drivetrain.accelerateDrive() + self.rightJoyX)    

        elif rightJoyX == 0  and leftJoyY != 0:
            self.straightPID.updatePID(self.error)  
            self.gain = self.straightPID.getOutput()
            subsystems.drivetrain.setLeftDrivePower(subsystems.drivetrain.accelerateDrive() - self.gain)
            subsystems.drivetrain.setRightDrivePower(subsystems.drivetrain.accelerateDrive() + self.gain)  

        else:
            subsystems.drivetrain.setLeftDrivePower(0.0)
            subsystems.drivetrain.setRightDrivePower(0.0)
    
    def isFinished():
        return False

    def end():
        pass
    
    def interrupted():
        pass