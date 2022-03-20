class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
        }

        answer = 0
        
        # 그냥 구현 문제
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i != len(s) - 1:
                    if s[i+1] == 'V':
                        answer += 4
                        i += 2
                    elif s[i+1] == 'X':
                        answer += 9
                        i += 2
                    else:
                        answer += 1
                        i+=1
                else:
                    answer += 1
                    i+=1
            elif s[i] == 'X':
                if i != len(s) - 1:
                    if s[i+1] == 'L':
                        answer += 40
                        i += 2
                    elif s[i+1] == 'C':
                        answer += 90
                        i += 2
                    else:
                        answer += 10
                        i+=1
                else:
                    answer += 10
                    i+=1
            elif s[i] == 'C':
                if i != len(s) - 1:
                    if s[i+1] == 'D':
                        answer += 400
                        i += 2
                    elif s[i+1] == 'M':
                        answer += 900
                        i += 2
                    else:
                        answer += 100
                        i+=1
                else:
                    answer += 100
                    i+=1
            else:
                answer += roman_map[s[i]]
                i += 1
        
        return answer


if __name__ == "__main__":
    s = 'III'

    ret = Solution().romanToInt(s)
    print(ret)

    
    s = 'LVIII'

    ret = Solution().romanToInt(s)
    print(ret)

    
    s = 'MCMXCIV'

    ret = Solution().romanToInt(s)
    print(ret)