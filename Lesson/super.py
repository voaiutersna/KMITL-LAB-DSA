"""Super() เมื่อต้องการใช้งานคุณสมบัติต่างๆในclassแม่ ex constructure method attribute"""
"""
Syntax
super().method_name(arguments)

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
    
"""class ลูกสามารถเข้าถึง public กับ protected ได้โดยใช้ super().ชื่อmethod(ข้อมูลที่ต้องการส่งไปยังmethodแม่)"""
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

"""ถ้าclassลูกไม่สร้าง constructure ในการสร้าง object มันจะไปดึง constructure ของclassแม่แบบauto"""
"""classลูกไม่สามารถเข้าถึงprivateของclassแม่ได้"""

account = Accounting("Non",20000) # สร้าง object จาก class account 
account.showdata() #สามาถเรียกใช้ฟังชั่นจากclassแม่ได้ตามปกติ (ถ้าไม่ใช่ private method)

programmer = Programmer("WHIS",50000) # สร้าง object จาก class programmer

sale = Sale("despacito",15000) # สร้าง object จาก class sale

