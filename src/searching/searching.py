def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search1(arr, target, l, h):
    if h>= low:
            pivot = (h + l) // 2
            if arr[pivot] == target:
                return pivot
            elif arr[pivot] > target:
                return binary_serach(arr, l, pivot -1, target)
            else:
                return binary_search(arr, pivot + 1, h, target)
    else:
        return -1  # not found

def binary_search(arr, target):
    l = 0
    h = len(arr) - 1
    pivot = 0

    while l <= h:
        pivot = (h+l) // 2
        if arr[pivot] < target:
            l = pivot + 1
        elif arr[pivot] > target:
            h = pivot - 1
        else:
            return pivot
    return -1