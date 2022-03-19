from collections import deque

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ['' for _ in range(numRows)]
        
        i = 0
        direction = 1

        # 1줄은 그냥 바로 처리
        if numRows == 1:
            return s

        for c in s:
            # 문자 삽입
            answer[i] += c

            # 진행
            i += direction
            
            # 방향 전환
            if i >= numRows - 1:
                direction = -1
            if i <= 0:
                direction = 1

        # 출력 순서 별로 문자열 생성
        answer = ''.join(answer)

        return answer


if __name__ == "__main__":
    s = 'PAYPALISHIRING'
    numRows = 3

    ret = Solution().convert(s, numRows)

    print(ret)

    
    numRows = 4

    ret = Solution().convert(s, numRows)

    print(ret)


    s = "AB"
    numRows = 1

    ret = Solution().convert(s, numRows)

    print(ret)