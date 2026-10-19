class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head

            if self.head != None:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head
        p = 1

        while p < pos - 1 and temp != None:
            temp = temp.next
            p += 1
        if temp == None:
            print("Invalid position")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next != None:
            temp.next.prev = new_node
        temp.next = new_node

    def traversal(self):
        if self.head == None:
            print("List is empty")
            return

        temp = self.head

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

        print()


list1 = DLL()

list1.insert(Node(10), 1)
list1.insert(Node(20), 2)
list1.insert(Node(30), 3)
list1.insert(Node(40), 4)

list1.traversal()

list1.insert(Node(25), 3)
list1.traversal()