class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current=current.next
        current.next= new_node
    def delete(self,data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current=current.next
    def display(self):
        start =  self.head
        while start:
            print(start.data, end=' ==> ')
            start = start.next
        return False

ll = LinedList()
ll.append('A')
ll.append('B')
ll.append('C')
ll.append('D')
print("Original List : ")
ll.display()

ll.delete('C')
print("\n\nAfter Deleting 'C' from the list :")
ll.display()
