#IPC using Shared Memory
"""
Client Code:
1. Same as server, name is enough for shared memory
2. get input from user and set it to the buffer
3. Reset the buffer before updating to new value
"""

from multiprocessing import shared_memory

shm_client = shared_memory.SharedMemory(name="sm3")
buffer = shm_client.buf

while True:
    server_data = bytes(buffer[:100]).decode('utf-8')
    print("Server Says",server_data)
    data = input("Input data ('exit' to exit): ")
    buffer[:100] = b'\x00' * 100 #clearing the buffer
    message = data.encode("utf-8")
    buffer[:len(message)] = message
    if data == "exit":
        buffer[:4] = b'exit'
        shm_client.close()
        shm_client.unlink()
        break


shm_client.close()