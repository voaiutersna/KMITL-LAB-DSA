"""
Encapsulation คือการซ่อนรายละเอียดภายในของวัตถุ (object) ไม่ให้ถูกเข้าถึงโดยตรงจากภายนอก แต่ให้เข้าถึงผ่านฟังก์ชันหรือเมธอดที่กำหนดไว้เท่านั้น

ทำให้ข้อมูลภายในวัตถุปลอดภัย ป้องกันการถูกแก้ไขหรือใช้ผิดวิธี

ช่วยควบคุมและจัดการข้อมูลให้เหมาะสม

ใน Python จะใช้การกำหนดตัวแปรหรือเมธอดเป็น private หรือ protected เพื่อซ่อนข้อมูลเหล่านั้น

"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner              # public attribute
        self.__balance = balance        # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} to {self.owner}'s account")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount} from {self.owner}'s account")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

    # Protected method (ใช้ underscore เดียว)
    def _internal_method(self):
        print("This is a protected internal method")

# สร้าง object
account = BankAccount("Alice", 1000)

# เข้าถึงข้อมูล public
print(account.owner)  # Alice

# เข้าถึงข้อมูล private โดยตรงจะ error
# print(account.__balance)  # AttributeError
#__balance สร้างเป็นแบบ private เรียกใช้งานโดยตรงไม่ได้ต้องผ่าน method ใน class

# ใช้เมธอด public เพื่อเข้าถึงข้อมูล private
print(account.get_balance())  # 1000

# ฝากเงิน ถอนเงิน
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # 1300

# ใช้ method protected (โดย convention ไม่แนะนำให้เรียกจากภายนอก)
account._internal_method()

"""
การซ่อนข้อมูลใน Python (Syntax & Structure)
ระดับการเข้าถึง	Prefix ตัวแปร/เมธอด	ความหมาย / การเข้าถึง
Public	ไม่มี	เข้าถึงได้ทั้งภายในและภายนอกคลาส
Protected	_ (underscore เดียว)	เข้าถึงได้แค่ในคลาสและ subclass แต่ก็ยังเข้าถึงได้จากภายนอก (เป็นแค่ convention) ก็เหมือนกับ Publicแหละ
Private	__ (double underscore)	Python จะทำ name mangling (เปลี่ยนชื่อภายใน) เพื่อป้องกันการเข้าถึงโดยตรงจากภายนอกคลาส

"""