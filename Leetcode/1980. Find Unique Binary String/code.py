from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return self.recurse(nums, '')

    # DFS
    def recurse(self, nums, cur):
        # 만약 없는 친구 나오면 그 친구 return
        if len(nums[0]) == len(cur):
            if cur in nums:
                return None
            else:
                return cur

        # 1 붙여서 
        one = self.recurse(nums, cur+'1')
        if one is not None:
            return one

        # 1에서 먼저 없는 애 나오면 0 쪽은 탐색 안함
        # 0부터 해도 됨, 문제 예시에서 11을 return하길래 1부터 함
        # Backtracking

        # 0 붙여서
        zero = self.recurse(nums, cur+'0')
        if zero is not None:
            return zero
        
        return None
        
if __name__ == '__main__':
    nums = ["01","10"]

    ret = Solution().findDifferentBinaryString(nums)
    print(ret)

    
    nums = ["00","01"]

    ret = Solution().findDifferentBinaryString(nums)
    print(ret)


    
    nums = ["111","011","001"]

    ret = Solution().findDifferentBinaryString(nums)
    print(ret)