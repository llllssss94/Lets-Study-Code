from tkinter import E
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        # Init
        answer = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while r > l:
                s = nums[i] + nums[r] + nums[l]
                
                if s == target:
                    return s

                # 더 짧은 경우
                if abs(target - s) < abs(answer - target):
                    answer = s
                

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    # 딱 맞음
                    return answer
                
        return answer


if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1

    ret = Solution().threeSumClosest(nums, target)
    print(ret)

    
    nums = [0, 1, 2]
    target = 3

    ret = Solution().threeSumClosest(nums, target)
    print(ret)

    
    nums = [0, 0, 0]
    target = 1

    ret = Solution().threeSumClosest(nums, target)
    print(ret)


    nums = [1,1,1,0]
    target = -100
    
    ret = Solution().threeSumClosest(nums, target)
    print(ret)


    nums = [0,2,1,-3]
    target = 1
    
    ret = Solution().threeSumClosest(nums, target)
    print(ret)


    nums = [1,1,-1,-1,3]
    target = -1
    
    ret = Solution().threeSumClosest(nums, target)
    print(ret)