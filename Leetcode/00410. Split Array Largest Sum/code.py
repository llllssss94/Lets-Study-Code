
from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Parametric Search
        # Search space가 index가 아니라 sum 값임
        # max랑 sum 사이 어딘가에서 결정될 것임
        l, r = max(nums), sum(nums)

        # sum과 max 가 같으면 바로 return 임
        # 찾다보면 같아짐
        while l < r:
            # 대강 잡은 중간 값
            mid = (l+r)//2

            # left의 합, 쪼개진 수
            s, cnt = 0, 1

            # mid 보다 커질 때 까지 새로운 left 생성
            for num in nums:
                if s + num <= mid: 
                    s += num
                else:
                    s = num
                    cnt += 1

            # 만약 m보다 더 많이 쪼개 졌다면
            # l을 mid + 1로 하여(이진 탐색) 더 많은 수가 한 sub array에 들어가도록 한다.
            if cnt > m:
                l = mid + 1
            else:
                r = mid

        return r


if __name__ == '__main__':
    nums = [7,2,5,10,8]
    m = 2

    ret = Solution().splitArray(nums, m)
    print("----------- ", ret)

    
    nums = [1,2,3,4,5]
    m = 2

    ret = Solution().splitArray(nums, m)
    print("----------- ", ret)

    
    nums = [1, 4, 4]
    m = 3

    ret = Solution().splitArray(nums, m)
    print("----------- ", ret)
    
    
    nums = [1,2,3,4,5]
    m = 1

    ret = Solution().splitArray(nums, m)
    print("----------- ", ret)
    
    nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
    m = 8

    ret = Solution().splitArray(nums, m)
    print("----------- ", ret)