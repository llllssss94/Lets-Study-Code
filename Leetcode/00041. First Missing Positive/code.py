from typing import *

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        if max_num < 1:
            return 1

        if min_num < 1:
            min_num = 1

        num_dict = dict()

        for num in nums:
            num_dict[str(num)] = True

        missing = -1
        for i in range(min_num, max_num+1):
            if str(i) not in num_dict:
                missing = i
                break

        if min_num > 1:
            return 1
        else:
            if missing < 1:
                return max_num+1
            else:
                return missing
            
