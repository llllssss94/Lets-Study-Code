from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        digit_list = [digits_map[i] for i in digits]

        if not digits:
            return ""

        comb_list = []
        for digit_data in digit_list:
            if not comb_list:
                comb_list = digit_data.copy()
            else:
                tmp = []
                for c in digit_data:
                    tmp += [cb + c for cb in comb_list]

                comb_list = tmp.copy()

        return sorted(comb_list)

if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))

    digits = ""
    print(Solution().letterCombinations(digits))

    digits = "2"
    print(Solution().letterCombinations(digits))

    digits = "234"
    print(Solution().letterCombinations(digits))