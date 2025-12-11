"""
Method Overloading 
นิยาม:การสร้างเมธอดชื่อเดียวกันในคลาสเดียวกัน แต่มี ** พารามิเตอร์ต่างกัน **
"""
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()