from typing import *

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ret = 0

        max_num = max(nums)
        l = 0
        ccnt = 0
        for r in range(len(nums)):
            if nums[r] == max_num:
                ccnt += 1

            # 이미 k개 이상이라면 갯수를 센다.
            while ccnt >= k:
                if nums[l] == max_num:
                    ccnt -= 1

                l += 1
            
            # l, r 서브 스트링이 을 포함하는 모든 경우는 l 앞쪽 갯수와 같다.
            ret += l

        return ret


if __name__ == "__main__":
    nums = [1,3,2,3,3]
    k = 2
    print(
        Solution().countSubarrays(nums, k)
    )