#!/usr/bin/python3
import logging
from motor import Motor
from led import Led
from buzzer import Buzzer
import time
from servo import Servo

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class Robot:

    def __init__(self):
        '''Constructor for class'''
        self.motor = Motor()

    def check_motors(self):
        '''Check speed of both checks'''
        logging.info('Starting motor run')
        try:
            self.motor.forwards(20, 3)
            self.motor.left(20, 3)
            self.motor.right(20, 3)
            self.motor.backwards(20, 3)
            self.motor.stop()
        except KeyboardInterrupt as error:
            logging.error('Error occurred: {}'.format(error))
       
if __name__ == "__main__":
    robot = Robot()
    robot.check_motors()
    led = Led()
    led.rainbow_cycle()
    led.wipe()
    buzzer = Buzzer()
    buzzer.run(True)
    time.sleep(3)
    buzzer.run(False)
    servo = Servo()
    for i in range(0, 180):
        servo.set_servo_pwm('0', i)
        servo.set_servo_pwm('1', i)
    servo.set_servo_pwm('0', 90)
