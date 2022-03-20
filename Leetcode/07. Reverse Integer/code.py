
class Solution:
    def reverse(self, x: int) -> int:
        # Fast solution
        answer = 0
        sign = 1
        if x < 0 :
            sign = -1
            x = -x
        
        while x > 0:
            answer = answer * 10 + x % 10
            x = x // 10
        
        answer = answer * sign
        
        if answer >= 2**31 or answer < -(2**31):
            return 0
        return answer

        
        # Python is God
        # Simple Solution
        if x < 0 :
            s_x = str(-x)[::-1]
            x = -int(s_x)
        else:
            s_x = str(x)[::-1]
            x = int(s_x)

        return x




if __name__ == "__main__":
    x = 123

    ret = Solution().reverse(x)
    print(ret)
    
    x = -123

    ret = Solution().reverse(x)
    print(ret)
    
    x = 120

    ret = Solution().reverse(x)
    print(ret)