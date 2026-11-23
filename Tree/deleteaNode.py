
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
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
            print(rt.data, end="  ")
            self.inorder(rt.right)

    # Preorder Traversal (Root, Left, Right)
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end="  ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    # Postorder Traversal (Left, Right, Root)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end="  ")

    # Minimum Value
    def minimum(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root

        while temp.left is not None:
            temp = temp.left

        print("Minimum value:", temp.data)

    # Maximum Value
    def maximum(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root

        while temp.right is not None:
            temp = temp.right

        print("Maximum value:", temp.data)

    # Delete Node
    def deleteNode(self, rt, value):
        if rt is None:
            return None

        if value < rt.data:
            rt.left = self.deleteNode(rt.left, value)

        elif value > rt.data:
            rt.right = self.deleteNode(rt.right, value)

        else:
            # Case 1: No left child
            if rt.left is None:
                return rt.right

            # Case 2: No right child
            if rt.right is None:
                return rt.left

            # Case 3: Both children exist
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.deleteNode(rt.right, succ.data)

        return rt

    # Find Inorder Successor
    def get_successor(self, temp):
        temp = temp.right

        while temp.left is not None:
            temp = temp.left

        return temp


# Create BST
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

print("\n\nPREORDER:")
b.preorder(b.root)

print("\n\nPOSTORDER:")
b.postorder(b.root)

# Minimum and Maximum
print("\n\nMINIMUM AND MAXIMUM:")
b.minimum()
b.maximum()

# Delete Node
print("\n\nAfter Deleting 4:")
b.root = b.deleteNode(b.root, 4)
b.inorder(b.root)

# Delete another Node
print("\n\nAfter Deleting 100:")
b.root = b.deleteNode(b.root, 100)
b.inorder(b.root)
