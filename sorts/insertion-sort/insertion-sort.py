import random

def insertion_sort(arr):
    length = len(arr)

    for i in range (1, length):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j-1
        arr[j+1] = key

def insertion_sort_reverse(arr):
    length = len(arr)

    for i in range (1, length):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j = j-1
        arr[j+1] = key


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

    insertion_sort(array)

    print("insertion_sort: " + str(array))

    array = genRandArray(arrayLen)
    print("array: " + str(array))
    
    insertion_sort_reverse(array)
    print("insertion_sort_reverse: " + str(array))
  


    