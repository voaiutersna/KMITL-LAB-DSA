"""
การ import class เข้ามาใช้งานจากไฟล์อื่น
Syntax: from ชื่อไฟล์ import ชื่อ class

"""
from overloading import Calculator

class excute(Calculator):
    def __init__(self):
        pass

aba = excute()
print(aba.add(10,20)) #เรียกใช้ method จาก class แม่ที่อยู่ไฟล์ overloading

