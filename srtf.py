"""
SRTF / SJF Pre-emptive code

Structure of a process
Process = [Burst Time, Arrival Time , Process Name]
This is the optimal way to do it without putting in extra code

"""

process_list = [[4,1,"p1"],[2,2,"p2"],[10,3,"p3"]]

#detailed version (simplified version without comments below)
def srtf_premptive(process_list):
    """
    Logic:
    1. For every time interval (1 unit in this case), we check all the processes
    which are available at that instant (arrival time is lower than current time)
    2. We find out the smallest burst time in those
    3. We service that process in that time interval (decrease the burst time by 1)
    4. If a process is completely serviced (burst time is zero), it is removed from
    the process queue.
    5. Repeat steps 1 to 5 till all processes are complete.

    Boundary Cases:
    1. When no process is available in that time interval: We simple +1 to the time
    and continue with the next time interval
    """
    #declaring stuff to display our answer
    completed_process = {}
    gantt_chart = []
    #setting time to 0 initially
    t = 0
    #running loop till all processes are serviced
    while process_list != []:
        #finding out all the available processses in that time interval
        available = []
        for process in process_list:
            arrival_time = process[1]
            if arrival_time <= t:
                available.append(process)
        """
        now that we have available processes, we need to find out
        lowest burst time, since we have the process with burst time as element 0
        we can just sort this list to find out the answer.
        """
        #before that let's address the boundary condition
        if available == []:
            gantt_chart.append("Idle")
            t += 1
            continue
        #else is not required when the 'if' has continue, adding for simplicity
        else:
            t += 1
            available.sort()
            #this is the process with the lowest burst time
            process = available[0]
            updated_process = list(process)
            #servicing the process
            #reduce burst time by 1
            updated_process[0] -= 1
            #add to gantt_chart process name
            gantt_chart.append(process[2])
            #check if there is anything left in bt
            if updated_process[0] == 0:
                #remove the process from the main process list
                #this is why we create a duplicate
                process_list.remove(process)
                process_name = process[2]
                ct = t
                tt = ct - process[1]
                wt = tt - process[0]
                completed_process[process_name] = [ct,tt,wt]

            else:
                #replace the process with current burst time
                process_list.remove(process)
                process_list.append(updated_process)
        
    #that's it
    #let's display our answer
    print(completed_process)
    print(gantt_chart)
    # you can make it display fancy if you want

def simple_srtf(process_list):
    completed_process = {}
    gantt_chart = []
    t = 0
    while process_list != []:
        available = []
        for process in process_list:
            if process[1] <= t:
                available.append(process)
        if available == []:
            gantt_chart.append("Idle")
            t += 1
            continue
        else:
            t += 1
            available.sort()
            process = available[0]
            updated_process = list(process)
            updated_process[0] -= 1
            gantt_chart.append(process[2])
            if updated_process[0] == 0:
                process_list.remove(process)
                process_name = process[2]
                ct = t
                tt = ct - process[1]
                wt = tt - process[0]
                completed_process[process_name] = [ct,tt,wt]

            else:
                process_list.remove(process)
                process_list.append(updated_process)
        
    print(completed_process)
    print(gantt_chart)


if __name__ == "__main__":
    srtf_premptive(process_list)