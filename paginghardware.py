# Paging Hardware
# Effective lines of code: 51
""""
Summary: We have to fit the logical pages into the main memory
Things to know:
    1. Logical pages are what your process is broken down into.
    2. Each Logical page will have a page size, which is what one
    single page is broken down to.
    3. In Main Memory, there will be frames, each frame will be allocated
    with one page from the process.
    4. PAGE SIZE = FRAME SIZE always, or else this doesn't work.
    5. Also, the size of the physical address should always be greater
    than the size of the logical address because then only all the pages
    can be alloted to frames in the main memory
    6. Page Table: A data structure which keeps track of all the pages alloted to which frame

Logic:
    I/P : Logical Address Size
          Physical Address Size
          Page Size
          Starting Address of the main memory page table

    Functions: create_page_table, map_page_table, display, get_physical_address()
    1. Create a class called "PageTable"
    2. In this class, initialize the following:
        1. Page Size
        2. Starting Address
        3. No of Frames = Physical Address Size // Page Size
        4. No of Pages = Logical Address Size // Page Size
        5. Logical Address Size
        6. PageTable = []

    3. create_page_table():
        3.1 Format [Frame Number, Page Number, Starting Address]
        3.2 since we know number of frames iterate from frame 0
        3.3 when it is 0, starting address will that of the input
        3.4 Else, it will be starting address of prev entry + page size
        3.5 The Page Number will be -1, indicating it is not allocated yet
    
    4. map_page_table():
        4.1 We use the random module for this function.
        4.2 we know the number of pages, so we iterate through that.
        4.3 For each page allocation, we check all the available frames.
        4.4 We pick a random one from that and allocate
    
    5. get_physical_address(logical_address):
        5.1 Find out what page the logical address is in
        5.2 Find out the offset (what subpage) the address is
        5.3 Iterate through page table, find the corresponding page.
        5.4 Add the offset to the starting address of that page.
        5.5 That is the physical address, return it.
"""
import random

class PageTable:

    def __init__(self,physical_address_size, logical_address_size, page_size, starting_address):
        self.pages = logical_address_size // page_size
        self.frames = physical_address_size // page_size
        self.page_size = page_size
        self.start_addr = starting_address
        self.page_table = []
        self.logi_size = logical_address_size

    def create_table(self):
        #we know the number of frames
        #Format : Frame_No  Page_no Start_Addr
        for frame_no in range(self.frames):
            if frame_no == 0:
                self.page_table.append([frame_no,-1,self.start_addr])
            else:
                st_address = self.page_table[-1][-1] + self.page_size
                self.page_table.append([frame_no,-1,st_address])
    
    def map_table(self,page):
        free = []
        for frame_no in range(self.frames):
            if self.page_table[frame_no][1] == -1:
                free.append(frame_no)
        
        frame = random.choice(free)
        self.page_table[frame][1] = page

    #simply allocating all the pages
    def allocate(self):
        for i in range(self.pages):
            self.map_table(i)
    
    def get_physical_addr(self,logical_addr):
        #Constraint: Logical addr should be within 0 to logical size-1
        #we need to find which page it is in
        page_no = logical_addr // self.pages
        offset = logical_addr % self.pages

        for frame in self.page_table:
            if frame[1] == page_no:
                physical_addr = frame[2] + offset
        #you can add exceptional handling with the constraint if you wish
        return physical_addr

    #writing a method to display page table
    def display(self):
        print(f"Frame Number\tPage Number\t Starting Address")
        for entry in self.page_table:
            print(f"{entry[0]}\t\t{entry[1]}\t\t{entry[2]}")

#that's it, now we just need driver code
if __name__ == "__main__":
    physical_address_size = int(input("Enter Physical Address Size: "))
    logical_address_size = int(input("Enter Logical Address Size: "))
    page_size = int(input("Enter the Page Size: "))
    starting_address = int(input("Enter the starting address: "))

    page_table = PageTable(physical_address_size,logical_address_size,page_size,starting_address)
    page_table.create_table()
    print("Before Allocation:")
    page_table.display()

    page_table.allocate()
    print("After Allocation: ")
    page_table.display()

    l_a = int(input(f"Enter a logical address from 0 to {logical_address_size - 1}"))
    phys_addr = page_table.get_physical_addr(l_a)
    print("Physical Address: ", phys_addr)
    