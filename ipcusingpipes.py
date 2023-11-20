#ipc using pipes
"""
1 read 1 write pipe:
methods:
os.pipe() - readpipe and write pipe
os.fork()
os.close()
os.read(readpipe,1024) 1024 is length in bytes to read
os.write(writepipe,data.encode())

CHILD: READ
PARENT: WRITE

Logic:
1. create the 2 pipes
2. os.fork()
3. If child close parent pipe, then read the data.
4. If parent close the child pipe, send the data and wait to complete.
"""

import os

def r1_w1pipe():
    read_pipe,write_pipe = os.pipe()
    p1 = os.fork()
    if p1 == 0:
        #child process
        os.close(write_pipe)
        print("Reading from read pipe: ")
        data = os.read(read_pipe,1024)
        print("Child Recieved:" ,data.decode())
    else:
        #parent process
        os.close(read_pipe)
        data = "This is a demonstration in piping"
        print("Writing to write pipe: ")
        os.write(write_pipe,data.encode())
        os.wait()

"""
2 pipes, 2 children 1 parent
Logic:
1. Exact same strategy, except we'll have two different pipes
2. Fork twice to create 2 child processes.
3. The parent will finally read both processes.
Here we send data from the children, the parent recieves it.
Extra:
os._exit(0) since we are writing from child, we can close it after writing
os.waitpid(pid,0) waiting to finish the child processses
"""
def pipe2_child2():
    read_pipe1,write_pipe1 = os.pipe()
    read_pipe2,write_pipe2 = os.pipe()
    process = os.fork()

    if process == 0:
        #This is the first Child Process
        os.close(read_pipe1)
        os.close(write_pipe2)
        data = "Data From Child Processs 1"
        os.write(write_pipe1,data.encode())
        os._exit(0) #Closing the child process
    else:
        #let's create the second child
        p2 = os.fork()
        if p2 == 0:
            #This is child 2
            os.close(read_pipe2)
            os.close(write_pipe1)
            data = "Data From Child Process 2"
            os.write(write_pipe2,data.encode())
            os._exit(0)
        else:
            #Let's wait for the child process to finish
            os.waitpid(process,0)
            os.waitpid(p2,0)
            #This is the parent, everything twice as 2 pipes
            os.close(write_pipe1)
            os.close(write_pipe2)
            data_1 = os.read(read_pipe1,1024)
            data_2 = os.read(read_pipe2,1024)
            print("PIPE1: ",data_1.decode())
            print("PIPE2: ", data_2.decode())

if __name__ == "__main__":
    pipe2_child2()
    r1_w1pipe()
    
