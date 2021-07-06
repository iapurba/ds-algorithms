#!/usr/bin/env python3

from typing import List


def two_sum(array: List[int], targer: int) -> bool:
    if not array:
        return False

    seen = set()

    for item in array:
        if item in seen:
            return True
        else:
            # Add second number (target - current) with is needed
            # against the current number to add up to the target
            seen.add(targer-item)

    return False


if __name__ == "__main__":
    nums = [10, 15, 3, 7]

    print(two_sum(nums, 17))
    print(two_sum(nums, 19))
