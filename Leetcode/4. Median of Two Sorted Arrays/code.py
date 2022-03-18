from typing import List
from collections import deque

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 정렬된 리스트들임        
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        h = total // 2

        # 항상 a가 짧도록
        if len(a) > len(b):
            a, b = b, a
        
        # Binary Search
        l, r = 0, len(a) - 1
        while True:
            a_idx = (l + r) // 2
            b_idx = h - a_idx - 2

            a_left = a[a_idx] if a_idx >= 0 else float('-inf')
            a_right = a[a_idx+1] if a_idx + 1 < len(a) else float('inf')
            b_left = b[b_idx] if b_idx >= 0 else float('-inf')
            b_right = b[b_idx+1] if b_idx + 1 < len(b) else float('inf')

            # left part is correct
            if a_left <= b_right and a_right > b_left:
                if total % 2 == 0:
                    answer = (max(a_left, b_left) + min(a_right, b_right)) / 2
                else:
                    answer = min(a_right, b_right)
                break
            else:
                if a_left > b_right:
                    r = a_idx - 1
                else:
                    l = a_idx + 1

        return answer

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    ret = Solution().findMedianSortedArrays(nums1, nums2)

    print(ret)


    nums1 = [1]
    nums2 = [2, 3]
    ret = Solution().findMedianSortedArrays(nums1, nums2)

    print(ret)
    
    nums1 = [1, 2]
    nums2 = [3, 4]
    ret = Solution().findMedianSortedArrays(nums1, nums2)

    print(ret)

    nums1 = []
    nums2 = [1,2,3,4,5]
    ret = Solution().findMedianSortedArrays(nums1, nums2)

    print(ret)

    
    nums1 = [3]
    nums2 = [-1, -2]
    ret = Solution().findMedianSortedArrays(nums1, nums2)

    print(ret)

