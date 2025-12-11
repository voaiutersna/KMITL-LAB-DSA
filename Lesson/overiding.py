"""
Method Overriding 
นิยาม:การเขียนเมธอดใน คลาสลูก (subclass) ที่มีชื่อเดียวกันกับเมธอดใน คลาสแม่ (superclass) 
เพื่อให้การทำงานแตกต่างกัน
"""
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
a.speak()  # Animal speaks

d = Dog()
d.speak()  
"""ถ้าclassลูกมี method ที่ชื่อเหมือน classแม่ มันจะใช้งานmethodของclassตัวมันเองก่อน
กรณีที่สร้าง object ในclassลูกนะ แต่ถ้าไม่มีmethodที่ชื่อเหมือนกันในclassแม่ มันก็จะไปใช้methodของclassแม่"""
