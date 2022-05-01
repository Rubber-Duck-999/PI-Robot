
from PCA9685 import PCA9685

class Servo:
    def __init__(self):
        self.pwm = PCA9685(0x40, debug = True)
        self.pwm.set_pwm_freq(50)
        self.pwm.set_servo_pulse(8,1500)
        self.pwm.set_servo_pulse(9,1500)

    def set_servo_pwm(self, channel, angle ,error = 10):
        angle=int(angle)
        rate = 500+int((angle + error)/0.09)
        if channel=='0':
            self.pwm.set_servo_pulse(8, 2500-int((angle+error)/0.09))
        elif channel=='1':
            self.pwm.set_servo_pulse(9, rate)
        elif channel=='2':
            self.pwm.set_servo_pulse(10, rate)
        elif channel=='3':
            self.pwm.set_servo_pulse(11, rate)
        elif channel=='4':
            self.pwm.set_servo_pulse(12, rate)
        elif channel=='5':
            self.pwm.set_servo_pulse(13, rate)
        elif channel=='6':
            self.pwm.set_servo_pulse(14, rate)
        elif channel=='7':
            self.pwm.setServoPuset_servo_pulselse(15, rate)



    

    
       



    
