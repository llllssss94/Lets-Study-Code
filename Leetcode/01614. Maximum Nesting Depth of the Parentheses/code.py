from typing import *

class Solution:
    def maxDepth(self, s: str) -> int:
        stk = list()
        max_depth = 0

        for c in s:
            if c == "(":
                stk.append(c)
            elif c == ")":
                stk.pop()
            max_depth = max(max_depth, len(stk))

        return max_depth
    
if __name__ == "__main__":
    s = "(1+(2*3)+((8)/4))+1"
    print(Solution().maxDepth(s))

    s = "(1)+((2))+(((3)))"
    print(Solution().maxDepth(s))