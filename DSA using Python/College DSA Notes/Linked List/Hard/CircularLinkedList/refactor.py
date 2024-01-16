class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")

    def search(self, data):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def delete(self, data):
        if not self.head:
            return

        current = self.head
        prev = None
        while True:
            if current.data == data:
                if current == self.head:
                    # If the head node is being deleted, update the head.
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    self.head = current.next
                    tail.next = self.head
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            if current == self.head:
                break

# Example usage:

my_list = CircularLinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print("Original Circular Linked List:")
my_list.display()

my_list.delete(3)
print("Circular Linked List after deleting 3:")
my_list.display()
