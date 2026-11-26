
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    count=0
    def __init__(self):
        self.root = None

    # Insert Node
    def insert(self, newnode):
        if self.root is None:
            self.root = newnode
        else:
            temp = self.root

            while True:
                if newnode.data < temp.data:
                    if temp.left is None:
                        temp.left = newnode
                        return
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = newnode
                        return
                    else:
                        temp = temp.right

    # Inorder Traversal (Left, Root, Right)
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            if rt.left is None and rt.right is None:
                self.count+=1
            print(rt.data, end="  ")
            self.inorder(rt.right)

    

    

    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key < temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False

    
b = BST()

# Insert Values
b.insert(Node(100))
b.insert(Node(10))
b.insert(Node(450))
b.insert(Node(4))
b.insert(Node(65))
b.insert(Node(300))
b.insert(Node(500))
b.insert(Node(50))

# Display Traversals
print("INORDER:")
b.inorder(b.root)



# if b.search(450):
#     print("\nFound node")
# else:
#     print("\nnot found")


if b.search(1000):
    print("\nFound node")
else:
    print("\nnot found")

