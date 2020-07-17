# We need to define a node class to input into our Ring Buffer
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 



class RingBuffer:
    def __init__(self, capacity):
        self.index = 0 
        self.capacity = capacity
        self.list = []

    def append(self, item):
        #check to see if the list is full
            #if so then update the head element inside the Buffer
        if len(self.list) == self.capacity:
            self.list[self.index] = item 
        else:
            #else just append the item to the Buffer 
            self.list.append(item)

        #we update the array to get back to zero 
        self.index = (self.index + 1) % self.capacity

    def get(self):
        #return the list 
        return self.list

llist = RingBuffer(5)
llist.append('a')
llist.append('b')
llist.append('c')
llist.append('d')
llist.append('e')
print('=======')
llist.get()