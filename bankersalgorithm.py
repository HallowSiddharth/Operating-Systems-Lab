#Bankers Algorithm
"""
Logic:
1. Calculate the Need Matrix
2. Calculate the safe sequence by comparing need with available
3. Incase a process can't be granted rn, send it to the end of the
process queue.
4. Calculate if safe sequence can be possible at first itself.
How to calculate if safe sequence is in infinite loop?
A: if the amount of non allocated iterations is greater than
the number of processes, we can definitely say that there exists
no safe sequence
"""
#format:
#[pid, A,B,C,D,E]
def calc_need_matrix(allocation,maxm):
    need = []
    for i in range(len(allocation)):
        pid = allocation[i][0]
        a = maxm[i][1] - allocation[i][1]
        b = maxm[i][2] - allocation[i][2]
        c = maxm[i][3] - allocation[i][3]
        d = maxm[i][4] - allocation[i][4]
        need.append([pid,a,b,c,d])
    d = {}
    #converting to a dictionary so that it doesn't matter
    #how much ever we decided to change process list
    print("NEED MATRIX:")
    for i in need:
        pid = i[0]
        d[pid] = i[1:]
        print(pid,d[pid])
    return d

def check(m1,m2):
    ans = True
    for i in range(len(m1)):
        if m1[i] > m2[i]:
            ans = False
    return ans

def bankers(need,process,available):
    print("Proccesses")
    for i in process:
        print(*i)
    #creating a dictionary for allocation
    allo_d = {}
    for i in process:
        allo_d[i[0]] = i[1:]
    safe_seq = []
    #This is what we're using to prevent infinite loop
    reset = 0
    while process!=[] or reset > len(need):
        p = process.pop(0)
        ch = check(need[p[0]],available)
        #p[0] is the process id
        if ch:
            #resetting because there is a process which can pass
            reset = 0
            safe_seq.append(p[0])
            for i in range(len(available)):
                available[i] += allo_d[p[0]][i]
        else:
            reset += 1
            process.append(p)
    if len(safe_seq) >= len(need):
        print("SAFE SEQUENCE POSSIBLE:")
        print(*safe_seq,sep="->")
    else:
        print("SAFE SEQUENCE NOT POSSIBLE DUE TO")
        print(process)

if __name__ == "__main__":
    allocation = [["p0",0,1,1,0],["p1",1,2,3,1],["p2",1,3,6,5],
                  ["p3",0,6,3,2],["p4",0,0,1,4]]
    maxm = [["p0",0,2,1,0],["p1",1,6,5,2],["p2",2,3,6,6],
                  ["p3",0,6,5,2],["p4",0,6,5,6]]
    available = [1,5,2,0]
    need = calc_need_matrix(allocation,maxm)
    bankers(need,allocation,available)




