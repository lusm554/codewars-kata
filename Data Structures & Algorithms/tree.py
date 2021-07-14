class Node:
    def __init__(self, sym):
        self.childleft = self.childright = None
        self.data = sym

root = Node('A')
root.childleft = Node('B')
root.childright = Node('C')
root.childleft.childleft = Node('D')
root.childright.childright = Node('E')

def PreOrd(root):
    if root:
        print(root.data)
        PreOrd(root.childleft)
        PreOrd(root.childright)

PreOrd(root)
