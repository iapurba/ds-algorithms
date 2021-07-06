#!/usr/bin/env python3

def selection_sort(array):

    size = len(array)

    for i in range(size):
        # select i as min index
        min_idx = i
        for j in range(i, size):
            # If the value of index j is less than the value of min_idx
            # update min_idx as j
            if array[min_idx] > array[j]:
                min_idx = j

        temp = array[i]
        array[i] = array[min_idx]
        array[min_idx] = temp

    return array


nums = [2, 5, 3, 1, 6, 12, 8, 19, 10, 22, 14]

print(selection_sort(nums))
