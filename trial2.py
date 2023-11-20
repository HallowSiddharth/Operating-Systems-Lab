import multiprocessing.shared_memory as shared_memory
# Client code
shm_client = shared_memory.SharedMemory(name="sm2")
buffer = shm_client.buf
while True:
    server_data = bytes(buffer[:100]).decode('utf-8')
    print("Server says:", server_data)
    user_input = input("Enter 'exit' to quit: ")
    buffer[:100] = b'\x00' * 100
    message_bytes = user_input.encode('utf-8')
    buffer[:len(message_bytes)] = message_bytes
    if user_input == 'exit':
        # Set the "exit" flag in the shared memory to signal the server to 
        #terminate
        buffer[:4] = b'exit'
        shm_client.close()
        shm_client.unlink()
        break

shm_client.close()
