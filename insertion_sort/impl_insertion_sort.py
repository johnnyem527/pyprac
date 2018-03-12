def insertion_sort(arr):

    for i in range(1, len(arr)):

        currentVal = arr[i]
        position = i

        while position > 0 and arr[position - 1] > currentVal:
            arr[position] = arr[position-1]
            position = position - 1

        arr[position] = currentVal

    return arr

arr = [1, 23, 12, 2, 13, 123, 4]
print(insertion_sort(arr))