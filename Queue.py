# The Queue is a linear data structure where elements are in sequential manner.
# It follows the F.I.F.O. mechanism that means first in, first out.
# Mechanism of a Queue:
#   front -> points to starting element
#   rear -> points to last element
# There are two operations:
#   enqueue -> inserting an element into the rear
#   dequeue -> deleting an element from the front
# There are two conditions:
#   overflow -> inserting into a full queue
#   underflow -> deleting from an empty queue

class myqueue:

    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def enque(self, element):
        if len(self.data) < 5:
            return self.data.append(element)
        else:
            return 'Overflow'

    def deque(self):
        if len(self.data) == 0:
            return 'Underflow'
        else:
            self.data.pop(0)

b = myqueue()
b.enque(2)
b.enque(3)
b.enque(4)
b.enque(5)
b.enque(6)
print(b.data)
b.deque()
print(b.data)
