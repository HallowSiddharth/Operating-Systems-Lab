#FCFS
#Process : [arrival_time, burst_time, pid]


def fcfs(process_list):
    t = 0
    gantt = []
    completed = {}
    process_list.sort()
    while process_list != []:
        if process_list[0][0] > t:
            t += 1
            gantt.append("Idle")
            continue
        else:
            process = process_list.pop(0)
            gantt.append(process[2])
            t += process[1]
            pid = process[2]
            ct = t
            tt = ct - process[0]
            wt = tt - process[1]
            completed[pid] = [ct,tt,wt]
    print(gantt)
    print(completed)



if __name__ == "__main__":
    process_list = [[2,6,"p1"],[5,2,"p2"],[1,8,"p3"],[0,3,"p4"],[4,4,"p5"]]
    fcfs(process_list)