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
    def delete(data):
        pass
    def MaximumLeft(self,node):
        curr = node.left
        while curr is not None and curr.right is not None:
            curr = curr.right
        return curr
    def dfs_delete(self,node:BSTNode,data):
        if node is None:
            print(f"Delete Error,",data, "is not found in Binary Search Tree.")
            return None
        if node.data > data:
                node.left = self.dfs_delete(node.left, data)
        elif node.data < data:
                node.right = self.dfs_delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            Max_value_node = self.MaximumLeft(node)
            node.data = Max_value_node.data
            node.left = self.dfs_delete(node.left, Max_value_node.data)
        return node
                
    def delete(self,data):
        if self.root:
            self.root = self.dfs_delete(self.root,data)
        else:
            return None
def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()