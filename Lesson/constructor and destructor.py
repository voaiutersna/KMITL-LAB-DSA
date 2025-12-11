""" 
Constructor is method ที่จะถูกใช้งานตอนเริ่มสร้างวัตถุ (ทันทีที่มีการสร้าง object __init__ จะทำงานทันที)
ใช้สำหรับ สร้างวัตถุ (Object) จากคลาส
"""
class Person:
    def __init__(self, name, age):
        self.name = name  # กำหนดค่า attribute
        self.age = age
"""
ไม่นิยมใช้เลย
Destructor is method ที่จะถูกใช้งานตอนสิ้นสุดการทำงานของclass กรณีถ้ากำหนดมันขึ้นมาน่ะ
ใช้สำหรับ ทำลายหรือคืนค่าทรัพยากร เมื่อ object ไม่ถูกใช้งานอีกแล้ว (หมดอายุการใช้งาน)
"""
def __del__(self):
        print(f"{self.name} ถูกลบแล้ว")