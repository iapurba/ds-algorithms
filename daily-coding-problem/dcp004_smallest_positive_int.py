#!/usr/bin/env python3

from typing import List


def find_smallest_missing_positive_int(array: List[int]) -> int:
    c = 0
    while (c != len(array)):
        if (array[c] > 0 and array[c] < len(array)
                and (array[c] != c+1) and array[c] != array[array[c]-1]):
            # Place current val to the index of (val-1)
            array[array[c]-1], array[c] = array[c], array[array[c]-1]
        else:
            c += 1

    for index, item in enumerate(array):
        if (index != (item-1)):
            return index + 1

    return len(array)


if __name__ == "__main__":

    nums = [4, 3, 2, -6, 5, 0, 1, 7, -1, 2, 4, -3]

    print(find_smallest_missing_positive_int(nums))
