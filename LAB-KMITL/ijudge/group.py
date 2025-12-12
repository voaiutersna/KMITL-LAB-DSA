class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []
    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.isdigit(".","",1):
                input_data = float(input_data)
        except(TypeError, ValueError, ArithmeticError, AttributeError):
            return None
        finally:
            self.data.append(input_data)
            self.size += 1
    def is_empty(self):
        if not self.size:
            return True
        return False
    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()
    def get_stack_top(self):
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self.data[-1]
    def get_size(self):
        return self.size
    def print_stack(self):
        print(self.data)
    
def Group(group,stack):
    list_group = []
    for i in range(group):
        list_group.append(list())
    # print(list_group)
    amount_group = len(list_group)-1
    index = 0
    while not stack.is_empty():
        if index == amount_group:
            list_group[index].append(stack.pop())
            index = 0
        else:
            list_group[index].append(stack.pop())
            index += 1
    num = 0
    for i in list_group:
        num += 1
        output = ""
        for j in range(len(i)):
            output += i[j]
            if j != len(i)-1:
                output += ", "
        print(f"Group {num}: {output}")
            
def main():
    group = int(input())
    person = int(input())
    stack = ArrayStack()
    for _ in range(person):
        inp = input()
        stack.push(inp)
    Group(group,stack)
main()
