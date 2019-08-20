
import wpilib
import wpilib.drive
from commandbased import CommandBasedRobot
from subsystems.DriveTrainSubsystem import DriveTrainSubsystem
from OI import OI
from wpilib.command import Scheduler
# from wpilib.robotbase import RobotBas

class SpartanRobot(CommandBasedRobot):
    
    def robotInit(self):
        self.oi = OI()
        self.driveTrain = DriveTrainSubsystem()

    def robotPeriodic(self):
        self.driveTrain.updateMotorOutputs()
    
    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass

    def disabledInit(self):
        pass
    
    def disabledPeriodic(self):
        Scheduler.getInstance().run()
        
    def teleopInit(self):
        print("Teleoperated Mode Initiated!")
        Scheduler.getInstance().run()

    def teleopPeriodic(self):
        Scheduler.getInstance().run()


if __name__ == "__main__":
    wpilib.run(SpartanRobot)