class Engine:
    def __init__(self, idle_rpm, redline, torque_curve):
        self.idle_rpm = idle_rpm
        self.redline = redline
        self.torque_curve = torque_curve

    def torque(self, rpm):

        if rpm <= self.torque_curve[0][0]:
            return self.torque_curve[0][1]

        if rpm >= self.torque_curve[-1][0]:
            return self.torque_curve[-1][1]

        for i in range(len(self.torque_curve) - 1):
            rpm1, torque1 = self.torque_curve[i]
            rpm2, torque2 = self.torque_curve[i + 1]

            if rpm1 <= rpm <= rpm2:
                t = (rpm - rpm1) / (rpm2 - rpm1)
                return torque1 + (torque2 - torque1) * t

    def hp(self, rpm):
        torque = self.torque(rpm)
        return torque * rpm / 7127



engI4 = Engine(
    idle_rpm=900,
    redline=7200,
    torque_curve=[
        (900, 120),
        (1500, 180),
        (2500, 260),
        (3500, 330),
        (4500, 380),
        (5500, 400),
        (6500, 380),
        (7200, 330),
    ]
)

rpm = 5200

print("RPM:", rpm)
print("Torque:", engI4.torque(rpm), "Nm")
print("Power:", round(engI4.hp(rpm), 1), "HP")
Engines = [engI4]