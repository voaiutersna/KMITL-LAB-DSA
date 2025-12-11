"""Setter การหกำหนดค่าให้ Object"""
def setName(self,newname):
    self.__name = newname

"""Getter การดึงค่าจาก private object"""
def getName(self):
    return self.__name

"""-------------------"""

class Employee:
    #class variable //ไม่จำเป้นต้องสร้าง object
    _minSalary = 12000
    _maxSalary = 50000
    _companyname = "KMITL"

    def __init__(self,name,salary,department):
        # instance variable //จำเป็นต้องสร้าง objectเพื่อเก็บข้อมูลและแสดงผล
        self.__name = name
        self.__salary = salary
        self.__department = department
        self._showdata() 
        print("----------------")
    
    #private method
    def _showdata(self):
        print(f"Name: {self.__name}")
        print(f"Salary: {self.__salary}")
        print(f"Department: {self.__department}")


obj1 = Employee("Kong",20000,"dev")

print(Employee._minSalary) #จะเห็นว่า variable นี้ไม่จำเป็นต้องสร้าง object ก็แสดงผลได้
print(Employee._companyname)