import time
class PID:

    def __init__(self, p_gain, i_gain, d_gain, f_gain):

        #PID constants
        self.P_GAIN = p_gain
        self.I_GAIN = i_gain
        self.D_GAIN = d_gain
        self.F_GAIN = f_gain

        self.kP = 0
        self.kI = 0
        self.kD = 0
        self.kF = 0

        #Variables for in between PID loops
        self.lastProportional = 0 
        self.lastTime = 0
        self.currentTime = 0
        self.timeDifference = 0
        self.target = 0
        self.output = 0

    def setTargetPID(self,newTarget):
        self.target = newTarget

    def updatePID(self,input):
        self.lastTime = lambda: int(round(time.time() * 1000))
        self.currentTime = lambda: int(round(time.time() * 1000))
        self.timeDifference = currentTime - lastTime
        self.lastProportional = kP
        self.kP = P_GAIN * (target - input)
        self.kI += kP
        self.kD = ((kP - lastProportional) / (timeDifference)) * D_GAIN
        self.output = kP + kI * I_GAIN - kD + F_GAIN * (input)

    def getOutput(self):
        return self.output

    def getPIDConstants(self):
        return ("PID: " + "P: "+ P_GAIN + " I: " + I_GAIN + " D: " + D_GAIN)