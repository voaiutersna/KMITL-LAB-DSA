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
        if self.head.data == node:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return
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
        if self.head is None:
            print("Cannot delete, ",end="")
            print(data,end="")
            print(" does not exist.")
            return
        curr = self.head
        if self.head.data == data:
           self.head = self.head.next
           self.count -= 1
           return
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
    def delete_front(self):
        if self.head is None:
            return
        front = self.head.data
        self.head = self.head.next
        self.count -= 1
        return front
    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            last = self.head.data
            self.head = None
            self.count -= 1
            return last
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        last = curr.next.data
        curr.next = None
        self.count -= 1
        return last
def main():
    linklist = SinglyLinkedList()
    loop = int(input())
    for i in range(loop):
        inp = int(input())
        linklist.insert_last(inp)
    result = SinglyLinkedList()
    if linklist.count == 1:
        print(linklist.head.data)
        return
    first = True
    while linklist.count > 0:
        if first:
            result.insert_last(linklist.delete_last())
            first = False
        for _ in range(2):
            result.insert_last(linklist.delete_front())
            if not linklist.count:
                result.traverse()
                return
        for _ in range(2):
            result.insert_last(linklist.delete_last())
            if not linklist.count:
                result.traverse()
                return
    result.traverse()
main()

