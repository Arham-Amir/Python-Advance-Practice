from contextlib import contextmanager
import socket


@contextmanager
def socketManager(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    yield s
    s.close()
    
with socketManager('127.0.0.0', 9999) as server:
    client, addr = server.accept()
    
print("End")