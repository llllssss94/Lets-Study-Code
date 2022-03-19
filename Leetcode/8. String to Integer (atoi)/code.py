class Solution:
    def myAtoi(self, s: str) -> int:
        sign = None        
        # can use isdigit but implement for study
        # ascii code in in line
        answer = 0
        for c in s:
            if c >= '0' and c <= '9':
                num = ord(c) - ord('0')
                answer = answer * 10 + num
            else:
                # whitespace must be ignored
                if c == ' ':
                    continue
                # sign이 정해진 이후에는 -, +도 중지신호로 처리
                # 처음에 위치하지 않은 경우에도 중지신호로 처리
                if sign is None and answer == 0:
                    if c == '-':
                        sign = -1
                    elif c== '+':
                        sign = 1
                    else:
                        break
                else:
                    # after digit started
                    # other character is end signal
                    break
        
        if sign is not None:
            answer = answer * sign

        if answer >= 2**31:
            answer = 2**31 - 1
        elif answer < -(2**31):
            answer = -(2**31)

        return answer
        

if __name__ == "__main__":
    s = '42'

    ret = Solution().myAtoi(s)
    print(ret)

    
    s = '-42'

    ret = Solution().myAtoi(s)
    print(ret)

    
    s = '41-93'

    ret = Solution().myAtoi(s)
    print(ret)

    s = "words and 987"

    ret = Solution().myAtoi(s)
    print(ret)