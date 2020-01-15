
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 13336

class TraktorServer:
    def __init__(udp_ip,udp_port):
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


    def run():
        while true:
            data, addr = sock.recvfrom(1024)
            print("recieved message: ", data)
            print("from: ", addr)

def main():
    traktorServer = TraktorServer(UDP_IP,UDP_PORT)
    traktorServer.run()

if __name__ == "__main__":
    main()