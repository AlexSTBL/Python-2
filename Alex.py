class MyPriorityQueue():
    def __init__(self,size):
        self.cq = []
        self.size = size
            
    def addPriority(self,job):
        if self.maxSize() == self.size:
            print ("Queue is full")
        else:
            self.cq.append(job)

            
    def maxSize(self):
        return len(self.cq)
    
    def find_max_priority(self):
        
        self.cq.sort()
        return(self.cq[-1])
    
    def remove_max_priority(self):
         
        self.cq.pop()
        
    def display_queue(self):
        print(self.cq)
               
see = MyPriorityQueue(4)
see.addPriority(7)
see.addPriority(9)
see.addPriority(6)
see.addPriority(7)
see.addPriority(2)
see.display_queue()
print(see.find_max_priority())
see.remove_max_priority()
see.display_queue()



