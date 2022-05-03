import socket
import time
import random
import string

class Client():
    def __init__(self, connect_mode):
        self.socket = None
        self.connect_mode = connect_mode
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket successfully created")
        except socket.error as error:
            print("socket creation failed with error {}".format(error))
    
    def connect(self, address):
        while self.connect_mode:
            # connecting to the server
            try:
                self.socket.connect((address, 10000))
                print("Connected successfully")
                self.connect_mode = False
            except socket.error as error:
                print("Socket connect error {}".format(error))
                time.sleep(10)

    def get_word(self):
        letters = string.ascii_lowercase
        word = ''.join(random.choice(letters) for i in range(10))
        return word

    def send(self):
        # connecting to the server
        try:
            message = self.get_word()
            self.socket.sendall(message.encode('utf-8'))
            print("Sent data to server")
        except socket.error as error:
            print("Socket connect error {}".format(error))
            self.connect()
        time.sleep(2)

if __name__ == "__main__":
    client = Client(True)
    client.connect('127.0.0.1')
    while True:
        client.send()