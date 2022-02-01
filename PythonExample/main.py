#!/usr/bin/python3

import speedtest
import logging

logging.basicConfig(level=logging.INFO)

class NetworkTest:

    def __init__(self):
        '''Constructor for class'''
        self.speed = speedtest.Speedtest()

    def check_speed(self):
        '''Check speed of both checks'''
        logging.info('Starting check')
        try:
            down_speed = self.speed.download() / 1048576
            up_speed = self.speed.upload() / 1048576
            down = round(down_speed)
            up = round(up_speed)
            logging.info('Download: {}'.format(down))
            logging.info('Upload: {}'.format(up))
        except speedtest.SpeedtestException as error:
            logging.error('Error occurred: {}'.format(error))
       
if __name__ == "__main__":
    network_test = NetworkTest()
    network_test.check_speed()
