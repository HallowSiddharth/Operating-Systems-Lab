import time
import multiprocessing.shared_memory as shared_memory
# Server code
shm_server = shared_memory.SharedMemory(create=True, size=100, name='sm2')
buffer = shm_server.buf
while True:
        # Display the data from shared memory
        server_data = bytes(buffer[:100]).decode('utf-8')
        print("Server data in memory:", server_data)
        # Check if the data in shared memory equals "exit" and terminate if 
        #true
        if buffer[:4] == b'exit':
            shm_server.close()
            shm_server.unlink()
            break
        time.sleep(5)

"""
multiprocessing.shared_memory.SharedMemory
True,size = 100, name sm2
buffer = shm_server.buf
bytes(buffer[:100]).decode()
if buffer[:4] == b"exit"
shmserver.unlink
shmserver.close
break

"""