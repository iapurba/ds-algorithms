#!/usr/bin/env python3

def binarySearch(array, target):

    if not array: return False

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        found = array[mid]

        if found == target:
            return True
        elif found > target:
            right = mid - 1
        else:
            left = mid + 1

    return False


if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    print(binarySearch(nums, 3)) # return True
    print(binarySearch(nums, 12)) # return False
