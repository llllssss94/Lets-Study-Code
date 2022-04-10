from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for n in nums:
            if n != val:
                nums[i] = n
                i += 1
        
        return i
        

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3

    ret = Solution().removeElement(nums, val)
    print(ret)


    
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    ret = Solution().removeElement(nums, val)
    print(ret)

    
    nums = [2]
    val = 3

    ret = Solution().removeElement(nums, val)
    print(ret)

    
    nums = [4, 5]
    val = 4

    ret = Solution().removeElement(nums, val)
    print(ret)