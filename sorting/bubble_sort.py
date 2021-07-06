#!/usr/bin/env python3

def bubble_sort(array):
    length = len(array)

    for i in range(length):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return array


nums = [2, 5, 3, 1, 6, 12, 8, 19, 10, 22, 14]

print(bubble_sort(nums))
