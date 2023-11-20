# Readers Writers Problem

"""
Logic:
    Things to memorize:
        threading.Thread(target= functionname, args = ()) = thread creation
        threading.Condition = Used for condition
        condition.wait() used to wait
        conition.notify() releasing the lock
        with condition: Use always

    We have one shared variable
        reader count
        condition
    
    1. Reader:
        1.1. A reader must wait if there are writers
        (incase there are writers read count will be -1 )
        1.2 When a reader is ready to read, read count +=1
        1.21 print reading and the shared memory
        1.3 Once a reader is finished we again subtract by 1

    2. Writer:
        2.1 Wait until no reader is present
        2.2 Set readcount to -1 to indicate writer is busy
        2.3 modify the shared value
        2.4 reset read count to 0 to say writer has finished
        2.5 IMPORTANT: condition.notify()
    
    3. Driver code:
        1. Create 2 lists of readers and writers, join them and shuffle the list
        2. Start the thread for each in the shuffled list
"""

import threading
import time
import random

condition = threading.Condition()
#Shared Variable
x = 0
reader_count = 0

def reader(i):
    global x
    global reader_count
    with condition:
        #checking if writer is there
        while reader_count == -1:
            condition.wait()
            print(f"Reader {i} is waiting")
        
    #Reader is now ready
    reader_count += 1 
    print(f"Reader {i} is now reading")
    print("Shared data is now: ",x)

    with condition:
        reader_count -= 1
        if reader_count == 0:
            print("No readers are reading")
            condition.notify() #notify the writer

def writer(i):
    global x
    global reader_count
    with condition:
        while reader_count>0:
            condition.wait()
            print(f"Writer {i} is Waiting")
    #Set read_count to -1
    reader_count = -1
    print(f"Writer {i} is now writing")
    time.sleep(0.1)
    x += 1
    print(f"{i} Value of shared memory: ",x)

    with condition:
        reader_count = 0
        condition.notify()
        print(f"Writer {i} has finished writing!")


if __name__ == "__main__":
    val = 10
    readers = [threading.Thread(target = reader, args=(i,)) for i in range(val)]
    writers = [threading.Thread(target = writer, args=(i,)) for i in range(val)]

    total = readers+writers
    random.shuffle(total)

    for i in total:
        i.start()

    for i in total:
        i.join()




        
