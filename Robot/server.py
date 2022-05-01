import socket
import time

class Server:
    def __init__(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.in_use = True
        try:
            self.socket.bind((address, port))
            self.socket.listen(5)
        except OSError as error:
            print('Socket in use: {}'.format(error))

    def start(self):
        print('Starting receive')
        conn = None
        try:
            conn, address = self.socket.accept()
            print('Accepting from {}'.format(address))
            message = ''
            while self.in_use:
                data = conn.recv(4096)
                if data:
                    message = data
                    print(message)
                    if message == 'Stop':
                        self.in_use = False
                else:
                    time.sleep(0.5)
            conn.close()
            print('Client disconnected')
        except OSError as error:
            print('Error on operating system: {}'.format(error))
        except KeyboardInterrupt as error:
            if conn:
                conn.close()
            print('Client disconnected')
            

if __name__ == "__main__":
    server = Server('0.0.0.0', 10000)
    server.start()