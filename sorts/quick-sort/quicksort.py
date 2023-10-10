import random

def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)
        

def partition(arr, start, end):
    pivot = arr[end]
    lhs = start-1
    for i in range(start, end):
        print(arr)
        if arr[i] <= pivot:
            lhs = lhs + 1
            temp = arr[lhs]
            arr[lhs] = arr[i]
            arr[i] = temp
    temp = arr[lhs + 1]
    arr[lhs + 1] = arr[end]
    arr[end] = temp
    return lhs + 1



# generate an array with random values
def genRandArray(length):
    num_range = range(100)
    amount = length
    return [random.choice(num_range) for _ in range(amount)]


if __name__ == "__main__":
    

    arrayLen = int(input("How many values in the array? "))
    print("Testing list with values")
    array = genRandArray(arrayLen)
    print("array: " + str(array))

    
    quicksort(array, 0, len(array)-1)
    print("quicksort: " + str(array))

   
  
    
