class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root=None):
        self.root = root
    def insert(self, data: int=None):
        pNew  = BSTNode(data) 
        if self.root is None:
           self.root = pNew
        else:
           root_node = self.root
           self.insert_recursive(root_node,data)
           
    def insert_recursive(self,node,data):
       pNew = BSTNode(data)
       if data < node.data:
          #ไปซ้าย
            if node.left is None:
                node.left = pNew
            elif node.left != None:
                self.insert_recursive(node.left,data)
       else:
            #ไปขวา
            if node.right is None:
                node.right = pNew
            elif node.right != None:
                self.insert_recursive(node.right,data)
    def preorder(self,node = None): #(Root → Left → Right)
        if node != None:
            print(" ->",node.data,end="")
            self.preorder(node.left)
            self.preorder(node.right)
        else:
            return
    def inorder(self,node = None): #(Left → Root → Right)
        if node != None:
            self.inorder(node.left)
            print(" ->",node.data,end="")
            self.inorder(node.right)
        else:
            return
    def postorder(self,node = None): #(Left → Right → Root)
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(" ->",node.data,end="")
        else:
            return
    def traverse(self):
        if self.root is None:
            print("This is an empty binary search tree.")
            return
        print("Preorder:",end="")
        self.preorder(self.root)
        print(" ")
        print("Inorder:",end="")
        self.inorder(self.root)
        print(" ")
        print("Postorder:",end="")
        self.postorder(self.root)
        print(" ")
    def deepest_left(self,node):
        #basecase
        if node.left is None:
            return node.data
        else:
            return self.deepest_left(node.left)
    def deepest_right(self,node):
        if node.right is None:
            return node.data
        else:
            return self.deepest_right(node.right)
    def find_min(self):
        # print("DEBUG:",self.root.data)
        return self.deepest_left(self.root)
    def find_max(self):
        return self.deepest_right(self.root)
def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
  my_bst.traverse()
  print("Max:", my_bst.find_max())
  print("Min:", my_bst.find_min())

main()
