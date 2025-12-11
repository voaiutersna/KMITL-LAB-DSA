"""📌 สรุป: การ overide
คำสั่ง	ทำอะไร
self.showdata()	เรียก showdata() ของคลาสตัวเอง
super().showdata()	เรียก showdata() จากคลาสแม่ (superclass)
"""
class Employee:
    # class variable
    company = "KMITL"
    project = "CODING OOP"
    __minsalary = 200000
    
    def __init__(self,name,salary,department):  
        print("Finish assign attribute")
        self.name = name
        self.salary = salary
        self.department = department

    #สร้าง method
    def showdata(self):
        print(f"Name : {self.name}")
        print(f"salary : {self.salary}")
        print(f"department : {self.department}")

    # รายได้ต่อปี
    #overloading method มันก็คือการ set ค่า defualt ใน parameter แหละ
    def getIncome(self,bonus = 0,overtime = 0):
        return (self.salary * 12) + bonus + overtime
    

class Accounting(Employee):
    __departmentname = "department:Account"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentname)
        self.age = age
    """Overide Method"""
    def showdata(self):
        super().showdata() #ไปเรียกใช้งาน showdata() ของclassแม่่ ถ้าเขียน self.showdata() จะเกิดinf loopเพราะเป็นการเรียกshowdata()ของclassตัวเอง
        print(f"อายุของพนักงาน:{self.age}")
        print("----------------------")
        

class Programmer(Employee):
    __departmentname = "department:Programmer"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentname)
        self.exerience = experience
        self.skill = skill
    """Overide Method"""
    def showdata(self):
        super().showdata() #ไปเรียกใช้งาน showdata() ของclassแม่่ ถ้าเขียน self.showdata() จะเกิดinf loopเพราะเป็นการเรียกshowdata()ของclassตัวเอง
        print(f"ประสบการณ์:{self.exerience}")
        print(f"ความสามารถ:{self.skill}")
        print("----------------------")


class Sale(Employee):
    __departmentname = "department:Sale"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentname)
        self.area = area
    """Overide Method"""
    def showdata(self):
        super().showdata() #ไปเรียกใช้งาน showdata() ของclassแม่่ ถ้าเขียน self.showdata() จะเกิดinf loopเพราะเป็นการเรียกshowdata()ของclassตัวเอง
        print(f"ขอบเขตการทำงาน:{self.area}")
        print("----------------------")



account = Accounting("Ray",20000,20) 
account.showdata()
print(f"รายได้ต่อปี: {account.getIncome()}")
print("----------------------")

programmer = Programmer("WHIS",50000,5,"Full-stack") 
programmer.showdata()
print(f"รายได้ต่อปี: {programmer.getIncome(300)}")
print("----------------------")

sale = Sale("despacito",15000,"Bangkok")
sale.showdata()
print(f"รายได้ต่อปี: {sale.getIncome(200,400)}")
print("----------------------")

