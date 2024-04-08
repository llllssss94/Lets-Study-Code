from typing import *

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

pick = 0
def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        r = n
        l = 0

        if guess(n) == 0:
            return n
        while r > l:
            # Binary Search
            g_num = (r+l) // 2
            ret = guess(g_num)
            if ret == 1:
                l = g_num
            elif ret == -1:
                r = g_num
            else:
                return g_num
        return n


if __name__ == "__main__":
    n = 10
    pick = 6
    print(Solution().guessNumber(n))

    n = 1
    pick = 1
    print(Solution().guessNumber(n))

    n = 2
    pick = 1
    print(Solution().guessNumber(n))