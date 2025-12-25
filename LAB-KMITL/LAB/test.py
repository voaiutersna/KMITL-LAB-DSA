class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    def traverse(self):
        head = self.head
        if head is None:
            print("This is an empty list.")
            return
        count = 0
        while head.next != None:
            print(head.data,end="")
            count += 1
            if self.count != count:
                print(" -> ",end="")
            head = head.next
        print(head.data)
    def insert_last(self,data):
        node = DataNode(data)
        if not self.count:
            self.head = node
            self.count += 1
            return
        head = self.head
        while True:
            if head.next == None:
                head.next = node
                self.count += 1
                return
            head = head.next
    def insert_front(self,data):
        node = DataNode(data)
        if not self.count:
            self.head = node
            self.count += 1
            return
        curr_head = self.head
        self.head = node
        node.next = curr_head
        self.count += 1
    def insert_before(self,node, data):
        new_node = DataNode(node)
        head = self.head
        if head is None:
            print(f"Cannot insert, {node} does not exist.")
            return
        if self.head.data == data:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return
        prev = self.head
        while prev.next != None:
            if prev.next.data == data:
                before = prev.next
                prev.next = new_node
                new_node.next = before
                self.count += 1
                return
            prev = prev.next
        print(f"Cannot insert, {node} does not exist.")
    def delete(self,data):
        pass

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input().strip()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
        mylist.insert_before(*data.split(", "))
    # elif condition == "D":
    #     mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()