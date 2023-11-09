def counting_sort(arr, maxVal):

    length = len(arr)

    counts = [0] * maxVal

    for i in range(0, maxVal):
        counts[arr[i]] = counts[arr[i]] + 1

    for j in range(1, maxVal):
        counts[j] = counts[j] + counts[j-1]

    for i in range(len(arr), 0):
        