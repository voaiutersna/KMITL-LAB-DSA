"""
isinstnace -> เช็คว่า object นี้ถูกสร้างจาก class ที่เรากำหนดไหม
dir -> แสดง Attribute and method(behavior)
__class__ -> แสดงชื่อ class ของ object 

"""
"""
Struture

isinstance(object, classinfo)
object คือ ตัวแปรหรือออบเจ็กต์ที่ต้องการตรวจสอบ
classinfo คือ ชนิดข้อมูล หรือ คลาส หรือ tuple ของคลาส เช่น int, str, หรือ (int, float)

dir(object=None)
ถ้าใส่ object จะคืนรายชื่อ attribute และ method ของออบเจ็กต์นั้น
ถ้าไม่ใส่อะไรเลย จะคืนชื่อของสโคปปัจจุบัน (เช่น ตัวแปรและฟังก์ชันที่กำหนดไว้ในโปรแกรมตอนนั้น)

object.__class__
คืนค่าคลาสของออบเจ็กต์  

"""
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

"""isinstance"""
print(isinstance(obj1, Employee)) #เช็คว่า obj1 สร้างมาจาก class Employeeหรือป่าว //Result True or False

"""dir"""
print(dir([])) # แสดง list method ของ list
print("--------------")
print(dir(Employee)) # แสดง list method ของ class
print("--------------")
print(dir(obj1)) # แสดง list method ของ obj1
print("--------------")

"""__class__"""
print(obj1.__class__) # obj1 เป็น object จาก class อะไร
