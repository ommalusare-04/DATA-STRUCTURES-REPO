class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SCLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def insert(self, new_node, pos):
        if pos == 1:
            if self.head == None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                new_node.next = self.head
                self.head = new_node
                temp.next = self.head
        else:
            temp = self.head
            p = 1

            while p < pos - 1 and temp.next != self.head:
                temp = temp.next
                p += 1

            if p != pos - 1:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node

    def delete(self, value):
        if self.head == None:
            print("List is empty")
            return

        temp = self.head

        if temp.data == value:
            if temp.next == self.head:
                self.head = None
                return

            last = self.head

            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head
            return

        prev = self.head
        temp = self.head.next

        while temp != self.head and temp.data != value:
            prev = temp
            temp = temp.next

        if temp == self.head:
            print("Value is not present in the list")
            return

        prev.next = temp.next

    def print(self):
        if self.head == None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.head:
                break

        print()


list1 = SCLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))

list1.print()

list1.insert(Node(34), 1)
list1.print()

list1.insert(Node(50), 6)
list1.print()

list1.insert(Node(2), 2)
list1.print()

list1.delete(2)
list1.print()

list1.delete(10)
list1.print()

list1.delete(100)
list1.print()