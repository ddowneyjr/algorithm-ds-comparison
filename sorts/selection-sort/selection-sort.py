import random

"""
Selection Sort
"""

def selection_sort(arr):
    if len(arr) == 0:
        return "empty list"
    
    sorted_index = 0
    
    for i in range(len(arr)):
        # variable to hold the minimun value starting at index 0
        min_index = i
        # variable to hold the index
        index = min_index+1
        # looping through the array
        while index < len(arr):
            # if we find a new minimum
            if arr[index] < arr[min_index]:
                # replace the current minimum index with the current index
                min_index = index
            # increment the index
            index = index+1

        # swapping
        temp = arr[sorted_index]
        arr[sorted_index] = arr[min_index]
        arr[min_index] = temp
        
        sorted_index = sorted_index + 1
    # return the minimum    
    return arr




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



    print("selection_sort: " + str(selection_sort(array)))
  


    print("\nTesting empty list")

    array = []
    print("selection_sort: " + str(selection_sort(array)))
 