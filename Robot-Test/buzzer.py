import time
import RPi.GPIO as GPIO

class Buzzer:
    def __init__(self):
        GPIO.setwarnings(False)
        self.buzzer = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzer,GPIO.OUT)

    def run(self, buzz):
        if buzz:
            GPIO.output(self.buzzer, True)
        else:
            GPIO.output(self.buzzer, False)

if __name__=='__main__':
    B = Buzzer()
    B.run(True)
    time.sleep(3)
    B.run(False)




