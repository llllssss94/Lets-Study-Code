from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = self.recurse(nums, 0, target)
        
        return answer

    def recurse(self, nums, idx, target):
        # 현재 리스트, 리스트의 원본 시작 인덱스, 찾고자 하는 수
        if len(nums) == 1:
            if nums[0] == target:
                return idx
            else:
                return -1

        l = len(nums) // 2

        left = nums[:l]
        right = nums[l:]

        if right[0] <= target:
            return self.recurse(right, idx + l, target)
        else:
            return self.recurse(left, idx, target)


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9

    ret = Solution().search(nums, target)
    print(ret)

    
    nums = [-1,0,3,5,9,12]
    target = 2

    ret = Solution().search(nums, target)
    print(ret)
    
    
    nums = [5]
    target = -5

    ret = Solution().search(nums, target)
    print(ret)

    
    
    nums = [5]
    target = 5

    ret = Solution().search(nums, target)
    print(ret)