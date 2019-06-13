from wpilib.command import CommandGroup
from src.python.frc.robot.autocommands.ArmRotateDegrees import ArmRotateDegrees
from src.python.frc.robot.autocommands.WristRotateDegrees import WristRotateDegrees

class ModifierButtonCombination(CommandGroup):

    def ModifierButtonCombination(self,armAngle, wristAngle):
        self.addParallel(ArmRotateDegrees(armAngle))
        self.addParallel(WristRotateDegrees(wristAngle))