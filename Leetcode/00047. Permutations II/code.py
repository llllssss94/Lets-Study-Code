from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        self.recurse(answer, [], nums)

        return answer

    # dfs with backtracking optim
    def recurse(self, answer, history, nums):
        if not nums:
            answer.append(history)
            return

        for i in range(len(nums)):
            # 방금 전에 방문한 숫자가 반복됬을 때는 skip
            if i > 0 and nums[i] == nums[i-1]:
                continue

            self.recurse(answer, history + [nums[i]], nums[:i] + nums[i+1:])

        return answer

if __name__ == "__main__":
    nums = [1,1,2]

    ret = Solution().permuteUnique(nums)
    print(ret)