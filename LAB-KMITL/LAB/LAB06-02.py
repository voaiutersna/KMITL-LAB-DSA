
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

class ProbHash:
    def __init__(self, size):
        self.hash_table = [None] * size
        self.size = size

    def hash(self, key):
        return key % self.size

    def rehash(self, hkey):
        return (hkey + 1) % self.size

    def insert_data(self, student):
        key = student.getId()
        index = self.hash(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = student
            print(f"Insert {key} at index {index}")
        else:
            new_index = self.rehash(index)
            while new_index != index:
                if self.hash_table[new_index] is None:
                    self.hash_table[new_index] = student
                    print(f"Insert {key} at index {new_index}")
                    return
                new_index = self.rehash(new_index)
            print(f"The list is full. {key} could not be inserted.")

    def search_data(self, std_id):
        index = self.hash(std_id)
        if self.hash_table[index] is not None and self.hash_table[index].getId() == std_id:
            print(f"Found {std_id} at index {index}")
            return self.hash_table[index]
        else:
            new_index = self.rehash(index)
            while new_index != index:
                if self.hash_table[new_index] is None:
                    break
                if self.hash_table[new_index].getId() == std_id:
                    print(f"Found {std_id} at index {new_index}")
                    return self.hash_table[new_index]
                new_index = self.rehash(new_index)
            print(f"{std_id} does not exist.")
            return None

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()