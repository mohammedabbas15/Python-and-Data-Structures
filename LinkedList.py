# Like arrays, Linked List is a linear data structure. Unlike arrays,
# linked list elements are not stored at a contiguous location;
# the elements are linked using pointers.
# Why linked lists?
# Arrays can be used to store data of similar types but arrays have
# the following limitations:
# The size of the array is fixed
# Inserting a new element in an array can be expensive
# Advantages over arrays:
# Dynamic size
# Ease of insertion/deletion


class Node:
    
    # function to initialize Node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    #function to initialize the head
    def __init__(self):
        self.head = None

    # this function prints the contents of a list starting from head
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    # start with the empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # link first node with second
    llist.head.next = second

    # link second node with third
    second.next = third

    llist.printList()
