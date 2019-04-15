from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from wpilib.interfaces import GenericHID

class XboxController(Joystick):
    
    def __init__(self):
        self.xButton = JoystickButton(3)
        self.yButton = JoystickButton(4)
		self.aButton = JoystickButton(1)
		self.bButton = JoystickButton(2)
		self.rightBumper = JoystickButton(6)
		self.leftBumper = JoystickButton(5)
		self.startButton = JoystickButton(8)
		self.selectButton = JoystickButton(7)
		self.leftStickButton = JoystickButton(9)
		self.rightStickButton = JoystickButton(10)
    
    def getLeftStickX(self):
        return self.getX(GenericHID.Hand.kLeft)
	

	def getLeftStickY(self):
		return self.getY(GenericHID.Hand.kLeft)

	def getRightStickX(self):
        return self.getX(GenericHID.Hand.kRight)
	

	def getRightStickY(self):
		return self.getY(GenericHID.Hand.kRight)
	

	def getLeftAnalogTrigger(self): 
		return self.getRawAxis(2)
	

	def getRightAnalogTrigger(self): 
		return self.getRawAxis(3)
	

	def getDPadValue(self):
		try: 
		    return self.getPOV()
		except:
			return -1

    def getRightBumperStatus(self):
        self.getRawButtonPressed(GenericHID.Hand.kRight)

    def getLeftBumperStatus(self):
        self.getRawButtonPressed(GenericHID.Hand.kLeft)