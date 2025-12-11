"""การแปลงobjectเป็นstring
def __str__(self):
    return "ชุดข้อความ"
"""

class Employee:
    # class variable
    company = "KMITL"
    project = "CODING OOP"
    __minsalary = 200000
    #constructure จะวิ่งมายัง class ลูกด้วย
    def __init__(self,name,salary,department):  # จะถูกเรียกใช้งานทันทีที่มีการสร้าง object คนเลยนิยม เอา __init__ มาเก็บค่า attribute
        print("Finish assign attribute")
        self.name = name
        self.salary = salary
        self.department = department

    #สร้าง method
    def showdata(self):
        print(f"Name : {self.name}")
        print(f"salary : {self.salary}")
        print(f"department : {self.department}")
    def getSalary(self):
        return self.salary * 12
    
    def __str__(self):
        return (f"ชื่อ:{self.name} ตำแหน่ง:{self.department} รายได้ต่อปี: {self.getSalary()}")
    

class Accounting(Employee):
    __departmentname = "department:Account"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)

class Programmer(Employee):
    __departmentname = "department:Programmer"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)

class Sale(Employee):
    __departmentname = "department:Sale"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentname)
        super().showdata()


account = Accounting("Non",20000) # สร้าง object จาก class account 
print(account.getSalary()) # การเรียกใช้งานmethodจากclassแม่
print(account.__str__())

print("----------------")

programmer = Programmer("WHIS",50000) # สร้าง object จาก class programmer
print(programmer.__str__())

print("----------------")

sale = Sale("despacito",15000) # สร้าง object จาก class sale
print(sale.__str__())