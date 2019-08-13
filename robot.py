
import wpilib
import wpilib.drive
from commandbased import CommandBasedRobot
from OI import OI
import subsystems
from wpilib.command import Scheduler
# from wpilib.robotbase import RobotBase
# from wpilib import TimedRobot

class SpartanRobot(CommandBasedRobot):
    
    def robotInit(self):
        subsystems.init()
        oi = OI()

    def robotPeriodic(self):
        subsystems.drivetrain.updateMotorOutputs()
    
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