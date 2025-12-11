"""Syntax ของการใช้ name mangling เพื่อเข้าถึง private attribute หรือ private method ของ superclass: """
class Parent:
    def __init__(self):
        self.__secret = "this is private"

    def __hidden_method(self):
        return "this is a hidden method"

class Child(Parent):
    def reveal(self):
        #Syntax:   _classแม่__private method/attribute

        # 🔓 Access private attribute using name mangling
        print(self._Parent__secret)

        # 🔓 Access private method using name mangling
        print(self._Parent__hidden_method())
# ใช้งาน
c = Child()
c.reveal()
