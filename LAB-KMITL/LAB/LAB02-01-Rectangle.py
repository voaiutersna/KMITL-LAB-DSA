class Rectangle:
    def __init__(self,height,wide):
        self.height = float(height)
        self.wide = float(wide)
    def calculate_area(self):
        return self.wide * self.height
    def calculate_perimeter(self):
        return (self.wide * 2) + (self.height * 2)

def main():
    height = float(input())
    wide = float(input())
    obj = Rectangle(height,wide)
    condition = input()
    result = None
    if condition == "area":
        result = obj.calculate_area()
    elif condition == "perimeter":
        result = obj.calculate_perimeter()
    print(f"{result:.2f}")
main()
