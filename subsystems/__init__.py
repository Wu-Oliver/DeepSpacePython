# from subsystems.ArmSubsystem import ArmSubsystem
from subsystems.DriveTrainSubsystem import DriveTrainSubsystem
# from subsystems.IntakeSubsystem import IntakeSubsystem
# from subsystems.PneumaticsSubsystem import PneumaticsSubsystem
# from subsystems.WristSubsystem import WristSubsystem

drivetrain = None
# arm = None
# intake = None
# pneumatics = None
# wrist = None

def init():

    global drivetrain#, arm, intake, pneumatics, wrist

    drivetrain = DriveTrainSubsystem()
    # arm = ArmSubsystem()
    # intake = IntakeSubsystem()
    # pneumatics = PneumaticsSubsystem()
    # wrist = WristSubsystem()