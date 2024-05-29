import socket

socketInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketInstance.connect(("127.0.0.1", 5555))

messageFromServer = socketInstance.recv(1024)
socketInstance.close()

print(messageFromServer.decode())