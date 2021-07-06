#!/usr/bin/env python3

def merge_sort(array):
    size = len(array)

    if size <= 1:
        return array

    mid = size // 2
    # Spilt the array into two subarrays from midway
    L = array[:mid]
    R = array[mid:]

    # Recursively sort both spited subarrays and merge them
    return merge(merge_sort(L), merge_sort(R))


# Helper function to merge two sorted arrays
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]


if __name__ == "__main__":

    nums = [2, 5, 3, 1, 6, 12, 8, 19, 10, 22, 14]

    print(merge_sort(nums))
