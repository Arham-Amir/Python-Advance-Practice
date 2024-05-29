import threading

def print10A():
    for i in range(0, 10):
        print("A\t")

def print10B():
    for i in range(0, 10):
        print("B\t")


t1 = threading.Thread(target=print10A)
t2 = threading.Thread(target=print10B)

lock = threading.Lock()
# and use lock by using with keyword

t1.start()
t2.start()

t1.join()
t2.join()
print("completed")