from typing import List
from collections import deque

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 정렬된 리스트들임            
        # O(n + m)
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2
        nums1 = deque(nums1)
        nums2 = deque(nums2)

        # 예외 처리 들
        if l == 1:
            if nums1:
                n = nums1.popleft()
            if nums2:
                n = nums2.popleft() 
            return n

        # 한 배열만 있는 경우 빠르게 처리
        if not nums1:
            if l % 2 == 0 :
                return (nums2[l//2 - 1] + nums2[(l//2)]) / 2
            else:
                return nums2[l//2]
        elif not nums2:
            if l % 2 == 0:
                return (nums1[l//2 - 1] + nums1[(l//2)]) / 2
            else:
                return nums1[l//2]

        # 홀수 인 경우
        # 두 배열이 비어있지 않은 경우
        p1 = 0
        p2 = 0
        if l % 2 != 0:
            median = 0
            while (p1 + p2) < ((l // 2) + 1):
                if p1 == l1 :
                    median = nums2[p2]
                    p2 += 1
                    continue
                if p2 == l2 :
                    median = nums1[p1]
                    p1 += 1
                    continue

                if nums1[p1] < nums2[p2]:
                    median = nums1[p1]
                    p1 += 1
                else:
                    median = nums2[p2]
                    p2 += 1

            answer = median
        else:
            # 짝수 인 경우
            answer = []
            median = 10e-7
            while (p1 + p2) < (l // 2) + 1:
                if p1 == l1 :
                    last = median
                    median = nums2[p2]
                    p2 += 1
                    continue
                if p2 == l2 :
                    last = median
                    median = nums1[p1]
                    p1 += 1
                    continue

                if nums1[p1] < nums2[p2]:
                    last = median
                    median = nums1[p1]
                    p1 += 1
                else:
                    last = median
                    median = nums2[p2]
                    p2 += 1
            answer = (last + median) / 2

        return answer

    def findMedianSortedArraysBS(self, nums1: List[int], nums2: List[int]) -> float:
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

