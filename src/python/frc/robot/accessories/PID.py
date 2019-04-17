class PID:

    def __init__(self):

        #PID constants
        self.P_GAIN  = 0
        self.I_GAIN  = 0
        self.D_GAIN  = 0
        self.F_GAIN  = 0

        self.kP = 0
        self.kI = 0
        self.kD = 0
        self.kF = 0

        #Variables for in between loops
        self.lastProportional = 0 
        self.lastTime = 0
        self.currentTime = 0
        self.timeDifference = 0

        self.target = 0
        self.output = 0
    
    def inputPID(self,p_gain,i_gain,d_gain,f_gain):

        #Instantiating attributes by parameters
        self.P_GAIN = p_gain
        self.I_GAIN = i_gain
        self.D_GAIN = d_gain
        self.F_GAIN = f_gain
        self.target = 0

    def setTargetPID(self,newTarget):
        self.target = newTarget

    def updatePID(self,input):
        lastTime = currentTime
        currentTime = #System.currentTimeMillis()
        timeDifference = currentTime - lastTime
        lastProportional = kP
        kP = P_GAIN * (target - input)
        kI += kP
        kD = ((kP - lastProportional) / (timeDifference)) * D_GAIN
        output = kP + kI * I_GAIN - kD + F_GAIN * (input)
        