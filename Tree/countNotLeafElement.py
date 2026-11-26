
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0

    # Insert a node
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    # Inorder Traversal
    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # Preorder Traversal
    def preorder(self, rt):
        if rt is None:
            return

        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    # Postorder Traversal
    def postorder(self, rt):
        if rt is None:
            return

        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    # Count Leaf Nodes
    def count_leaf(self, rt):
        if rt is None:
            return

        if rt.left is None and rt.right is None:
            self.cnt += 1

        self.count_leaf(rt.left)
        self.count_leaf(rt.right)

    # Count Non-Leaf Nodes
    def count_non_leaf(self, rt):
        if rt is None:
            return

        if rt.left is not None or rt.right is not None:
            self.cnt += 1

        self.count_non_leaf(rt.left)
        self.count_non_leaf(rt.right)


# Driver Code
b1 = BST()

b1.insert(Node(34))
b1.insert(Node(44))
b1.insert(Node(54))
b1.insert(Node(23))
b1.insert(Node(12))
b1.insert(Node(345))
b1.insert(Node(3))
b1.insert(Node(4))

# Inorder
print("Inorder:")
b1.inorder(b1.root)

# Preorder
print("\n\nPreorder:")
b1.preorder(b1.root)

# Postorder
print("\n\nPostorder:")
b1.postorder(b1.root)

# Count Leaf Nodes
b1.cnt = 0
b1.count_leaf(b1.root)
print("\n\nTotal Leaf Nodes:", b1.cnt)

# Count Non-Leaf Nodes
b1.cnt = 0
b1.count_non_leaf(b1.root)
print("Total Non-Leaf Nodes:", b1.cnt)
