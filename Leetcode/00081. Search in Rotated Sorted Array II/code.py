from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return True
            
            # m부터 r까지 순증가
            if nums[m] < nums[r]:
                # right에 있는 경우
                if nums[m] < target <= nums[r]:
                    # m과 r 사이에 있으면 그 사이를 탐색
                    l = m + 1
                else:
                    # 사이에 없으면 최소 nums[m]보다 target이 작으므로 그 아래를 택함
                    r = m - 1
            elif nums[m] > nums[r]:
                # 중간에 rotate 지점 있는 경우
                if nums[l] <= target < nums[m]:
                    # l과 m 사이에 존재하면 그 사이를 탐색
                    r = m - 1
                else:
                    # 아니면 최소 l과 m사이는 아니므로 m부터 r사이를 탐색
                    # 왜냐면 m 이후에 nums[m] 보다 작은 값이 있는데
                    # nums[l] 보다 크지 않기 때문
                    l = m + 1
            else:
                # 같은 수가 연이어 있는 경우임
                # m을 구하며 이진 탐색하는게 빠르므로 while 따로 안함
                # 다른 수가 나올때까지 하나씩 탐색하다가
                # 만약 l과 r이 만날때까지 같은 수라면 target이 없는 것임
                r -= 1
        
        return False

        
    def search_badsol(self, nums: List[int], target: int) -> bool:
        answer = self.recurse((len(nums) - 1) // 2, sorted(nums), target)
        
        return answer

    def recurse(self, m, nums, target):
        if not nums:
            return False
        
        if nums[m] == target:
            return True

        if len(nums) <= 1:
            return False
        
        if nums[m] < target:
            return self.recurse((len(nums[m:]) - 1 ) // 2, nums[m+1:], target)
        else:
            return self.recurse((len(nums[:m]) - 1 ) // 2, nums[:m], target)


if __name__ == "__main__":
    nums = [2,5,6,0,0,1,2]
    target = 0

    ret = Solution().search(nums, target)
    print(ret)

    
    nums = [2,5,6,0,0,1,2]
    target = 3

    ret = Solution().search(nums, target)
    print(ret)

    
    
    nums = [1,0,1,1,1]
    target = 0

    ret = Solution().search(nums, target)
    print(ret)

    
    
    nums = [2,2,2,3,2,2,2]
    target = 3

    ret = Solution().search(nums, target)
    print(ret)



    
    nums = [1, 1]
    target = 0

    ret = Solution().search(nums, target)
    print(ret)

