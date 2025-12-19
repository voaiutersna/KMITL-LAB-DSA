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
    
def Group(stack):
    s1 = ArrayStack()
    s2 = ArrayStack()
    for i in range(len(stack.data)):
        if not i % 2:
            s1.push(stack.data[i])
        else:
            s2.push(stack.data[i])
    return s1,s2

def main():
    stack = ArrayStack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    stack.push("d")
    stack.push("e")
    s1,s2 = Group(stack)
    s1.print_stack()
    s2.print_stack()
main()
