#Shortest Seek Time First: SSTF disk scheduling
"""
Logic:
1. You will be given initial head position, and a set of disk requests
2. We always have to choose the shortest seek time abs(head - disk request)
3. add this seektime to the total seektime
4. print the total seektime and the order to the user
"""

def sstf_algo(initial_head,requests):
    current_head = initial_head
    sequence = []
    total_seektime = 0
    while requests != []:
        requests = sorted(requests, key= lambda x: abs(x-current_head))
        next_request = requests.pop(0)
        sequence.append(next_request)
        total_seektime += abs(next_request - current_head)
        current_head = next_request
    
    print("Total Seek time: ", total_seektime)
    print("Order: ", sequence)


if __name__ == "__main__":
    initial_head = 250
    sequence = [100,150,25,275]
    sstf_algo(initial_head,sequence)