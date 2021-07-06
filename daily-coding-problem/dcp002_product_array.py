#!/usr/bin/env python3

from typing import List


def product_array(array: List[int]) -> List[int]:
    product = 1
    # Assume the array does not contain any 0
    for i in array:
        product *= i

    for index, item in enumerate(array):
        # Without using division
        array[index] = int(product * pow(item, -1))

    return array


if __name__ == "__main__":
    nums = [10, 15, 3, 7]
    print(product_array(nums))
