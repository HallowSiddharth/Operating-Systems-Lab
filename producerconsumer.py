from threading import Semaphore
import time
import threading

max_c = 10
full = Semaphore(0)
empty = Semaphore(max_c)
mutex = Semaphore(1)
queue = []

def producer(i):
    empty.acquire()
    mutex.acquire()
    print("Produced: ", i)
    queue.append(i)
    mutex.release()
    full.release()



def consumer(i):
    full.acquire()
    mutex.acquire()
    print("Consumer has consumed: ", queue.pop(0))
    mutex.release()
    empty.release()



import random
total = []

for i in range(max_c):
    total.append(threading.Thread(target=producer,args=[i]))
    total.append(threading.Thread(target= consumer,args=[i]))

random.shuffle(total)

for i in total:
    i.start()
    time.sleep(1)

for i in total:
    i.join()
