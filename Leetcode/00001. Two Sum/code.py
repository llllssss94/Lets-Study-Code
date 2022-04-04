class Solution:
    def twoSum(self, nums, target):
        f_i = 0
        s_i = len(nums) - 1

        
        sorted_num = sorted(nums)
        # 오름차순 정렬 후 투 포인터로 찾기
        while f_i <= s_i:
            cur_sum = sorted_num[f_i] + sorted_num[s_i]
            if cur_sum == target:
                break
            else:
                if cur_sum < target:
                    f_i += 1
                else:
                    s_i -= 1

        # 같은 수
        if sorted_num[f_i] == sorted_num[s_i]:
            answer = [i for i, x in enumerate(nums) if x == sorted_num[f_i]]
        else:
            answer = [nums.index(sorted_num[f_i]), nums.index(sorted_num[s_i])]
        
        return answer
        

if __name__ == "__main__":
    s = Solution()

    l = [2,7,11,15]
    t = 9

    print(s.twoSum(l, t))

    l = [3,2,4]
    t = 6
    print(s.twoSum(l, t))

    l = [3,3]
    t = 6
    print(s.twoSum(l, t))

    l = [-3,4,3,90]
    t = 0
    print(s.twoSum(l, t))