class DataNode:
    def __init__(self, student=None, data=None):
        self.data = data
        self.student = student
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
            print("|",head.student,head.data,"|",end="")
            count += 1
            if self.count != count:
                print(" -> ",end="")
            head = head.next
        print("|",head.student,head.data,"|",end="")
    def find_mean(self,mean):
        curr = self.head
        if curr is None:
            print("This is an empty list.")
            return
        #process
        # almost_mean = self.head
        find_first_almost_mean = True 
        almost_mean = None #เราจะไม่เอาตัวแรกhead มาใส่เพราะมีโอกาสที่ตัวแรกจะมีค่าเยอะกว่า mean และใกล้เคียง meanมากที่สุด
        while curr != None:
            if find_first_almost_mean: #หาตัวแรกสุดที่ค่าน้อกว่า mean เพื่อเริ่มเปรียบเทียบ
                if curr.data <= mean:
                    find_first_almost_mean = False
                    almost_mean = curr
                    curr = curr.next
                    continue
                curr = curr.next
            else:# เริ่มเปรียบเทียบพอเจอตัวแรกละ
                if (abs(curr.data - mean) < abs(almost_mean.data - mean)) and curr.data <= mean: #เปรียบเทียบระยะห่าง
                    almost_mean = curr
                curr = curr.next
        
        if almost_mean is None:
            return
        print(str(almost_mean.student)+"	"+str(almost_mean.data))
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
    def insert_last_student(self,student,data):
        node = DataNode(student,data)
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
    def insert_index(self,index,data):
        prev = self.head
        insert_node = DataNode(data)
        if index == self.count:
            self.insert_last(data)
            return
        if index > self.count - 1 or index < 0:
            # print("Wrong index")
            return
        count = 0
        #insert head
        if index == 0:
            self.insert_front(data)
            return
        while prev != None:
            if count+1 == index: #อยู่ที่nodeก่อนหน้าที่จะถึงindex
                next_node = prev.next
                prev.next = insert_node
                insert_node.next = next_node
                self.count += 1
                return
            prev = prev.next
            count += 1
                
def main():
    linklist = SinglyLinkedList()
    loop = int(input())
    if not loop:
        return
    mean = 0
    for i in range(loop):
        student, data = input().split()
        mean += float(data)
        linklist.insert_last_student(int(student), float(data))
    mean /= loop
    # print(mean)
    linklist.find_mean(mean)
    # linklist.traverse()
main()
