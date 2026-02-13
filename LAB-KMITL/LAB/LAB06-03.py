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

def binary_search(data, name):
    left = 0
    right = len(data) - 1
    count = 0
    while left <= right:
        mid = (left + right) // 2
        count += 1
        if data[mid].getName() == name:
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {count}")
            return
        elif data[mid].getName() < name:
            left = mid + 1
        else:
            right = mid - 1
    print(f"{name} does not exists.")
    print(f"Comparisons times: {count}")

def main():
    import json
    std_in = json.loads(input())
    data = []
    for s in std_in:
        data.append(Student(s["id"], s["name"], s["gpa"]))
    name = input()
    binary_search(data, name)

main()