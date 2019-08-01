
import wpilib
import wpilib.drive
from commandbased import CommandBasedRobot
#from wpilib.command import Scheduler
#from src.python.frc.robot.subsystems.ArmSubsystem import ArmSubsystem as arm
from subsystems.DriveTrainSubsystem import DriveTrainSubsystem as drive
#from src.python.frc.robot.subsystems.IntakeSubsystem import IntakeSubsystem as intake
#from src.python.frc.robot.subsystems.PneumaticsSubsystem import PneumaticsSubsystem as pneumatics
#from src.python.frc.robot.subsystems.WristSubsystem import WristSubsystem as wrist
from OI import OI

from wpilib.command import Scheduler
from wpilib.robotbase import RobotBase
from wpilib import TimedRobot

class SpartanRobot(CommandBasedRobot):

    def __init__(self):
        super().__init__()
        self.drivetrain = drive()  
        self.oi = OI()
    
    def robotInit(self):
        pass

    
    def robotPeriodic(self):
        self.drivetrain.updateMotorOutputs()
    
    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass

    def disabledInit(self):
        pass
    
    def disabledPeriodic(self):
        pass
        
    def teleopInit(self):
        print("Teleoperated Mode Initiated!")

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(SpartanRobot)