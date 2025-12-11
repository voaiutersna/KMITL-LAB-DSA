"""
Inheritance (การสืบทอด) คือความสามารถในการสร้างคลาสใหม่ (subclass/child class) 
ที่ สืบทอด คุณสมบัติ (attributes) และ พฤติกรรม (methods) มาจากคลาสเดิม (superclass/parent class) 
เพื่อให้สามารถ reuse code, ขยายการทำงาน, และ ลดความซ้ำซ้อน
"""
"""
คลาสแม่
class Employee:

คลาสลูก ที่ต้องการmethodและattribue ของclassแม่
class Programmer(Employee):

"""
class ParentClass:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")

# สืบทอดจาก ParentClass
class ChildClass(ParentClass):
    def play(self):
        print(f"{self.name} is playing")
