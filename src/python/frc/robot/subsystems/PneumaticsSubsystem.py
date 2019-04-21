from wpilib.command import Subsystem
from src.python.frc.robot.RobotMap import RobotMap
from wpilib import Compressor
from wpilib import Solenoid

class PneumaticsSubsystem(Subsystem):

    def __init__(self):
        self.mainCompressor = Compressor(RobotMap.PCMID)
        self.intakeSolenoid = Solenoid(RobotMap.PCMID,RobotMap.intakeSolenoidChannel)
        self.isExtended = False

        self.mainCompressor.start()

    def initDefaultCommand(self):
        pass

    def flipSolenoid(self):
        if self.isExtended == False:
            self.isExtended = True
        else:
            self.isExtended == False
        
        self.intakeSolenoid.set(isExtended)

    def getIsExtended(self):
        return self.isExtended


    