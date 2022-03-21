from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0

        if len(strs) == 1:
            return strs[0]

        min_len = min([len(s) for s in strs])

        while i < min_len:
            is_same = True
            prefixs = [s[i] for s in strs]
            if len(set(prefixs)) != 1:
                is_same = False
                break
            if not is_same:
                break
            i += 1
        return strs[0][:i]
                

if __name__ == "__main__":
    strs = ["flower","flow","flight"]

    ret = Solution().longestCommonPrefix(strs)
    print(ret)

    strs = ["dog","racecar","car"]

    ret = Solution().longestCommonPrefix(strs)
    print(ret)
    
    strs = [""]

    ret = Solution().longestCommonPrefix(strs)
    print(ret)
