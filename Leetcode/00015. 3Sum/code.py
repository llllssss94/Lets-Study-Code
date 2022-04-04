from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()

        # three pointer
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1


            while r > l:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    # i가 작은 수에서 점점 커지므로
                    # r을 낮춤
                    answer.add((nums[i], nums[l], nums[r]))
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1


        return answer



if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]

    ret = Solution().threeSum(nums)
    print(ret)

    
    nums = [0, 0, 0]

    ret = Solution().threeSum(nums)
    print(ret)