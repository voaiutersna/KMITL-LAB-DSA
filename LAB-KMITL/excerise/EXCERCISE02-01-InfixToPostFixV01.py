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
    
def infixToPostfix(expression):
    stack = ArrayStack()
    operation = ["*","/","+","-"]
    high_oper = ["*","/"]
    low_oper = ["+","-"]
    postfix = ""
    for i in expression:
        #print(i)
        if i in operation:
            if i == "*" or i =="/":
                if stack.is_empty():
                    stack.push(i)
                else: 
                    while not stack.is_empty():
                        top = stack.get_stack_top() 
                        # print("top working",top) 
                        if top in high_oper:
                            pop_oper = stack.pop() 
                            postfix += pop_oper 
                        else:
                            break
                    stack.push(i)
            else:
                if stack.is_empty():
                    stack.push(i)
                else:
                    while not stack.is_empty():
                        pop_item = stack.pop()
                        postfix += pop_item
                    stack.push(i)
        else:
            postfix += i
    for i in range(len(stack.data)-1,-1,-1):
        postfix += stack.data[i]
    return postfix

def main():
    inp = input()
    result = infixToPostfix(inp.replace(" ",""))
    print(result)
main()
