class DataNode:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
      self.head = None
      self.count = 0
    def insert_last(self,data):
        add_node = DataNode(data)
        curr_node = self.head
        if curr_node is None:
            self.head = add_node
            return
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = add_node
        self.count += 1

    def traverse(self):
        curr_node = self.head
        if  curr_node is None:
            print("This is an empty list.")
            return
        while curr_node.next != None:
            print(curr_node.data,end=" -> ")
            curr_node = curr_node.next
        print(curr_node.data)

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    mylist.insert_last(input())
  mylist.traverse()

main()