from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        nums[:] = sorted(list(set(nums)))

        return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 2]

    ret = Solution().removeDuplicates(nums)
    print(ret)