class DataNode:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    #insert node
    def insert_front(self,data):
        Add_Node = DataNode(data)
        #validate
        if self.count == 0:
            self.head = Add_Node
            self.count += 1
            return
        #insert process
        before_node = self.head
        self.head = Add_Node
        self.head.next = before_node
        self.count += 1
    def insert_last(self,data):
        Add_Node = DataNode(data)
        #Validate
        if self.count == 0:
            self.head = Add_Node
            self.count += 1
            return
        
        #insert process
        head = self.head
        while head.next != None:
            head = head.next
        head.next = Add_Node
        self.count += 1
    def insert_before(self,target,data):
        insert_node = DataNode(data)
        #Validate
        if self.count == 0:
            print("Can't insert")
            return
        if self.head.data == target:
            self.insert_front(data)
            return
        curr = self.head
        while curr.next != None:
            if curr.next.data == target:
                before_node = curr.next
                curr.next = insert_node
                insert_node.next = before_node
                self.count += 1
                return
            curr = curr.next
        print("Can't insert")
    def traverse(self):
        head = self.head
        if head is None:
            return
        while head.next != None:
            print(head.data,end=" -> ")
            head = head.next
        print(head.data)
    