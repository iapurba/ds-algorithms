#!/usr/bin/env python3


def quick_sort(array, l, r):

    if l < r:
        partition_idx = get_partition(array, l, r)

        # Recursively call left and right subarray to the pivot
        quick_sort(array, l, partition_idx-1)
        quick_sort(array, partition_idx+1, r)

    return array


# Helper function to find the final resting position of the pivot
def get_partition(array, l, r):

    # Here we make the right most element and pivot
    piovt = array[r]

    # We rearrange the array such that
    # The elements smaller than the pivot are at left to the pivot
    # And the elements greater that the pivot are at right to the pivot
    i = l
    for j in range(i, r):
        if array[j] < piovt:
            swap(array, i , j)
            i += 1
    swap(array, i, r)

    return i


# Helper function to swap elements at two different array indices i, j
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


if __name__ == "__main__":

    nums = [2, 5, 3, 1, 6, 12, 8, 19, 10, 22, 14]

    print(quick_sort(nums, 0, len(nums)-1))
