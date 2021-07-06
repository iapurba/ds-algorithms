#!/usr/bin/env python3

def insertion_sort(array):

    size = len(array)

    for step in range(1, size):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

    return array


nums = [2, 5, 3, 1, 6, 12, 8, 19, 10, 22, 14]

print(insertion_sort(nums))
