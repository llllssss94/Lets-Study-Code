from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        self.recurse(answer, '', n)

        return answer

    def recurse(self, answer, cur, n):
        # 열수 잇는 만큼 열었으면
        if n == 0:
            num = 0
            # 안닫힌 갯수 찾아서
            for c in cur:
                if c == '(':
                    num += 1
                else:
                    num -= 1
            # ) 갯수 = len(cur) - 1 - i
            # 닫아줌
            cur += ')'*(num)
            if cur not in answer:
                answer.append(cur)
            return

        # 현재 닫을 수 있는 갯수 찾기
        num = 0
        for c in cur:
            if c == '(':
                num += 1
            else:
                num -= 1

        # 여는 case부터 하나씩 닫는 것을 늘려가기
        for i in range(num + 1):
            self.recurse(answer, cur + (')' * i) + '(', n - 1)
        


        

if __name__ == "__main__":
    n = 3

    ret = Solution().generateParenthesis(n)
    print(ret)