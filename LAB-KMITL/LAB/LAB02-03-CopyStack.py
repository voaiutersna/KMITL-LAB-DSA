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
    
def copy_stack(s1,s2):
    while not s2.is_empty():
        s2.pop()
    for i in s1.data:
        s2.push(i)

def main():
    s1 = ArrayStack()
    s2 = ArrayStack()
    s1.push(10)
    s1.push(20)
    s1.push(30)
    s2.push(15)
    s2.push(25)

    copy_stack(s1,s2)

    s1.print_stack()
    s2.print_stack()
main()
