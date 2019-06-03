
import wpilib
import wpilib.drive
from src.python.frc.robot.subsystems.ArmSubsystem import ArmSubsystem
from src.python.frc.robot.subsystems.DriveTrainSubsystem import DriveTrainSubsystem
from src.python.frc.robot.subsystems.IntakeSubsystem import IntakeSubsystem
from src.python.frc.robot.subsystems.PneumaticsSubsystem import PneumaticsSubsystem
from src.python.frc.robot.subsystems.WristSubsystem import WristSubsystem
from src.python.frc.robot.OI import OI

from wpilib.robotbase import RobotBase
from wpilib import TimedRobot

 
class SpartanRobot(TimedRobot):
    
    def robotInit(self):
        self.drivetrain = DriveTrainSubsystem()  
        self.pneumatics = PneumaticsSubsystem()
        self.arm = ArmSubsystem()
        self.wrist = WristSubsystem()
        self.intake = IntakeSubsystem()
        self.oi = OI()

    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass
        
    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(SpartanRobot)