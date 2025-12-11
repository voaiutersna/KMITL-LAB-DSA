# Encapsulation: ใช้ __ เพื่อปกป้องข้อมูลจากการเข้าถึงโดยตรง
#Conceptหลักของการใช้งานแบบPrivateคือ ถ้าหากจะมีการใช้งานหรือเปลี่ยนค่าต้องมีการใช้ฟั่งชั่นที่มาจากในclass only อย่าง getter setter แล้วเรียกใช้ภายนอกได้
class Employee:
    def __init__(self, name, salary, department):
        # Private attributes (name mangling: _Employee__name)
        self.__name = name
        self.__salary = salary
        self.__department = department
        self.__showdata()  # ✔️ เรียก private method ภายใน class ได้ 

    # Private method
    def __showdata(self):
        print("=== Employee Info ===")
        print(f"Name: {self.__name}")
        print(f"Salary: {self.__salary}")
        print(f"Department: {self.__department}")

    # Public getter (สำหรับเข้าถึงข้อมูลภายนอก)
    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_department(self):
        return self.__department

    # Public setter (ควบคุมการเปลี่ยนค่า)
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")


# ====== ทดสอบการใช้งาน ======
obj1 = Employee("Kong", 20000, "dev")

# ❌ ไม่สามารถเข้าถึง private method ได้จากภายนอก
try:
    obj1.__showdata()
except AttributeError:
    print("❌ Cannot access __showdata() from outside")

# ❌ ไม่สามารถเข้าถึง attribute ได้โดยตรง
obj1.__name = "WHIS"  # สร้าง attribute ใหม่ ไม่ได้เปลี่ยนของจริง
print(obj1.__name)    # WHIS

# ✅ ใช้ public getter เข้าถึงข้อมูลจริง
print(obj1.get_name())       # Kong
print(obj1.get_salary())     # 20000

# ✅ ใช้ public setter เปลี่ยนค่า
obj1.set_salary(50000)
print(obj1.get_salary())     # 50000

# ⚠️ Name mangling (ไม่แนะนำ แต่ทำได้)
print(obj1._Employee__name)  # Kong
