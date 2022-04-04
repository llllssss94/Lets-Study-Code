from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        


if __name__ == "__main__":
    s = ["h","e","l","l","o"]

    sln = Solution()
    ret = sln.reverseString(s)