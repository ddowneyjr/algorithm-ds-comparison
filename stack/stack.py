

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
        return self.stack[len(self.stack)-1]
    
    def __str__(self):
        for value in self.stack:
            print(value)
    

if __name__ == "__main__":
    stack = Stack()

    for number in range(0, 10000):
        stack.push(number)

    # pop is very slow compared to dequeue
    while len(stack.stack) != 0:
        stack.pop()
    