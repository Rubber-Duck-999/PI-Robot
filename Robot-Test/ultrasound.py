import time
import RPi.GPIO as GPIO
from servo import *
from PCA9685 import PCA9685

class Ultrasonic:
    def __init__(self):
        GPIO.setwarnings(False)
        self.trigger_pin = 27
        self.echo_pin = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin,GPIO.OUT)
        GPIO.setup(self.echo_pin,GPIO.IN)

    def send_trigger_pulse(self):
        GPIO.output(self.trigger_pin,True)
        time.sleep(0.00015)
        GPIO.output(self.trigger_pin,False)

    def wait_for_echo(self,value,timeout):
        count = timeout
        while GPIO.input(self.echo_pin) != value and count>0:
            count = count-1
     
    def get_distance(self):
        distance_cm=[0, 0, 0, 0, 0]
        for i in range(3):
            self.send_trigger_pulse()
            self.wait_for_echo(True,10000)
            start = time.time()
            self.wait_for_echo(False,10000)
            finish = time.time()
            pulse_len = finish-start
            distance_cm[i] = pulse_len/0.000058
        distance_cm=sorted(distance_cm)
        return int(distance_cm[2])

    def check_distance(self, angle):
        print('Checking distance')
        if angle == 30:
            left = self.get_distance()
            print('Left: {}'.format(left))
        elif angle == 90:
            middle = self.get_distance()
            print('Middle: {}'.format(middle))
        else:
            right = self.get_distance()
            print('Right: {}'.format(right))

    def run(self):
        self.servo = Servo()
        self.servo.set_servo_pwm('0', 90)
        while True:
            for i in range(30,151,60):
                self.servo.set_servo_pwm('0', i)
                time.sleep(0.2)
                self.check_distance(i)
            for i in range(90,30,-60):
                self.servo.set_servo_pwm('0', i)
                time.sleep(0.2)
                self.check_distance(i)

