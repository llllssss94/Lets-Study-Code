from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        # 순서대로 정렬
        nums = sorted(nums)

        # 중복 제거를 위함
        visited = {}

        # 앞 2숫자는 고정
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # 탐색 재귀 호출
                self.recurse(i, j, j+1, len(nums) - 1, nums, target, answer, visited)
        return answer

    
    def recurse(self, i, j, l, r, nums, target, answer, visited):
        # i,j에 대해 모든 탐색 종료
        if l >= r:
            return

        # 방문 처리를 위한 것
        k = (nums[i], nums[j], nums[l], nums[r])

        s = nums[i] + nums[j] + nums[l] + nums[r]
        
        if s == target:
            # 방문 안한 경우에만 저장
            if k not in visited:
                answer.append([nums[i], nums[j], nums[l], nums[r]])
                visited[k] = True
            # 방문 한 경우에도 이후의 경우의 수를 따지기 위해 l, r 모두 증감
            self.recurse(i, j, l+1, r-1, nums, target, answer, visited)
        elif s < target:
            self.recurse(i, j, l+1, r, nums, target, answer, visited)
        else:
            self.recurse(i, j, l, r-1, nums, target, answer, visited)
            

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0

    ret = Solution().fourSum(nums, target)
    print(ret)


    
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0

    ret = Solution().fourSum(nums, target)
    print(ret)

    
    
    nums = [4,-3,-8,5,2,10,6,3,-4,-4,4,3,0,-10,0,-6,-5,-3]
    target = -19

    ret = Solution().fourSum(nums, target)
    print(ret)