#Priority CPU scheduling
#Non pre-emptive

#Process : [Priority, pid, bursttime, arrival time]

def priority(process_list):
    gantt = []
    t = 0
    completed = {}
    while process_list != []:
        available = []
        for p in process_list:
            arrival_time = p[3]
            if arrival_time <= t:
                available.append(p)
        
        if available == []:
            gantt.append("Idle")
            t += 1
            continue
        else:
            available.sort()
            process = available[0]
            #service the process
            #1. remove the process
            process_list.remove(process)
            #2. add to gantt chart
            pid = process[1]
            gantt.append(pid)
            #3. update the time
            burst_time = process[2]
            t += burst_time
            #create an entry in the completed dictionary
            #Calculate ct, tt, wt
            ct = t
            arrival_time = process[3]
            tt = ct - arrival_time
            wt = tt - burst_time
            completed[pid] = [ct,tt,wt]
        
    print(gantt)
    print(completed)

if __name__ == "__main__":
    process_list = [[5,"p1",6,2],[4,"p2",2,5],[1,"p3",8,1],[2,"p4",3,0],[3,"p5",4,4]]
    priority(process_list)