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

    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
        arr=[]
        cnt=0
        level=0
        arr.append(rt)
        while(cnt<len(arr)):
            node_count=len(arr)-cnt   # level wise node count
            print(f"level {level}:",end=" ")
            for i in range(node_count):
                temp=arr[cnt]
                cnt+=1

                print(temp.data,end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            print()
            level+=1
                


b=BST()
b.insert(Node(100))
b.insert(Node(10))
b.insert(Node(450))
b.insert(Node(4))
b.insert(Node(300))
b.insert(Node(500))
b.insert(Node(2))
b.insert(Node(7))
print("\nInorder traversal")
b.inorder(b.root)
print("\nLevel wise traversal")
b.level_order(b.root)


