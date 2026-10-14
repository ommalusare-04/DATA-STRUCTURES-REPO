class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    # Insert node at a specific position
    def insert(self, new_node, pos):
        if pos == 1:
            if self.head is None:
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

            new_node.next = temp.next
            temp.next = new_node

    # Delete node by value
    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        prev = None

        # If the first node contains the value
        if temp.data == value:
            if temp.next == self.head:
                self.head = None
            else:
                last = self.head

                while last.next != self.head:
                    last = last.next

                self.head = temp.next
                last.next = self.head
            return

        prev = temp
        temp = temp.next

        while temp != self.head:
            if temp.data == value:
                prev.next = temp.next
                return

            prev = temp
            temp = temp.next

        print("Value not found")

    # Print list elements
    def print(self):
        print("\nList elements:")

        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.head:
                break

        print()


list1 = SLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))
list1.append(Node(60))

list1.print()

list1.insert(Node(58), 1)
list1.print()

list1.insert(Node(25), 2)
list1.print()

list1.delete(40)
list1.print()