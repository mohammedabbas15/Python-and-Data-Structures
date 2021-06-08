# A birary tree is one where each node has at most two children, the left
# child and the right child. Trees are used to define hierarchy. It starts
# with the root node and goes all the way down, the last nodes are called
# child nodes.


class Node:

    def __init__(self, data, left = None, right = None):
        self.left = None
        self.right = None
        self.data = data

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.data)
        printTree(node.right, level + 1)
        

#root = Node('A')
#root.childleft = Node('B')
#root.childright = Node('C')
#root.childleft.childleft = Node('D')
#root.childleft.childright = Node('E')
t = Node(1, Node(2, Node(4, Node(7)),Node(9)), Node(3, Node(5), Node(6)))
printTree(t)


