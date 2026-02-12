
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
    def delete(self,data):
        head = self.head
        if not self.count:
           print("Cannot delete, "+data+" does not exist.")
           return
        if head.data == data:
          self.head = head.next
          self.count -= 1
          return
        while head.next is not None:
           if head.next.data == data:
              head.next = head.next.next
              self.count -= 1
              return
           head = head.next
        print("Cannot delete by index, "+data+" does not exist.")
    def insert_index(self,data,index):
        insert_data = DataNode(data)
        index = int(index)
        head = self.head

        # ex node มี 3 -> count = 4 / valid 0-4 
        if self.count < index:
           print("Cannot insert by index, "+data+" does not exist.")
           return
        if head is None and index == 0:
           self.head = insert_data
           self.count += 1
           return
        if not index:
           before_node = self.head
           self.head = insert_data
           insert_data.next = before_node
           self.count += 1
           return
        else:
           count = 0
           while head.next is not None:
                if count + 1 == index:
                    before_node = head.next
                    head.next = insert_data
                    insert_data.next = before_node
                    self.count += 1
                    return
                head = head.next
                count += 1
                if head.next is None and count+1 == index:
                   head.next = insert_data
                   self.count += 1
                   return
        print("Cannot insert by index, "+data+" does not exist.")

                

def main():
    mylist = SinglyLinkedList()
    
    # Test 1: Insert to empty list at index 0
    print("Test 1: Insert 'A' at index 0 (empty list)")
    mylist.insert_index("A", 0)
    mylist.traverse()  # Expected: A
    
    # Test 2: Insert at front (index 0)
    print("\nTest 2: Insert 'B' at index 0")
    mylist.insert_index("B", 0)
    mylist.traverse()  # Expected: B -> A
    
    # Test 3: Insert at middle (index 1)
    print("\nTest 3: Insert 'C' at index 1")
    mylist.insert_index("C", 1)
    mylist.traverse()  # Expected: B -> C -> A
    
    # Test 4: Insert at end (index 3)
    print("\nTest 4: Insert 'D' at index 3 (end)")
    mylist.insert_index("D", 3)
    mylist.traverse()  # Expected: B -> C -> A -> D
    
    # Test 5: Insert at invalid index
    print("\nTest 5: Insert 'E' at index 10 (invalid)")
    mylist.insert_index("E", 10)
    mylist.traverse()  # Expected: error message, list unchanged

main()
