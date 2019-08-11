from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from accessories.ControllerLogitech import Logitech
from accessories.ControllerXbox import Xbox
from wpilib.interfaces import GenericHID
from accessories.POVButton import POVButton
from accessories.ModifierCombo import ModifierCombo
from autocommands.ModifierButtonCombination import ModifierButtonCombination
class OI():
    
    def __init__(self):
        
        #Defining the main controllers
        # self.logitechController = Logitech(0)
        self.xBoxController = Xbox(0)

        #Xbox Controller Button
        self.xboxUp = POVButton(xBoxController, 0)
        self.xboxDown = POVButton(xBoxController, 180)


        # self.xboxUp = POVButton(self.logitechController, 0)
        # self.xboxDown = POVButton(self.logitechController, 180)

        #Defining modifier 1 button combinations for the xbox controller 
        self.mod1AndX = ModifierCombo(self.xBoxController.rightBumper, self.xBoxController.xButton) 
        self.mod1AndY = ModifierCombo(self.xBoxController.rightBumper, self.xBoxController.yButton)
        self.mod1AndA = ModifierCombo(self.xBoxController.rightBumper, self.xBoxController.aButton)
        self.mod1AndB = ModifierCombo(self.xBoxController.rightBumper, self.xBoxController.bButton)
        self.mod1AndDPadUp = ModifierCombo(self.xBoxController.rightBumper, self.xboxUp)
        self.mod1AndDPadDown = ModifierCombo(self.xBoxController.rightBumper, self.xboxDown)

        #Defining modifier 2 button combinations for the xbox controller
        self.mod2AndA = ModifierCombo(self.xBoxController.leftBumper, self.xboxA) 
        self.mod2AndX = ModifierCombo(self.xBoxController.leftBumper, self.xboxX)
        self.mod2AndB = ModifierCombo(self.xBoxController.leftBumper, self.xboxB)
        self.mod2AndY = ModifierCombo(self.xBoxController.leftBumper, self.xboxY)
        self.mod2AndDPadUp = ModifierCombo(self.xBoxController.leftBumper, self.xboxUp)
        self.mod2AndDPadDown = ModifierCombo(self.xBoxController.leftBumper, self.xboxDown)
        
        '''self.xboxStart.whenPressed(PneumaticsActivate());
        self.logitechStart.whenPressed(AutonomousOveride());

        #Defining button combinations for modifier 1
        self.mod1AndDPadDown.whenPressed(ModifierButtonCombination(66, 0))
        self.mod1AndDPadUp.whenPressed(ModifierButtonCombination(175, 0))
        self.mod1AndA.whenPressed(ModifierButtonCombination(0, 20))
        self.mod1AndX.whenPressed(ModifierButtonCombination(0, 20))
        self.mod1AndB.whenPressed(ModifierButtonCombination(0, 20))
        self.mod1AndY.whenPressed(ModifierButtonCombination(0, 20))
        self.xboxBack.whenPressed(PneumaticsActivate())

        #Defining button combinations for modifier 2.
        self.mod2AndDPadDown.whenPressed(ModifierButtonCombination(0, 20))
        self.mod2AndDPadUp.whenPressed(ModifierButtonCombination(0, 20))
        self.mod2AndA.whenPressed(ModifierButtonCombination(0, 20))
        self.mod2AndX.whenPressed(ModifierButtonCombination(0, 20))
        self.mod2AndB.whenPressed(ModifierButtonCombination(0, 20))
        self.mod2AndY.whenPressed(ModifierButtonCombination(0, 20))'''

    # def getSecondaryControllerLeftStickY(self):
    #     return self.xBoxController.getRawAxis(1)

    # def getSecondaryControllerRightStickY(self): 
    #     return self.xBoxController.getRawAxis(5)

    # def getSecondaryControllerRightStickX(self):
    #     return self.xBoxController.getRawAxis(4)
        
    # def getSecondaryControllerLeftTrigger(self):
    #     return self.xBoxController.getRawAxis(2)

    # def getSecondaryControllerRightTrigger(self):
    #     return self.xBoxController.getRawAxis(3)

    # def AutonomousOveride(self):
    #     return True
