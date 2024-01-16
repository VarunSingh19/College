class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # Corrected the assignment to connect the last node to the head.

    def delete(self, key):
        if not self.head:
            return
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
        else:
            temp = self.head
            prev = None
            while temp.next != self.head:
                prev = temp
                temp = temp.next
                if temp.data == key:
                    prev.next = temp.next
                    break

    def display(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print()

clist = CircularLinkedList()
clist.insert(1)
clist.insert(2)
clist.insert(3)
clist.display()
clist.delete(2)
clist.display()
