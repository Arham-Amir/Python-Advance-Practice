import threading
import time
import math

lock = threading.Lock()
num = 1025

def increaseNumberToMax():
    global num, lock
    lock.acquire()
    while num < 24459:
        num*=2
        print(num)
        time.sleep(0.5)
    print("Number reached to the maximum")
    lock.release()

def decreaseNumberToMin():
    global num, lock
    lock.acquire()
    while num > 1:
        num = math.floor(num/2)
        print(num)
        time.sleep(0.5)
    print("Number reached to the minimum")
    lock.release()

t1 = threading.Thread(target=increaseNumberToMax)
t2 = threading.Thread(target=decreaseNumberToMin)

t1.start()
t2.start()

t1.join()
t2.join()