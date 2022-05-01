import time
from PCA9685 import PCA9685


class Motor:
    MAXIMUM_VALUE = 4095
    def __init__(self):
        # Set input variables for motor
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.set_pwm_freq(50)

    def set_duty_range(self, duty):
        # Set ranges of duty
        if duty > self.MAXIMUM_VALUE:
            duty = self.MAXIMUM_VALUE
        elif duty < -self.MAXIMUM_VALUE:
            duty = -self.MAXIMUM_VALUE
        return duty
        
    def left_Upper_Wheel(self, duty):
        if duty > 0:
            self.pwm.setMotorPwm(0, 0)
            self.pwm.setMotorPwm(1, duty)
        elif duty < 0:
            self.pwm.setMotorPwm(1, 0)
            self.pwm.setMotorPwm(0, abs(duty))
        else:
            self.pwm.setMotorPwm(0, self.MAXIMUM_VALUE)
            self.pwm.setMotorPwm(1, self.MAXIMUM_VALUE)

    def left_Lower_Wheel(self, duty):
        if duty > 0:
            self.pwm.setMotorPwm(3, 0)
            self.pwm.setMotorPwm(2, duty)
        elif duty < 0:
            self.pwm.setMotorPwm(2, 0)
            self.pwm.setMotorPwm(3, abs(duty))
        else:
            self.pwm.setMotorPwm(2, self.MAXIMUM_VALUE)
            self.pwm.setMotorPwm(3, self.MAXIMUM_VALUE)

    def right_Upper_Wheel(self, duty):
        if duty > 0:
            self.pwm.setMotorPwm(6, 0)
            self.pwm.setMotorPwm(7, duty)
        elif duty < 0:
            self.pwm.setMotorPwm(7, 0)
            self.pwm.setMotorPwm(6, abs(duty))
        else:
            self.pwm.setMotorPwm(6, self.MAXIMUM_VALUE)
            self.pwm.setMotorPwm(7, self.MAXIMUM_VALUE)

    def right_Lower_Wheel(self, duty):
        if duty > 0:
            self.pwm.setMotorPwm(4, 0)
            self.pwm.setMotorPwm(5, duty)
        elif duty < 0: 
            self.pwm.setMotorPwm(5, 0)
            self.pwm.setMotorPwm(4, abs(duty))
        else:
            self.pwm.setMotorPwm(4, self.MAXIMUM_VALUE)
            self.pwm.setMotorPwm(5, self.MAXIMUM_VALUE)
            
    def set_motor_model(self, duty_1, duty_2, duty_3, duty_4):
        self.left_Upper_Wheel(self.set_duty_range(duty_1))
        self.left_Lower_Wheel(self.set_duty_range(duty_2))
        self.right_Upper_Wheel(self.set_duty_range(duty_3))
        self.right_Lower_Wheel(self.set_duty_range(duty_4))
                 
    def check_multiplier(self, multiplier):
        if multiplier > 40:
            multiplier = 40
        elif multiplier <= 0:
            multiplier = 1
        return multiplier
                
    def forwards(self, multiplier, length):
        multiplier = self.check_multiplier(multiplier)
        duty = 100 * multiplier
        self.set_motor_model(duty, duty, duty, duty)
        time.sleep(length)

    def backwards(self, multiplier, length):
        multiplier = self.check_multiplier(multiplier)
        duty = -100 * multiplier
        self.set_motor_model(duty, duty, duty, duty)
        time.sleep(length)

    def left(self, multiplier, length):
        multiplier = self.check_multiplier(multiplier)
        duty = 100 * multiplier
        turn_duty = -(duty / 4)
        self.set_motor_model(turn_duty, turn_duty, duty, duty)
        time.sleep(length)
    
    def right(self, multiplier, length):
        multiplier = self.check_multiplier(multiplier)
        duty = 100 * multiplier
        turn_duty = -(duty / 4)
        self.set_motor_model(duty, duty, turn_duty, turn_duty)
        time.sleep(length)

    def stop(self):
        self.setMotorModel(0, 0, 0, 0)
    

if __name__=='__main__':
    try:
        vehicle = Motor()
        vehicle.forwards(20, 3)
        vehicle.backwards(20, 3)
        vehicle.stop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print('Shutting down')
