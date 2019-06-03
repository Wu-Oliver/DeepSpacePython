from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from src.python.frc.robot.accessories.ControllerLogitech import Logitech
from src.python.frc.robot.accessories.ControllerXbox import Xbox
from wpilib.interfaces import GenericHID
from src.python.frc.robot.accessories.POVButton import POVButton
from src.python.frc.robot.accessories.ModifierCombo import ModifierCombo



class OI():
    
    def __init__(self):
        
        #Defining the main controllers
        self.logitechController = Logitech()
        self.xBoxController = Xbox()

        #Xbox Controller Buttons
        self.xboxA = JoystickButton(self.xBoxController, 1)
        self.xboxB =  JoystickButton(self.xBoxController, 2)
        self.xboxY =  JoystickButton(self.xBoxController, 4)
        self.xboxX =  JoystickButton(self.xBoxController, 3)
        self.xboxLB =  JoystickButton(self.xBoxController, 5)
        self.xboxRB =  JoystickButton(self.xBoxController, 6)
        self.xboxStart =  JoystickButton(self.xBoxController, 8)
        self.xboxBack =  JoystickButton(self.xBoxController, 7)
        self.xboxLStickButton =  JoystickButton(self.xBoxController, 9)
        self.xboxRStickButton =  JoystickButton(self.xBoxController, 10)
        self.xboxUp = POVButton(self.xBoxController, 0)
        self.xboxDown = POVButton(self.xBoxController, 180)

        #Logitech Controller Buttons
        self.logitechA =  JoystickButton(self.logitechController, 1)
        self.logitechB = JoystickButton(self.logitechController, 2)  
        self.logitechY = JoystickButton(self.logitechController, 4)
        self.logitechX =  JoystickButton(self.logitechController, 3) 
        self.logitechLB = JoystickButton(self.logitechController, 5) 
        self.logitechRB =  JoystickButton(self.logitechController, 6) 
        self.logitechStart =  JoystickButton(self.logitechController, 8)
        self.logitechBack = JoystickButton(self.logitechController, 7) 
        self.logitechLStickButton =  JoystickButton(self.logitechController, 9)
        self.logitechRStickButton =  JoystickButton(self.logitechController, 10)
        self.xboxUp = POVButton(self.logitechController, 0)
        self.xboxDown = POVButton(self.logitechController, 180)

        #Defining modifier 1 button combinations for the xbox controller 
        self.mod1AndX = ModifierCombo(self.xboxRB, self.xboxX) 
        self.mod1AndY = ModifierCombo(self.xboxRB, self.xboxY)
        self.mod1AndA = ModifierCombo(self.xboxRB, self.xboxA)
        self.mod1AndB = ModifierCombo(self.xboxRB, self.xboxB)
        self.mod1AndDPadUp = ModifierCombo(self.selfxboxRB, self.xboxUp)
        self.mod1AndDPadDown = ModifierCombo(self.xboxRB, self.xboxDown)

        #Defining modifier 2 button combinations for the xbox controller
        self.mod2AndA = ModifierCombo(self.xboxLB, self.xboxA) 
        self.mod2AndX = ModifierCombo(self.xboxLB, self.xboxX)
        self.mod2AndB = ModifierCombo(self.xboxLB, self.xboxB)
        self.mod2AndY = ModifierCombo(self.xboxLB, self.xboxY)
        self.mod2AndDPadUp = ModifierCombo(self.xboxLB, self.xboxUp)
        self.mod2AndDPadDown = ModifierCombo(self.xboxLB, self.xboxDown)

    def OI(self):
        #self.xboxStart.whenPressed(PneumaticsActivate());
        #self.logitechStart.whenPressed(AutonomousOveride());

        mod1AndDPadDown.whenPressed(ModifierButtonCombination(66, 0))
        mod1AndDPadUp.whenPressed(new ModifierButtonCombination(175, 0))
        mod1AndA.whenPressed(new ModifierButtonCombination(0, 20));
        mod1AndX.whenPressed(new ModifierButtonCombination(0, 20));
        mod1AndB.whenPressed(new ModifierButtonCombination(0, 20));
        mod1AndY.whenPressed(new ModifierButtonCombination(0, 20));
        // xboxBack.whenPressed(new PneumaticsActivate());

        // Defining button combinations for modifier 2.
        mod2AndDPadDown.whenPressed(new ModifierButtonCombination(0, 20));
        mod2AndDPadUp.whenPressed(new ModifierButtonCombination(0, 20));
        mod2AndA.whenPressed(new ModifierButtonCombination(0, 20));
        mod2AndX.whenPressed(new ModifierButtonCombination(0, 20));
        mod2AndB.whenPressed(new ModifierButtonCombination(0, 20));
        mod2AndY.whenPressed(new ModifierButtonCombination(0, 20));
                






