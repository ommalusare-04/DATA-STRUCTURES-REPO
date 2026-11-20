class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None

    def insert(self,newnode):
        if self.root is None:   # BST is empty
            self.root=newnode    #First Node 
        else:
            temp=self.root
            while True:
                if newnode.data < temp.data:
                    if temp.left is None:
                        temp.left=newnode
                        return
                    else:
                        temp=temp.left

                else:
                    if temp.right is None:
                        temp.right=newnode
                        return
                    else:
                        temp=temp.right

    def inorder(self,rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end="  ")
            self.inorder(rt.right)

b=BST()
b.insert(Node(20))
b.insert(Node(30))
b.insert(Node(10))
b.insert(Node(5))
b.inorder(b.root)


