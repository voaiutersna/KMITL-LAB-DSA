class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root: int=None):
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
    def preorder(self,node = None):
        if node != None:
            print(" ->",node.data,end="")
            self.preorder(node.left)
            self.preorder(node.right)
        else:
            return

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
  print("Preorder:", end="")
  my_bst.preorder(my_bst.root)
main()
