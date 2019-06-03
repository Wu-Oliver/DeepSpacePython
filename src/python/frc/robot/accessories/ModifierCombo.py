from wpilib.buttons.joystickbutton import JoystickButton
from wpilib.buttons.button import Button
from wpilib.joystick import Joystick


class ModifierCombo() :
    
    def __init__(self,modifierButton,activator):
        self.m_modifierButton = modifierButton
        self.m_activator = activator

    def get(self):
        return self.m_modifierButton.get(), self.m_activator.get()
