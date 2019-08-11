
import wpilib
import wpilib.drive
from commandbased import CommandBasedRobot
# from wpilib.command import Scheduler
from subsystems.ArmSubsystem import ArmSubsystem
from subsystems.DriveTrainSubsystem import DriveTrainSubsystem
from subsystems.IntakeSubsystem import IntakeSubsystem
from subsystems.PneumaticsSubsystem import PneumaticsSubsystem
from subsystems.WristSubsystem import WristSubsystem
from OI import OI

from wpilib.command import Scheduler
# from wpilib.robotbase import RobotBase
# from wpilib import TimedRobot

class SpartanRobot(CommandBasedRobot):

    def __init__(self):
        super().__init__()
        self.drivetrain = DriveTrainSubsystem()
        self.intake = IntakeSubsystem()
        self.pneumatics = PneumaticsSubsystem()
        self.wrist = WristSubsystem()
        self.arm = ArmSubsystem()
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