"""Setter การหกำหนดค่าให้ Object"""
def setName(self,newname):
    self.__name = newname

"""Getter การดึงค่าจาก private object"""
def getName(self):
    return self.__name

"""-------------------"""

class Employee:
    def __init__(self,name,salary,department):
        #private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department
        self._showdata() #การเรียกใช้งาน private method สามารถเรียกจาก __init__ เพราะอยู่ในclassเดียวกัน
        print("----------------")
    
    #private method
    def _showdata(self):
        print(f"Name: {self.getName()}")
        print(f"Salary: {self.__salary}")
        print(f"Department: {self.getDepartment()}")

    #setter method ไว้ใช้เปลี่ยนค่าจากภายนอกclass
    def setName(self,newname):
        self.__name = newname
    def setSalary(self,newsalary):
        self.__salary = newsalary
    
    #getter method ไว้ใช้แสดงค่าจากภายนอกclass
    def getName(self):
        return self.__name
    def getDepartment(self):
        return self.__department
    


obj1 = Employee("Kong",20000,"dev")

#ทำการเปลี่ยนค่า private object โดยการเรียกใช้ function ในclass (Setter)
obj1.setName("Non") 
obj1.setSalary("50000")

#แสดงผลค่า private object โดยการเรียกใช้ function ใน class (Getter)
print(obj1.getName())
print(obj1.getDepartment())

print("-------------------")
obj1._showdata()