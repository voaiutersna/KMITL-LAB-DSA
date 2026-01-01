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
        if not self.count:
            print("Cannot insert, ",end="")
            print(node,end="")
            print(" does not exist.")
            return

        new_node = DataNode(data)

        # กรณี node อยู่ที่ head
        if self.head.data == node:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return

        # กรณี node อยู่ตำแหน่งอื่น
        prev = self.head
        curr = self.head.next

        while curr is not None:
            if curr.data == node:
                prev.next = new_node
                new_node.next = curr
                self.count += 1
                return
            prev = curr
            curr = curr.next

        print("Cannot insert, ",end="")
        print(node,end="")
        print(" does not exist.")
    def delete(self, data):
        # กรณี linklist ว่าง
        if self.head is None:
            print("Cannot delete, ",end="")
            print(data,end="")
            print(" does not exist.")
            return
        curr = self.head

        #target is head
        if self.head.data == data:
           self.head = self.head.next
           self.count -= 1
           return
        #target is other
        while curr.next!= None:
            if curr.next.data == data:
              target = curr.next
              curr.next = target.next
              self.count -= 1
              return
            curr = curr.next
        print("Cannot delete, ",end="")
        print(data,end="")
        print(" does not exist.")
    def findindex(self,index):
        head = self.head
        
        if index < 1 or index > self.count:
            print("Error")
            return
        #traverse
        count = 1
        curr = head
        while count <= index:
            if count == index:
                print(curr.data)
                return
            curr = curr.next
            count += 1
def main():
    linklist = SinglyLinkedList()
    while True:
        inp = input()
        if inp == "Last":
            index = int(input())
            # print(linklist.traverse())
            linklist.findindex(int(index))
            break
        linklist.insert_last(inp)
main()