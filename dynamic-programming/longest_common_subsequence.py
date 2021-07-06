#!/usr/bin/env python3

# Implementation of dynamic programming to find out longest common subsequence

def longest_common_subsequence(s1: str, s2: str) -> int:
    '''
    * create a dp table to cache the result of orginal subporblems.
    *
    * s2 will be on the rows, s1 will be on the columns.
    *
    * +1 to leave a room at left for "" (empyt string).
    '''

    cache = [[0 for i in range(len(s1) + 1)] for i in range(len(s2) + 1)]

    '''
    * cache[s2.length()][s1.lenth()] is our orginal subproblem. Each entry in 
    * the table is taking a substring operation against whatever string is on 
    * the rows or colums.
    *
    * It goes from index 0 to index s2Row/s1Col (exclusive).
    '''

    for s2_row in range(len(s2) + 1):
        for s1_col in range(len(s1) + 1):

            if (s2_row == 0 or s1_col == 0):
                cache[s2_row][s1_col] = 0

            elif s2[s2_row-1] == s1[s1_col-1]:
                cache[s2_row][s1_col] = cache[s2_row - 1][s1_col-1] + 1

            else:
                cache[s2_row][s1_col] = max(
                    cache[s2_row][s1_col-1], cache[s2_row-1][s1_col])

    return cache[s2_row][s1_col]


if __name__ == "__main__":

    print(longest_common_subsequence("", "azb"))  # returns 0
    print(longest_common_subsequence("aab", "azb"))  # returns 2
    print(longest_common_subsequence("aggtab", "gxtxayb"))  # returns 4
