class car:
    """Attibute"""
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    """process"""
    def show_info(self):
        print(f"Your brand car is : {self.brand}")
        print(f"Your car is make in {self.year} year")
    def check_oldnew(self):
        check = 2025 - self.year
        if check>10:
            print("your car is old")
        else:
            print("your car is still new")

# made object
car1 = car("Lambo",2020)
#calling a method / function
car1.show_info()
car1.check_oldnew()