class HeapData:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.index = None
        # self.left_object = None
        # self.right_object = None

class Heap:
    def __init__(self):
        self.array = [None]

    def insert(self, element):

        # If the Priority Queue is Empty
        if self.array[0] == None:
            self.array[0] = element
            element.index = 0

        # If the Priority Queue is not Empty
        elif self.array[0] is not None:
            self.array.append(element)
            element.index = len(self.array)-1


        # Call heapify to make sure everything is in the proper place
        sorted = False
        index = element.index

        while sorted is not True:
            parent = self.array[self.findParent(index)]
            temp_parent_index = parent.index
            if self.array[index].key < parent.key:

                self.swap(index, parent.index)
                index = temp_parent_index

            else:
                sorted = True




    def swap(self, index_one, index_two):
        temp = self.array[index_one]
        self.array[index_one] = self.array[index_two]
        self.array[index_two] = temp
        self.array[index_two].index = index_two
        self.array[index_one].index = index_one


    def extractMin(self):
        # Swapping the root with the last object in the Heap
        if self.array[0] is not None:
            self.swap(0, len(self.array)-1)


        # Call heapify to make sure everything is in proper place

        return_min = self.array[len(self.array)-1]
        sorted = False
        index = return_min.index

        while sorted is not True:
            parent = self.array[self.findParent(index)]
            temp_parent_index = parent.index
            if self.array[index].key < parent.key:

                self.swap(index, parent.index)
                index = temp_parent_index

            else:
                sorted = True
        self.array.remove(self.array[len(self.array)-1])

        return return_min


    def heapify(self, index):
        # Function to balance the heap

        # Recursively check elements in the heap[
        # Start at the last object in the heap as that is the only thing that can be out of balance
        # Check if it is greater than its parent
        # If so swap and recursively check that node and the parent
        # If not then the heap is balanced

        if self.findLeft(index) < len(self.array) and self.array[self.findLeft(index)].key < self.array[index].key:
            smallest = self.findLeft(index)
        else:
            smallest = index

        if self.findRight(index) < len(self.array) and self.array[self.findRight(index)].key < self.array[index].key:
            smallest = self.findRight(index)

        if smallest is not index:
            self.swap(index, smallest)
            self.heapify(smallest)






    def decreaseKey(self, index, new_key):
        if new_key < self.array[index].key:
            self.array[index].key = new_key

        sorted = False
        index = self.array[index].index

        while sorted is not True:
            parent = self.array[self.findParent(index)]
            temp_parent_index = parent.index
            if self.array[index].key < parent.key:

                self.swap(index, parent.index)
                index = temp_parent_index

            else:
                sorted = True



    def findLeft(self, index):
        return int((2 * (index + 1)) - 1)

    def findRight(self, index):
        return int(2 * (index + 1))

    def findParent(self, index):
        return int((index-1) / 2)

    def __str__(self):
        result = ''

        if self.array[0] is not None:
            for object in self.array:
                result += str(object.key) + ' '

        return result

if __name__ == '__main__':
    myHeap = Heap()
    node1 = HeapData(10, 2)
    node2 = HeapData(11, 10)
    node3 = HeapData(12, 25)
    node4 = HeapData(13, 1)
    node5 = HeapData(14, 11)
    node6 = HeapData(15, 20)

    myHeap.insert(node1)
    myHeap.insert(node2)
    myHeap.insert(node3)
    myHeap.insert(node4)
    myHeap.insert(node5)
    myHeap.insert(node6)
    print(str(myHeap))

    myHeap.extractMin()
    print(str(myHeap))

    myHeap.decreaseKey(2, 10)
    print(str(myHeap))








