
class RobotMap(self):

  self.armSpeedMultiplier = 1
  self.driveSpeedMultiplier = 1
  self.wristSpeedMultiplier = 1

  #PWM - Pulse Width Modulation Ports
  self.leftDriveMotor1 = 7
  self.leftDriveMotor2 = 8
  self.leftDriveMotor3 = 9

  self.rightDriveMotor1 = 0
  self.rightDriveMotor2 = 1
  self.rightDriveMotor3 = 2

  #WristMotor - Talon SRX
  self.wristMotor = 9

  #IntakeMotor
  self.intakeLeft = 4
  self.intakeRight = 5

  #D I/O - Digital Input/Output Ports
  self.leftDriveEncoder1 = 0 #white - channel A
  self.leftDriveEncoder2 = 1 #brown - channel B
  self.rightDriveEncoder1 = 2 #white - channel A
  self.rightDriveEncoder2 = 3 #brown - channel B

  #Limit Switch Ports
  self.ArmLimitSwitch = 9
  self.WristLimitSwitch = 8

  #Deadzones
  self.joystickDeadzone = 0.05
  self.triggerDeadzone = 0.05

  #Arm Motors
  self.armBaseMotor1 = 3
  self.armBaseMotor2 = 4
  self.armBaseMotor3 = 8

  #Arm Encoders
  self.armEncoder1 = 0
  self.armEncoder2 = 0
  self.armEncoder3 = 0

  #Pneumatics Control Module (PCM)
  self.leftIntakeSolenoid = 0
  self.rightIntakeSolenoid = 1

  #INTAKE SPEED CONSTANTS
  self.shootBallFast = 0.8;
  self.shootBallSlow = -0.5;

  #Arm Angle Level Constants
  self.groundLevelAngle = 0
  self.cargoShipAngle = 0
  self.rocketLevel1Angle = 0
  self.rocketLevel2Angle = 0
  self.rocketLevel3Angle = 0

  #Wrist Angle Level Constants
  self.raisedWrist = 0
  self.loweredWrist = 0

  #Arm Power Constants
  self.armPowerFast = 0.8
  self.armPowerSlow = -0.3

  #Drive Straight PIDF
  self.DriveStraightP = 0.00
  self.DriveStraightI = 0
  self.DriveStraightD = 0.00
  self.DriveStraightFF = 0

  #Drive Distance PIDF
  self.DistanceP = 0.035
  self.DistanceI = 0
  self.DistanceD = 0
  self.DistanceFF = 0

  #Arm Raise PIDF
  self.ArmRaiseP = 0.001
  self.ArmRaiseI = 0
  self.ArmRaiseD = 0
  self.ArmRaiseFF = 0

  #Arm Lower PIDF
  self.ArmLowerP = 0
  self.ArmLowerI = 0
  self.ArmLowerD = 0
  self.ArmLowerFF = 0

  #Arm Gravity Resist PIDF
  self.ArmGravityP = 0
  self.ArmGravityI = 0
  self.ArmGravityD = 0
  self.ArmGravityFF = 0

  #Wrist Gravity Resist PIDF
  self.WristGravityP = 0
  self.WristGravityI = 0
  self.WristGravityD = 0
  self.WristGravityFF = 0

  #Wrist Rotate PIDF
  self.WristRotateP = 0
  self.WristRotateI = 0
  self.WristRotateD = 0
  self.WristRotateFF = 0

  #Turn PIDF
  self.urnP = 0.5
  self.TurnI = 0.2
  self.TurnD = 0.03
  self.TurnFF = 0.2

  #CAN Device IDs
  self.PDPID = 1
  self.PCMID = 0

  #PCM Device IDs
  self.intakeSolenoidChannel = 7

  #Speed Constants Ball
  self.intakeSpeed = 0.2
  self.tossBallSpeed = -0.2
  self.blastBallSpeed = -0.7

  #Drive Train Presets
  self.lowDriveSpeed = 0.8
  self.moderateDriveSpeed = 1.2
  self.highDriveSpeed = 1.4

  def setArmMultiplier(multiplier):
    armSpeedMultiplier = multiplier
  

  def setWristMultiplier(multiplier):
    wristSpeedMultiplier = multiplier
  

  def setDriveMultiplier(multiplier):
    driveSpeedMultiplier = multiplier;
