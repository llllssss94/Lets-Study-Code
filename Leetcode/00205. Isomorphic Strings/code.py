from typing import *

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_code = dict()
        t_code = dict()

        for i in range(len(s)):
            if s[i] not in s_code:
                s_code[s[i]] = i
            
            if t[i] not in t_code:
                t_code[t[i]] = i

            if s_code[s[i]] != t_code[t[i]]:
                return False
            
        return True
    
if __name__ == "__main__":
    s = "egg"
    t = "add"

    print(Solution().isIsomorphic(s, t))

    s = "foo"
    t = "bar"

    print(Solution().isIsomorphic(s, t))