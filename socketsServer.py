import threading
import socket

socketStopEvent = threading.Event()

socketInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketInstance.bind(('127.0.0.1', 5555))
socketInstance.listen()

def socketListen():
    print("Server listening ...\n")
    while not socketStopEvent.is_set():
        client, address = socketInstance.accept()
        print(f'Connected with the client: {address}')
        client.send("You are Connected Sucessfully".encode())
        client.close() 

socketThread = threading.Thread(target=socketListen)
socketThread.start()


x = input("Enter t to terminate the server. ")
while(x!='t' and x!='T'):
    x = input("Enter t to terminate the server. ")

socketStopEvent.set()
socketThread.join()
print("Server Stopped ...\n")
socketInstance.close()
