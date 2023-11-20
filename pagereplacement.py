#Page Replacement Algorithms
"""
Types:
    1. First In First Out
    2. Least Recently Used
    3. Optimal

Breaking down the logic:
1. We seperate the finding page fault from the actual process.
    This is to reduce complexity (you'll see)
    Finding page fault = previous frame != current frame
2. For LRU and Optimal, we'll use the index functions to see
which to eliminate
    by finding the index by reverse a sliced list (you'll see)
    we can reduce complexity in this comparison
"""

#We can write this into a class, or just different fxns

def FIFO(processes,frame_size):
    #this is where we do all our stuff
    #initializing everything to be blank
    tracker = [["-" for _ in range(frame_size)] for i in range(len(processes))]
    replace = 0
    page_fault = 0
    for i in range(len(processes)):
        process = processes[i]
        #Copying previous alignment to make changes
        if i>=1:
            tracker[i] = list(tracker[i-1])
        if process not in tracker[i]:
            #We replace the the page which our replace variable points
            #Since it's FIFO, we can just +1 % Frame size, to always know
            #what to replace.
            page_fault += 1 #adding a page fault
            tracker[i][replace] = process
            #setting so that next time fifo is followed
            #1st element... 2nd element... nth element, then repeat
            replace = (replace+1) % frame_size
    
    #that's it
    print("First In First out")
    print("Page Faults: ",page_fault)
    for i in tracker:
        print(i)

def LRU(processes,frame_size):
    tracker = [["-" for _ in range(frame_size)] for i in range(len(processes))]
    page_fault = 0
    #Here what to replace we have to find out, doesn't follow a pattern
    #So no need to define it
    for i in range(len(processes)):
        process = processes[i]
        #Copying previous alignment to make changes
        if i>=1:
            tracker[i] = list(tracker[i-1])
        if process not in tracker[i]:
            page_fault += 1
            #initially we just fillup the empty spaces
            if "-" in tracker[i]:
                ind = tracker[i].index("-")
                tracker[i][ind] = process
            #if not
            else:
                recent = processes[:i]
                #preventing shallowcopy and reversing it
                recent = list(recent)
                recent = recent[::-1]
                #Now we check which has the largest index in reverse list
                ind_to_replace = None
                for p in tracker[i]:
                    temp_index = recent.index(p)
                    if ind_to_replace is None:
                        ind_to_replace = temp_index
                    if temp_index > ind_to_replace:
                        ind_to_replace = temp_index
                #element to replace
                element_to_replace = recent[ind_to_replace]
                #Now we have what element to replace
                #We need to find the position in frame to replace
                ind = tracker[i].index(element_to_replace)
                #Replace
                tracker[i][ind] = process
    #that's it
    print("Least Recently Used")
    print("Page Faults : ", page_fault)
    for i in tracker:
        print(i)


def optimal(processes,frame_size):
    """Here we do the opposite
    Search for the highest index from the remaining processes
    No need to do reverse"""
    tracker = [["-" for _ in range(frame_size)] for i in range(len(processes))]
    page_fault = 0
    #Here what to replace we have to find out, doesn't follow a pattern
    #So no need to define it
    for i in range(len(processes)):
        process = processes[i]
        #Copying previous alignment to make changes
        if i>=1:
            tracker[i] = list(tracker[i-1])
        if process not in tracker[i]:
            page_fault += 1
            #initially we just fillup the empty spaces
            if "-" in tracker[i]:
                ind = tracker[i].index("-")
                tracker[i][ind] = process
            #if not
            else:
                element_to_replace = None
                ind_to_replace = None
                #p is the processes in the page
                for p in tracker[i]:
                    if p in processes[i+1:]:
                        temp_ind = processes[i+1:].index(p)
                        if ind_to_replace is None or temp_ind > ind_to_replace:
                            ind_to_replace = temp_ind
                    else:
                        element_to_replace = p

                if element_to_replace == None:
                    if ind_to_replace is None:
                        element_to_replace = tracker[i][0]   
                    else:
                    #element to replace
                        element_to_replace = processes[i+1:][ind_to_replace]
                    #remaining code is the same as LRU
                    #Now we have what element to replace
                    #We need to find the position in frame to replace
                    ind = tracker[i].index(element_to_replace)
                    #Replace
                    tracker[i][ind] = process
                else:
                    ind = tracker[i].index(element_to_replace)
                    #Replace
                    tracker[i][ind] = process

    #that's it
    print("Optimal Page Replacement")
    print("Page Faults : ", page_fault)
    for i in tracker:
        print(i)

import random
if __name__ == "__main__":
    reference = [random.choice([1,2,3,4,5,6,7]) for _ in range(15)]
    frame_size = 4
    print("Reference: ",reference)
    FIFO(reference,frame_size)
    print("Reference: ",reference)
    LRU(reference,frame_size)
    print("Reference: ",reference)
    optimal(reference,frame_size)
