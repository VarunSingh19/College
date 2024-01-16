# # Insertion and Deletion in Linked List:
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def printList(self):
#         temp = self.head
#         if not temp:
#             print("List is empty")
#             return
#         else:
#             print("Head/Start :")
#         while temp:
#             print(temp.data, end="->")
#             temp = temp.next

#     def insert(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         elif self.head.data >= new_node.data:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next and new_node.data > current.next.data:
#                 current = current.next
#             new_node.next = current.next
#             current.next = new_node
#     def delete(self, key):
#         if self.head is None:
#             print("Deletion: the given list is empty")
#             return

#         if self.head.data == key:
#             self.head = self.head.next
#             return

#         current = self.head
#         previous = None
#         while current:
#             if current.data == key:
#                 break
#             previous = current
#             current = current.next

#         if current is None:
#             print("\nDeletion: key not found")
#         else:
#             previous.next = current.next


# if __name__ == '__main__':
#     LL = LinkedList()
#     LL.printList()
#     LL.insert(10)
#     LL.insert(12)
#     LL.insert(8)
#     LL.insert(11)
#     LL.insert(15)
#     LL.insert(13)
#     LL.printList()
#     LL.delete(7)
#     LL.delete(8)
#     LL.delete(13)
#     LL.printList()

# import matplotlib.pyplot as plt
# plt.plot([1,2,3,4],[10,15,13,18])

import pandas as pd
data = pd.read_csv(r'C:\Users\varun\Desktop\College\DSA using Python\College DSA Notes\Linked List\Hard\data.csv')
data.drop_duplicates()
print(data)

import re
text =  'Email me at varun@gmail.com or call me at 123-456-789'
emails =  re.findall(r'[\w\.-]+@[\w\.-]+',text)
print(emails)