import threading
import socket

socketStopEvent = threading.Event()

# Create a socket instance
socketInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketInstance.bind(('127.0.0.1', 5555))
socketInstance.listen()

def socketListen():
    print("Server listening ...\n")
    while not socketStopEvent.is_set():
        try:
            client, address = socketInstance.accept()
            print(f'Connected with the client: {address}')
            client.send("You are Connected Successfully".encode())
            client.close()
        except OSError as e:
            if socketStopEvent.is_set():
                break
            else:
                raise e

# Create and start the socket listening thread
socketThread = threading.Thread(target=socketListen)
socketThread.start()

# Wait for user input to terminate the server
x = input("Enter 't' to terminate the server. ")
while x.lower() != 't':
    x = input("Enter 't' to terminate the server. ")

# Set the stop event to terminate the socket listening thread
socketStopEvent.set()

# Close the socket instance
socketInstance.close()

# Wait for the socket listening thread to finish
socketThread.join()

print("Server Stopped ...\n")
