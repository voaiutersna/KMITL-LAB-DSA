"""super() ใน Python (โดยเฉพาะใน OOP - Object-Oriented Programming) 
ใช้เพื่อเรียก method หรือ constructor ของ คลาสแม่ (superclass)
 โดยเฉพาะเมื่อเราทำการสืบทอด (inheritance) คลาสลูกจากคลาสแม่"""

"""
ประโยชน์ของ super()
เรียก constructor ของคลาสแม่ (__init__)

เรียก method ของคลาสแม่ที่ถูก override

สนับสนุนการทำ multiple inheritance ได้ดี

ช่วยลดการเขียนโค้ดซ้ำ

"""

"""super().method_name(arguments)"""

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # เรียก method จาก Animal
        print("Dog barks")

dog = Dog()
dog.speak()
# Output:
# Animal speaks
# Dog barks
