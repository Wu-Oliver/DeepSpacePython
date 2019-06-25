from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from wpilib.interfaces import GenericHID

class Logitech(Joystick):

    def __init__(self):
        self.xButton = JoystickButton(self,3)
        self.yButton = JoystickButton(self,4)
        self.aButton = JoystickButton(self,1)
        self.bButton = JoystickButton(self,2)
        self.rightBumper = JoystickButton(self,6)
        self.leftBumper = JoystickButton(self,5)
        self.startButton = JoystickButton(self,8)
        self.selectButton = JoystickButton(self,7)
        self.leftStickButton = JoystickButton(self,9)
        self.rightStickButton = JoystickButton(self,10)

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
            return(-1)

                    
                        