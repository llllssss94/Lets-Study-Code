class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # 전체를 a로 초기화
        # 사전식 순서이므로 뒤에서부터 최대한 z로 보내버리기!
        answer = [1, ] * n
        remain = k - sum(answer)
        i = n - 1
        
        # 뒤에서 부터 확인, 바로 z로 변환하면서 속도가 매우 빨라짐
        while remain:            
            if remain > 25:
                answer[i] = 26
                remain -= 25
                i -= 1
            else:
                answer[i] += remain
                remain = 0
        
        ret = ''
        # 문자로 변환
        for c in answer:
            ret += chr(c - 1 + ord('a'))
            
        return ret