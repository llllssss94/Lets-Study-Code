from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        i = 0
        answer = []

        while i < len(ops):
            if ops[i] not in ["C", "D", "+"]:
                answer.append(int(ops[i]))
            else:
                if ops[i] == "C":
                    answer = answer[:-1]
                elif ops[i] == "D":
                    answer.append(answer[-1]*2)
                else:
                    answer.append(answer[-1] + answer[-2])
            i += 1
        
        return sum(answer)

if __name__ == "__main__":
    ops = ["5","2","C","D","+"]

    ret = Solution().calPoints(ops)
    print(ret)