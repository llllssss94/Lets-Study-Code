from operator import le
from re import sub
from turtle import left


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        answer = 0

        # sliding window!
        # 값이 변할 때마다 새롭게 연속된 수의 갯수를 센다.
        # 값이 변한 순간에 이전에 연속되었던 갯수와 지금까지 연속됫던 수 중 작은 수만큼 
        # 왜냐면 0->1인 경우와 1->0인 경우 이전에 연속되었던 0,1이 재사용되기 때문
        # 값이 변하면 이전 숫자가 있던 곳 만큼 윈도우를 줄이는 것

        left_cnt = 0
        curr_cnt = 1

        # 현재 값이 이전값과 다른지 봐야하므로, 1부터 시작해야 함
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                answer += min(curr_cnt, left_cnt)

                left_cnt = curr_cnt
                curr_cnt = 1
            else:
                # 이전 값과 같으면 연속된 수 증가
                curr_cnt += 1

        # 마지막 연속 값에 대해서 추가
        answer += min(curr_cnt, left_cnt)
        
        return answer
        
        


if __name__ == "__main__":
    s = "00110011"

    ret = Solution().countBinarySubstrings(s)
    print(ret)
    
    s = "10101"

    ret = Solution().countBinarySubstrings(s)
    print(ret)

    
    s = "01"

    ret = Solution().countBinarySubstrings(s)
    print(ret)
    

    s = "000111000"

    ret = Solution().countBinarySubstrings(s)
    print(ret)