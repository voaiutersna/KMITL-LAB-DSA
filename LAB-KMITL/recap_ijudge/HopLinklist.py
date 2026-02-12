
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
        print("Cannot delete, "+data+" does not exist.")
    def reverse(self):
        if not self.count:
           print("Can not Reverse (This is an empty Linklist)")
           return
        if self.count == 1:
           return

        prev_node = None
        curr_node = self.head

        while curr_node is not None:
           next_node = curr_node.next
           curr_node.next = prev_node
           prev_node = curr_node
           curr_node = next_node

        self.head = prev_node
    def MergeTwoSortedLists(self,linklist1,linklist2):
        if not linklist1.count and not linklist2.count:
           return
        if linklist1.count and not linklist2.count:
           return linklist1
        if not linklist1.count and linklist2.count:
           return linklist2
        curr1 = linklist1.head
        curr2 = linklist2.head
        result = SinglyLinkedList()
        while curr1 is not None and curr2 is not None:
            if curr1.data <= curr2.data:
               result.insert_last(curr1.data)
               curr1 = curr1.next
               if curr1 is None:
                    result_node = result.head
                    while result_node.next != None:
                      result_node = result_node.next
                    result_node.next = curr2
                    return result
            else:
               result.insert_last(curr2.data)
               curr2 = curr2.next
               if curr2 is None:
                    result_node = result.head
                    while result_node.next != None:
                      result_node = result_node.next
                    result_node.next = curr1
                    return result
        return result
    def HopLinklist(self):
        curr = self.head
        if self.count == 0:
           return
        
        #Test1 : 1 2 3 4 5 6 | 1 -> 3 -> 5
        #Test2 : 1 2 3 4 5 6 7| 1 -> 3 -> 5 -> 7
        first = True
        isprint = True
        while curr != None:
            if first:
              first = False
              print(curr.data,end="")
              isprint = False
              curr = curr.next
              continue
            if isprint is False:
               isprint = True
               curr = curr.next
               continue
            print(" -> ",end="")
            print(curr.data,end="")
            isprint = False
            curr = curr.next
        print()
           
def main():
    # Test Case 1: Reverse list ที่มีหลาย elements
    print("=== Test Case 1: Multiple elements ===")
    mylist = SinglyLinkedList()
    mylist.insert_last("A")
    mylist.insert_last("B")
    mylist.insert_last("C")
    mylist.insert_last("D")
    print("Before reverse:")
    mylist.traverse()  # A -> B -> C -> D
    mylist.reverse()
    print("After reverse:")
    mylist.traverse()  # D -> C -> B -> A

    # Test Case 2: Empty list
    print("\n=== Test Case 2: Empty list ===")
    empty_list = SinglyLinkedList()
    empty_list.reverse()  # Should print error message

    # Test Case 3: Single element
    print("\n=== Test Case 3: Single element ===")
    single = SinglyLinkedList()
    single.insert_last("X")
    print("Before reverse:")
    single.traverse()  # X
    single.reverse()
    print("After reverse:")
    single.traverse()  # X

    # Test Case 4: Two elements
    print("\n=== Test Case 4: Two elements ===")
    two = SinglyLinkedList()
    two.insert_last("1")
    two.insert_last("2")
    print("Before reverse:")
    two.traverse()  # 1 -> 2
    two.reverse()
    print("After reverse:")
    two.traverse()  # 2 -> 1

main()

# Test MergeTwoSortedLists
print("\n=== Test MergeTwoSortedLists ===")

# Test Case 1: ปกติ
print("\nTest 1: list1 = [1,2,4], list2 = [1,3,4]")
list1 = SinglyLinkedList()
list1.insert_last(1)
list1.insert_last(2)
list1.insert_last(4)

list2 = SinglyLinkedList()
list2.insert_last(1)
list2.insert_last(3)
list2.insert_last(4)

merger = SinglyLinkedList()
result = merger.MergeTwoSortedLists(list1, list2)
result.traverse()  # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4

# Test Case 2: list หนึ่งว่าง
print("\nTest 2: list1 = [], list2 = [0]")
list1 = SinglyLinkedList()
list2 = SinglyLinkedList()
list2.insert_last(0)

merger = SinglyLinkedList()
result = merger.MergeTwoSortedLists(list1, list2)
result.traverse()  # Expected: 0

# Test Case 3: ทั้งสอง list ว่าง
print("\nTest 3: list1 = [], list2 = []")
list1 = SinglyLinkedList()
list2 = SinglyLinkedList()

merger = SinglyLinkedList()
result = merger.MergeTwoSortedLists(list1, list2)
if result:
    result.traverse()
else:
    print("Empty result")

# Test Case 4: list ยาวไม่เท่ากัน
print("\nTest 4: list1 = [1,2], list2 = [3,4,5,6]")
list1 = SinglyLinkedList()
list1.insert_last(1)
list1.insert_last(2)

list2 = SinglyLinkedList()
list2.insert_last(3)
list2.insert_last(4)
list2.insert_last(5)
list2.insert_last(6)

merger = SinglyLinkedList()
result = merger.MergeTwoSortedLists(list1, list2)
result.traverse()  # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6
