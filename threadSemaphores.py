import threading
import time

semaphore = threading.BoundedSemaphore(value=5)


def accessResource(thread_number):
    print(f"\nThread-{thread_number} trying to access the resource.")
    semaphore.acquire()
    print(f"Thread-{thread_number} gets access to resource.")
    time.sleep(5)
    print(f"\nfThread-{thread_number} releasing resource.")
    semaphore.release()

for thread_number in range(10):
    t1 = threading.Thread(target=accessResource, args=(thread_number,))
    t1.start()
    time.sleep(0.5)
