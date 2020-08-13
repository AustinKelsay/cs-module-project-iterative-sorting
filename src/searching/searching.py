def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # 1 Compare the target element to the midpoint
    # 2 Determine which half to go in, toss th other half out
    # 3 If the midpoint matches our target, return the midpoint
    # 4 Repeat this process
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            high = mid - 1
        if target > arr[mid]:
            low = mid + 1

    return -1  # not found
