from socket import *
import threading
import time



def send(sock):
    while True:
        sendData = input()
        print('')
        sock.send(sendData.encode('utf-8'))


def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 : ', recvData.decode('utf-8'))
        print('')


port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('211.108.167.150', port))

print('접속 완료')
input()

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))


sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass