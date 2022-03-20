class Solution:
    def intToRoman(self, num: int) -> str:
        # 그리디!
        answer = ''
        roman_map = {
            'M' : 1000,
            'C' : 100,
            'X' : 10,
            'I' : 1
        }
        
        #    'D' : 500,
        #    'L' : 50,
        #    'V' : 5,
        for k, v in roman_map.items():            
            d = num // v
            num = num % v
            
            # 예외 처리의 연속...
            if d == 4:
                if v == 100:
                    abbr = 'D'
                elif v == 10:
                    abbr = 'L'
                else:
                    abbr = 'V'
                answer = answer + k + abbr
            elif d == 9:                
                if v == 100:
                    abbr = 'M'
                elif v == 10:
                    abbr = 'C'
                else:
                    abbr = 'X'
                answer = answer + k + abbr
            elif d ==5:
                if v == 100:
                    abbr = 'D'
                elif v == 10:
                    abbr = 'L'
                else:
                    abbr = 'V'
                answer = answer + abbr
            else:
                if d > 5:
                    d = d - 5
                    if v == 100:
                        abbr = 'D'
                    elif v == 10:
                        abbr = 'L'
                    else:
                        abbr = 'V'
                else:
                    abbr = ''

                answer = answer + abbr + (k * d)
        
        return answer


if __name__ == "__main__":
    num = 3

    ret = Solution().intToRoman(num)
    print(ret)

    
    num = 58

    ret = Solution().intToRoman(num)
    print(ret)
    

    num = 1994

    ret = Solution().intToRoman(num)
    print(ret)

    
    num = 9

    ret = Solution().intToRoman(num)
    print(ret)

    
    num = 68

    ret = Solution().intToRoman(num)
    print(ret)

