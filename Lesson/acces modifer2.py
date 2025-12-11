
"""
private(__) จะมีแต่class method ของตัวเองที่ใช้งานได้
"""

#Encapsulation
class Employee:
    def __init__(self,name,salary,department):
        #private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department
        self.__showdata() #การเรียกใช้งาน private method สามารถเรียกจาก __init__ เพราะอยู่ในclassเดียวกัน
    
    #private method
    def __showdata(self):
        print(f"Name: {self.__name}")
        print(f"Salary: {self.__salary}")
        print(f"Department: {self.__department}")


obj1 = Employee("Kong",20000,"dev")

#ไม่สามารถเปลี่ยนค่าและเรียกใช้งานได้จากภายนอก
#❗ ไม่ได้แก้ค่า self.__name ดั้งเดิม
#แต่เป็นการสร้าง attribute ใหม่ ชื่อ __name ที่อยู่นอก name mangling

obj1.__name = "WHIS"
obj1.__salary = 50000
obj1.__showdata()