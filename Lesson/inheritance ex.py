class Employee:
    # class variable
    company = "KMITL"
    project = "CODING OOP"
    __minsalary = 200000
    #constructure จะวิ่งมายัง class ลูกด้วย
    def __init__(self,name,salary,department):  # จะถูกเรียกใช้งานทันทีที่มีการสร้าง object คนเลยนิยม เอา __init__ มาเก็บค่า attribute
        print("defult Constructor")
        self.name = name
        self.salary = salary
        self.department = department

    #สร้าง method
    def showdata(self):
        print(f"Name : {self.name}")
        print(f"salary : {self.salary}")
        print(f"department : {self.department}")
    
#class ลูกสามารถเข้าถึง public กับ protected ได้
class Accounting(Employee):
    __department = "department:Account"
    def __init__(self):
        pass
class Programmer(Employee):
    __department = "department:Programmer"
    def __init__(self):
        pass
class Sale(Employee):
    __department = "department:Sale"
    def __init__(self):
        pass

"""ถ้าclassลูกไม่สร้าง constructure ในการสร้าง object มันจะไปดึง constructure ของclassแม่แบบauto"""
"""classลูกไม่สามารถเข้าถึงprivateของclassแม่ได้"""

account = Accounting() # สร้าง object จาก class account 
print(account.company)

programmer = Programmer() # สร้าง object จาก class programmer
print(programmer.project)

sale = Sale() # สร้าง object จาก class sale
"""การดึง variable private ของ classแม่มาใช้งาน ต้องเข้าถึงclassแม่ก่อน"""
print(sale._Employee__minsalary)

