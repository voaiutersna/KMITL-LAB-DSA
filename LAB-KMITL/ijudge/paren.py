class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []
    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".","",1).isdigit():
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
def  is_parentheses_matching():
    x = input()
    s1 = ArrayStack()
    for i in x:
        if i == "(":
            s1.push(i)
            continue
        if i == ")":
            open_bucket = s1.pop()
    if s1.is_empty():
        print(f"Parentheses in {x} are matched")
        print("True")
        return
    print(f"Parentheses in {x} are unmatched")
    print("False")
is_parentheses_matching()
