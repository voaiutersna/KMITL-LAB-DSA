"""
Acess modier ระดับในการเข้าถึง class attribute method และอื่นๆ ในoop โดยมีประโยชน์ สิทะ์ในการใช้งาน

public สามารถเข้าถึงและเรียกใช้ได้หมด ใครก็ได้
protected(_) เข้าถึงได้เฉพาะ class ตัวมันเองและclassลูก แต่จริงๆก็สามารถเรียกใช้แบบ publicได้
private(__) จะมีแต่class method ของตัวเองที่ใช้งานได้
 
"""

#Encapsulation
class Employee:
    def __init__(self,name,salary,department):
        self._namename = name
        self._salary = salary
        self._department = department
    
    #protected method แค่มี _ ข้างหน้า ในการใช้งานหรือการสร้าง แค่นี้เลย แม่งเหมือนกัน
    def _showdata(self):
        print(f"Name: {self._name}")
        print(f"Salary: {self._salary}")
        print(f"Department: {self._department}")


obj1 = Employee("Kong",20000,"dev")
obj1._name = "WHIS"
print(obj1._name)
obj1._showdata()