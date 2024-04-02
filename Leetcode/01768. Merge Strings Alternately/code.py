from typing import *

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        ret = ""

        i = 0
        while i < max(l1, l2):
            if i < l1:
                ret += word1[i]
            
            if i < l2:
                ret += word2[i]
            
            i += 1

        return ret
    

if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    print(Solution().mergeAlternately(word1, word2))

    word1 = "ab"
    word2 = "pqrs"
    print(Solution().mergeAlternately(word1, word2))

    word1 = "abcd"
    word2 = "pq"
    print(Solution().mergeAlternately(word1, word2))