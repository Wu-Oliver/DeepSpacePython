import math

armSpeedMultiplier = 1
driveSpeedMultiplier = 1
wristSpeedMultiplier = 1

numberOfTicks = 2048
wheelCircumference = 6*math.pi

  #PWM - Pulse Width Modulation Ports
leftDriveMotor1 = 7
leftDriveMotor2 = 8
  # leftDriveMotor3 = 9

rightDriveMotor1 = 0
rightDriveMotor2 = 1
  # rightDriveMotor3 = 2

  #WristMotor - Talon SRX
wristMotor = 9

  #IntakeMotor
intakeLeft = 4
intakeRight = 5

  #D I/O - Digital Input/Output Ports
leftDriveEncoder1 = 0 #white - channel A
leftDriveEncoder2 = 1 #brown - channel B
rightDriveEncoder1 = 2 #white - channel A
rightDriveEncoder2 = 3 #brown - channel B

  #Limit Switch Ports
ArmLimitSwitch = 9
WristLimitSwitch = 8

  #Deadzones
joystickDeadzone = 0.05
triggerDeadzone = 0.05

  #Arm Motors
armBaseMotor1 = 3
armBaseMotor2 = 4
armBaseMotor3 = 8

  #Arm Encoders
armEncoder1 = 0
armEncoder2 = 0
armEncoder3 = 0

  #Pneumatics Control Module (PCM)
leftIntakeSolenoid = 0
rightIntakeSolenoid = 1

  #INTAKE SPEED CONSTANTS
shootBallFast = 0.8
shootBallSlow = -0.5

  #Arm Angle Level Constants
groundLevelAngle = 0
cargoShipAngle = 0
rocketLevel1Angle = 0
rocketLevel2Angle = 0
rocketLevel3Angle = 0

  #Wrist Angle Level Constants
raisedWrist = 0
loweredWrist = 0

  #Arm Power Constants
armPowerFast = 0.8
armPowerSlow = -0.3

  #Drive Straight PIDF
DriveStraightP = 0.00
DriveStraightI = 0
DriveStraightD = 0.00
DriveStraightFF = 0

  #Drive Distance PIDF
DistanceP = 0.035
DistanceI = 0
DistanceD = 0
DistanceFF = 0

  #Arm Raise PIDF
ArmRaiseP = 0.001
ArmRaiseI = 0
ArmRaiseD = 0
ArmRaiseFF = 0

  #Arm Lower PIDF
ArmLowerP = 0
ArmLowerI = 0
ArmLowerD = 0
ArmLowerFF = 0

  #Arm Gravity Resist PIDF
ArmGravityP = 0
ArmGravityI = 0
ArmGravityD = 0
ArmGravityFF = 0

  #Wrist Gravity Resist PIDF
WristGravityP = 0
WristGravityI = 0
WristGravityD = 0
WristGravityFF = 0

  #Wrist Rotate PIDF
WristRotateP = 0
WristRotateI = 0
WristRotateD = 0
WristRotateFF = 0

  #Turn PIDF
TurnP = 0.5
TurnI = 0.2
TurnD = 0.03
TurnFF = 0.2

  #CAN Device IDs
PDPID = 1
PCMID = 0

  #PCM Device IDs
intakeSolenoidChannel = 7

  #Speed Constants Ball
intakeSpeed = 0.2
tossBallSpeed = -0.2
blastBallSpeed = -0.7

  #Drive Train Presets
lowDriveSpeed = 0.8
moderateDriveSpeed = 1.2
highDriveSpeed = 1.4

  #Set speed multipliers
def setArmMultiplier(multiplier):
  armSpeedMultiplier = multiplier
    

def setWristMultiplier(multiplier):
  wristSpeedMultiplier = multiplier
    
def setDriveMultiplier(multiplier):
  driveSpeedMultiplier = multiplier