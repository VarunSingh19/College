# Simple Queue.;

# def Simple_Queue():
#     queue = []
#     queue.append(1)
#     queue.append(3)
#     queue.append(2)
#     print(queue)
#     print(queue.pop())
#     print(queue)
# Simple_Queue()

# Implementation using Collection deque
# from collections import deque
# def Deque_Problem ():
#     queue = deque()
#     queue.append(1)
#     queue.append(2)
#     queue.append(3)
#     print(queue)
#     print(queue.popleft())
#     print(queue)
# Deque_Problem()
 
# # Using a user Defined Linked List:
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def empty(self):
        return self.front is None

    def enqueue(self, item):
        temp = QueueNode(item)
        if self.rear is None:
            self.front = temp
            self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.empty():
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("Current Front Element: " + str(queue.front.data))
    print("Current Rear Element: " + str(queue.rear.data))

    queue.dequeue() #Eliminating 1
    queue.dequeue() #Eliminating 2

    print("Queue Current Front: " + str(queue.front.data))
    print("Queue Current Rear: " + str(queue.rear.data))
