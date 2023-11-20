#Dynamic Memory Allocation
"""
Logic:
    First fit: Search for first available slot
    Best Fit: Search for the smallest available slot close to allocation
    Worst Fit: Search for the largest available slot always
1. If slot is found, reduce the block size with this size and assig
2. If not, send to cant_fit list
"""

def first_fit(blocks,workload):
    assignment = []
    cant_fit = []
    while workload!=[]:
        size = workload.pop(0)
        assigned = False
        for i in blocks:
            if size <= i[1]:
                i[1] -= size
                assignment.append([i[0],size])
                assigned = True
                break
        if not assigned:
            cant_fit.append(size)
    print("Assigned the following:")
    print(assignment)
    if cant_fit!=[]:
        print("Couldn't fit the following")
        print(cant_fit)

def best_fit(blocks,workload):
    assignment = []
    cant_fit = []
    while workload!=[]:
        size = workload.pop(0)
        assigned = False
        #only extra line
        blocks = sorted(blocks, key = lambda x: x[1])
        for i in blocks:
            if size <= i[1]:
                i[1] -= size
                assignment.append([i[0],size])
                assigned = True
                break
        if not assigned:
            cant_fit.append(size)
    print("Assigned the following:")
    print(assignment)
    if cant_fit!=[]:
        print("Couldn't fit the following")
        print(cant_fit)

def worst_fit(blocks,workload):
    assignment = []
    cant_fit = []
    while workload!=[]:
        size = workload.pop(0)
        assigned = False
        blocks = sorted(blocks, key = lambda x: x[1])
        #only extra line
        blocks = blocks[::-1]
        for i in blocks:
            if size <= i[1]:
                i[1] -= size
                assignment.append([i[0],size])
                assigned = True
                break
        if not assigned:
            cant_fit.append(size)
    print("Assigned the following:")
    print(assignment)
    if cant_fit!=[]:
        print("Couldn't fit the following")
        print(cant_fit)

if __name__ == "__main__":
    blocks = [["A",200],["B",150],["C",225]]
    workload = [150, 100, 125, 100]
    b1,w1 = [["A",200],["B",150],["C",225]],[100, 100, 125, 150]
    b2,w2 = [["A",200],["B",150],["C",225]],[100, 100, 125, 150]
    b3,w3 = [["A",200],["B",150],["C",225]],[100, 100, 125, 150]
    print("First Fit")
    first_fit(b1,w1)
    print("Best Fit")
    best_fit(b2,w2)
    print("Worst Fit")
    worst_fit(b3,w3)


