class Engine:
    def __init__(self, idle_rpm, redline, max_torque):
        self.rpm = idle_rpm
        self.idle_rpm = idle_rpm
        self.redline = redline
        self.max_torque = max_torque

engineI4 = Engine(idle_rpm=1200, redline=7000, max_torque=100)
engineI6 = Engine(idle_rpm=1000, redline=7900, max_torque=150)
engines = list()
engines.append(engineI4)
engines.append(engineI6)
var = """W
 
Throttle
 
Engine
 
Torque
 
Gearbox
 
Wheel torque
 
Acceleration
 
Speed
 
Position"""