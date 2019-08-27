
import wpilib
import wpilib.drive
from commandbased import CommandBasedRobot
from subsystems.DriveTrainSubsystem import driveTrain
import accessories
from wpilib.command import Scheduler
from accessories.OI import OI
# from wpilib.robotbase import RobotBas

class SpartanRobot(CommandBasedRobot):

    def robotInit(self):
        self.driveTrain = driveTrain
        self.oi = OI()

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

    def getRobotObject(self):
        return self


if __name__ == "__main__":
    wpilib.run(SpartanRobot)