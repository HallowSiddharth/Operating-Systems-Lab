#shared memory
"""
Things to remember
import multiprocessing.shared_memory as shared_memory
that has a class called Shared Memory

Logic:
1. Create a shared memory, server side la set the size and create
client side la just name podhum
2. Iterate over a while loop, look at the buffer print it
3. in case buffer says exit, exit the program
"""

import time
import multiprocessing.shared_memory as shared_memory

shm_server = shared_memory.SharedMemory(create=True,size=100,name="sm3")
buffer = shm_server.buf

while True:
    server_data = bytes(buffer[:100]).decode('utf-8')
    print("Server Says: ",server_data)

    if server_data[:4] == "exit":
        shm_server.close()
        shm_server.unlink()
        break

    time.sleep(3)
        