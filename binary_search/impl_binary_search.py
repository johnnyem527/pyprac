def binary_search(arr, ele):

    first = 0
    last = len(arr) - 1

    found = False

    while first <= last and not found:

        mid = int((first + last)/2)

        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found

arr = [1, 23, 63, 112, 233, 999]
print(binary_search(arr, 999))


def rec_binary_search(arr, ele):
    # base case
    if len(arr) == 0:
        return False

    else:
        mid = int(len(arr)/2)

        if arr[mid] == ele:
            return True

        else:
            if ele < arr[mid]:
                return rec_binary_search(arr[:mid], ele)
            else:
                return rec_binary_search(arr[mid+1:], ele)

print(rec_binary_search(arr, 23))