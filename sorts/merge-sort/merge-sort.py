import random

def merge(left, right):
    result = [None] * (len(left) + len(right))
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result[k] = left[i]
            i += 1

        else: 
            result[k] = right[j]
            j += 1

        k += 1
    
    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1
    

    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1

    return result



def merge_sort_iter(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    left = arr[:(n//2)]
    right = arr[(n//2):]
    

    insertion_sort(left)
    insertion_sort(right)

    result = merge(left, right)

    return result


def merge_sort_recur(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        left = arr[:(n//2)]
        right = arr[(n//2):]
        if left:
            left = merge_sort_recur(left)
        if right:
            right = merge_sort_recur(right)

        result = merge(left, right)

        return result


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

    

    print("merge_sort_iter: " + str(merge_sort_iter(array)))

    array = genRandArray(arrayLen)
    print("array: " + str(array))

    

    print("merge_sort_recur: " + str(merge_sort_recur(array)))
  
    