# สร้าง class
class class_name:

#กำหนด attribute โดยใช้ __init__
    def __init__(self,data1,data2):
        self.variable1 = data1
        self.variable2 = data2

#กำหนด behavior ก็สร้าง function ทั่วไปเลย
    def func_name(self,argument1,argument2,argument3):
        #statement processต่างๆ
        pass

#การใช้งาน 
#1.สร้างobjectมา (กำหนดattribute)
"""variable = class_name(argument1,argument2)"""
emp1 = class_name("datauser","datapass") 

#2.การเอาไปใช้ หรือเรียกใช้งานฟังชั่น
"""variable.func_name(argument1,argument2,argument3)"""
emp1.func_name(x,y,z)