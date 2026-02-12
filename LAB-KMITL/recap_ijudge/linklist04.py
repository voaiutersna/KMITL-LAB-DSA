class DataNode:
  def __init__(self,data=None):
    self.data = data
    self.next = None
class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.count = 0
    def insert_last(self,data):
        add_node = DataNode(data)
        curr_node = self.head
        if not self.count:
            self.head = add_node
            self.count += 1
            return
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = add_node
        self.count += 1

    def insert_front(self,data):
        add_node = DataNode(data)
        
        if not self.count:
            self.head = add_node
            self.count += 1
            return
        head_node = self.head
        add_node.next = head_node
        self.head = add_node
        self.count += 1

    def traverse(self):
        curr_node = self.head
        if not self.count:
            print("This is an empty list.")
            return
        while curr_node.next != None:
            print(curr_node.data,end=" -> ")
            curr_node = curr_node.next
        print(curr_node.data)
    def insert_before(self,node, data):
        insert_node = DataNode(data)
        curr = self.head
        if not self.count:
          print("Cannot insert, "+node+" does not exist.")
          return
        
        if curr.data == node:
           insert_node.next = self.head
           self.head = insert_node
           self.count += 1
           return

        while curr.next != None:
            if curr.next.data == node:
              before_node = curr.next
              curr.next = insert_node
              insert_node.next = before_node
              self.count += 1
              return
            curr= curr.next
        print("Cannot insert, "+node+" does not exist.")
def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    # elif condition == "D":
    #    mylist.delete(data)
    else:
        print("Invalid Condition!")
  mylist.traverse()

main()