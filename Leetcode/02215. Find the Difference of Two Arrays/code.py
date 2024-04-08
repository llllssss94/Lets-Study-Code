from typing import *

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        answer.append(list(set(nums1) - set(nums2)))
        answer.append(list(set(nums2) - set(nums1)))

        return answer
    
if __name__ == "__main__":
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    print(Solution().findDifference(nums1, nums2))