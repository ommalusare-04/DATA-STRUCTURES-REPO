class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            p = 1

            while temp and p < pos - 1:
                temp = temp.next
                p += 1

            if temp == None:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node

    def delete(self, value):
        temp = self.head

        if temp == None:
            print("List is empty")
            return

        if temp.data == value:
            self.head = temp.next
            return

        prev = temp
        temp = temp.next

        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp == None:
            print("Value is not present in the list")
            return

        prev.next = temp.next

    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        self.head = prev

    def findmid_del(self):
        if self.head == None:
            print("List is empty")
            return

        temp = self.head
        temp1 = self.head
        prev = None

        while temp1 and temp1.next:
            prev = temp
            temp = temp.next
            temp1 = temp1.next.next

        print("Middle Node:", temp.data)

        if prev == None:
            self.head = temp.next
        else:
            prev.next = temp.next

    def del_first_last(self):
        if self.head == None:
            print("List is empty")
            return

        if self.head.next == None:
            self.head = None
            return

        self.head = self.head.next

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def print(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


list1 = SLL()

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

list1.delete(3)
list1.print()

print("Reversed LL:")
list1.reverse()
list1.print()

list1.findmid_del()
list1.print()

list1.del_first_last()
list1.print()