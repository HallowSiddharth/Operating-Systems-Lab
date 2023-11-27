from threading import Thread, Semaphore
import time

readers_count = 0
resource = 0
mutex = Semaphore(1)
readers_sem = Semaphore(1)  # Controls access to the readers_count variable
writer_sem = Semaphore(1)   # Controls access to the resource variable

def reader(reader_id):
    global readers_count, resource
    while True:
        time.sleep(1)
        readers_sem.acquire()
        readers_count += 1
        if readers_count == 1:
            writer_sem.acquire()
        readers_sem.release()

        # Read from the resource
        print(f"Reader {reader_id} is reading resource: {resource}")

        readers_sem.acquire()
        readers_count -= 1
        if readers_count == 0:
            writer_sem.release()
        readers_sem.release()

def writer(writer_id):
    global resource
    while True:
        time.sleep(2)
        writer_sem.acquire()
        # Write to the resource
        resource += 1
        print(f"Writer {writer_id} is writing resource: {resource}")
        writer_sem.release()

# Create reader and writer threads
readers = [Thread(target=reader, args=(i,)) for i in range(3)]
writers = [Thread(target=writer, args=(i,)) for i in range(2)]

# Start the threads
for reader_thread in readers:
    reader_thread.start()

for writer_thread in writers:
    writer_thread.start()

# Wait for all threads to finish
for reader_thread in readers:
    reader_thread.join()

for writer_thread in writers:
    writer_thread.join()