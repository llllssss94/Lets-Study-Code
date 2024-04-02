from typing import *

class Solution:
    def moveZeroes_BP(self, nums: List[int]) -> None:
        l = 0

        for r in range(len(nums)):
            # r 포인터를 0이 아닌 수까지 진행
            # 그동안 l은 고정

            # r 이 0이 아닌 수를 찾으면 l 과 스위칭 후 기존 l 자리는 완료이므로 l 포인터 한칸 전진
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        return nums

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return nums
        
        r = 0
        l = 0
        while True:
            # 첫 0 지점
            while nums[l] != 0 and l < len(nums) - 1:
                l += 1

            # 0이 없는 경우
            if l == len(nums) - 1:
                break

            # 0 이후 처음 나온 0이 아닌 수와 swap
            r = l
            while r < len(nums):
                if nums[r] == 0:
                    r += 1
                else:
                    break
            
            # 끝까지 다 본 경우
            if r >= len(nums):
                break

            nums[l], nums[r] = nums[r], nums[l]

    

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print(Solution().moveZeroes_BP(nums))

    nums = [0]
    print(Solution().moveZeroes_BP(nums))

    nums = [0,0,1]
    print(Solution().moveZeroes_BP(nums))

    nums = [2,1]
    print(Solution().moveZeroes_BP(nums))