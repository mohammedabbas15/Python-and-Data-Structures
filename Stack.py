# The stack is a linear data structure where elements are arranged sequentially.
# It follows the mechanism L.I.F.O which means last in first out.
# So, the last element inserted will be removed as the first.
# The operations are:
#   Push -> inserting an element into the stack
#   Pop -> deleting an element from the stack
# The conditions to check are:
#   overflow condition: this condition occurs when we try to put one more
#   element into a stack that is already having maximum elements.
#   underflow condition: this condition occurs when we try to delete an
#   element from an empty stack.

class mystack:
    
    def __init__(self):
        self.data = []

    def length(self):   # return the length of the stack
        return len(self.data)

    def is_full(self):  # check if the list is full or not
        if len(self.data) == 5:
            return True
        else:
            return False

    def push(self, element): # Add an element to the end of the list
        if len(self.data) < 5:
            self.data.append(element)
        else:
            return 'Overflow!'

    def pop(self):  # remove the last element from the list
        if len(self.data) == 0:
            return 'Underflow!'
        else:
            return self.data.pop()


# testing the stack with some operations
a = mystack() # create our object to reference
print(a.length()) # starting length of the stack
a.push(10)
a.push(20)
a.push(25)
a.push(50)
print(a.length())
print(a.is_full())
a.push(33)
print(a.is_full())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.length())
print(a.pop())
