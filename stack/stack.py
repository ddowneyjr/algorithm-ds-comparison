

class Stack:
    def __init__(self) :
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return_val = None
        if len(self.stack) > 0:
            return_val = self.stack.remove(self.stack[len(self.stack)-1])
            
        return return_val

    def peek(self):
        return self.stack[0]
    
    def __str__(self):
        for value in self.stack:
            print(value)
    

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.__str__()
    print(stack.pop())
    print(stack.peek())