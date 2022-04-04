from typing import List
from itertools import permutations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = [[chr(ord('a') + (3*i) + j) for j in range(3)] for i in range(5)]
        digit_map.append(['p', 'q', 'r', 's'])
        digit_map.append(['t', 'u', 'v'])
        digit_map.append(['w', 'x', 'y', 'z'])

        answer = []
        for n in digits:
            num = int(n) - 2
            if len(answer) == 0:
                answer = digit_map[num]
            else:
                new_c = []
                for c in answer:
                    for k in digit_map[num]:
                        new_c.append(c + k)
                    
                answer = new_c

        return answer

if __name__ == "__main__":
    digits = "23"

    ret = Solution().letterCombinations(digits)
    print(ret)


    
    digits = ""

    ret = Solution().letterCombinations(digits)
    print(ret)

    
    digits = "2"

    ret = Solution().letterCombinations(digits)
    print(ret)