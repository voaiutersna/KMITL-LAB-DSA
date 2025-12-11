class bank:
    def __init__(self,user,password,balance):
        self.username = user
        self.password = password
        self.balance = balance
        
    # Process
    def showinfo(self):
        print(f"Your account username is {self.username}")
        print(f"Your account password is {self.password}")
        print(f"Your current balance is {self.balance}")
        print("---------------------------")

    def login(self,inputuser,inputpass):
        if inputuser == self.username and inputpass == self.password:
            print("You have sucessful login")
        else:
            print("incorrect username or password")
    def deposite(self,amount):
        if amount  >= 0:
            self.balance += amount
            print(f"You have deposite {amount}")
            print(f"Your current balance is {self.balance}")
        else:
            print("Enter positive number")
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"You have withdraw {amount}")
            print(f"Your current balance is {self.balance}")
        else:
            print("Your balance is not enough to withdraw")

    def transfer(self,reciver,amount): # เราส่งข้อมูลตัวอื่นมาเก็บใน reciver
        if amount < self.balance and amount >= 0:
            pass
        else:
            print("You not have enough money to transfer")
            return
        self.balance -= amount
        reciver.balance += amount # reciver ก็จะเป็น attribute ของตัวที่ส่งมาจาก parameter 
        print(f"You have {amount} transfer to {reciver.username} ")
        print(f"You current balance is {self.balance}")
        print(f"The reciver balance is {reciver.balance}")

customer1 = bank("user12345",12345678,10000)
customer2 = bank("user55555",123123,20000)
customer1.login("user12345",12345678)

#tranfer
customer1.transfer(customer2,500)
