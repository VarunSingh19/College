class Root_Node:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.val = item

def Inorder_Traverse(root):
    if root:
        Inorder_Traverse(root.left)
        print(str(root.val) +  "->",end="")
        Inorder_Traverse(root.right)

def Postorder_Traverse(root):
    if root:
        Postorder_Traverse(root.left)
        Postorder_Traverse(root.right)
        print(str(root.val) +  "->",end="")
        
def Preorder_Traverse(root):
    if root:
        print(str(root.val) +  "->",end="")
        Preorder_Traverse(root.left)
        Preorder_Traverse(root.right)

root = Root_Node(1)
root.left = Root_Node(2)
root.right = Root_Node(3)
root.left.left = Root_Node(4)
root.left.right = Root_Node(5)
root.right.left = Root_Node(6)
root.right.right = Root_Node(7)
root.left.left.left = Root_Node(8)
root.left.left.right = Root_Node(9)
root.left.right.left = Root_Node(10)
root.left.right.right = Root_Node(11)


print("\nPreorder Traversal :") #First Visit
Preorder_Traverse(root)
print("\nInorder Traversal :") #Second Time Visit
Inorder_Traverse(root)
print("\nPostorder Traversal :") # Third Time Visit
Postorder_Traverse(root)
