
import socket
import os

UDP_IP = os.environ['AGENT_IP']
UDP_PORT = int(os.environ['AGENT_PORT'])
class TraktorServer:
    def run(name):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        while True:
            data, addr = sock.recvfrom(1024)
            print("recieved message: ", data)
            print("from: ", addr)

def main():
    print("Server starting on: ", UDP_IP, ":",UDP_PORT)

    traktorServer = TraktorServer()
    traktorServer.run()

if __name__ == "__main__":
    main()