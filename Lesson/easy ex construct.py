#การสร้าง constructure
class Employee:
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
        

obj1 = Employee("Whis",100000,"SE")
#การเปลี่ยนค่า attribute
obj1.salary = 200000

obj1.showdata()


