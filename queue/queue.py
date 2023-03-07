

class Queue:
    def __init__(self) :
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return_val = None
        if len(self.queue) > 0:
            return_val = self.queue.remove(self.queue[0])
            
        return return_val

    def peek(self):
        return self.queue[0]
    
    def __str__(self):
        for value in self.queue:
            print(value)
    

if __name__ == "__main__":
    queue = Queue()
    for number in range(0, 10000):
        queue.enqueue(number)

    while len(queue.queue) != 0:
        queue.dequeue()

    #queue.__str__()