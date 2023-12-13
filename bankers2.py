#Banker's Algorithm (using dictionaries)

#step 1: Need matrix
def calc_need(allocated,max_):
    need = {}
    for pid in allocated:
        max_list = max_[pid]
        alloc_list = allocated[pid]
        need_values = []
        for i in range(len(max_list)):
            need_values.append(max_list[i] - alloc_list[i])
        need[pid] = need_values
    return need

def bankers(allocated,max_,available):
    need = calc_need(allocated,max_)
    safe_sequence = []
    not_processed = 0
    processes = []
    for pid in allocated:
        processes.append(pid)
    total_processes = len(processes)

    while not_processed < total_processes and len(safe_sequence) != total_processes :
        pid = processes.pop(0)
        #Check if the process can be serviced
        if available >= need[pid]:
            #The process can be serviced
            safe_sequence.append(pid)
            not_processed = 0
            for i in range(len(available)):
                available[i] += allocated[pid][i]
        else:
            not_processed += 1
            processes.append(pid)

    if len(safe_sequence) != total_processes:
        print("No safe sequence possible")
    else:
        print("Safe sequence possible")
        print(*safe_sequence,sep="->")
        print("Avaiable: ",available)
        
#get the input
if __name__ == "__main__":
    available = [3,3,2]
    allocated = {"p0": [0,1,0],"p1":[2,0,0],"p2":[3,0,2],"p3":[2,1,1],"p4":[0,0,2]}
    max_ = {"p0":[7,5,3],"p1":[3,2,2],"p2":[9,0,2],"p3":[2,2,2],"p4":[4,3,3]}
    bankers(allocated,max_,available)
