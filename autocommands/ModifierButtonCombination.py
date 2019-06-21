from wpilib.command import CommandGroup
from autocommands.ArmRotateDegrees import ArmRotateDegrees
from autocommands.WristRotateDegrees import WristRotateDegrees

class ModifierButtonCombination(CommandGroup):

    def ModifierButtonCombination(self,armAngle, wristAngle):
        self.addParallel(ArmRotateDegrees(armAngle))
        self.addParallel(WristRotateDegrees(wristAngle))