
class Student:
    def __init__(self,id,name,gpa):
        self.std_id = id
        self.name = name
        self.gpa = gpa
    def getId(self):
        return self.std_id
    def getName(self):
        return self.name
    def getGpa(self):
        return self.gpa
    def print_details(self):
        print(f"ID: {self.getId()}")
        print(f"Name: {self.getName()}")
        print(f"GPA: {self.getGpa():.2f}")

def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())