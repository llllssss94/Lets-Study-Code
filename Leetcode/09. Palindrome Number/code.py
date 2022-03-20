from collections import deque
from enum import Flag

class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = deque()

        # 문제 기준으로는 음수면 부호때문에 무조건 False
        # 문제가 이상함
        if x < 0:
            return False

        # deque로 양방향으로 꺼내자
        # 투포인터 써도 좋을듯
        while x:
            nums.append(x%10)
            x = x // 10

        is_pal = True
        while len(nums) > 1:
            front_num = nums.popleft()
            back_num = nums.pop()
            if front_num != back_num:
                is_pal = False
                break

        return is_pal


if __name__ == "__main__":
    x = 121

    ret = Solution().isPalindrome(x)
    print(ret)


    x = -121

    ret = Solution().isPalindrome(x)
    print(ret)

    
    x = 10

    ret = Solution().isPalindrome(x)
    print(ret)