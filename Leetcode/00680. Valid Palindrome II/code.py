class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        # 처음 다른 곳 찾기
        while l < r:
            if s[l] != s[r]:
                break
            l += 1
            r -= 1

        if l >= r:
            return True

        l_del = self.is_Palindrome(s[:l] + s[l+1:])
        r_del = self.is_Palindrome(s[:r] + s[r+1:])
        

        return l_del | r_del

    
    def is_Palindrome(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True


if __name__ == "__main__":
    s = "aba"

    ret = Solution().validPalindrome(s)
    print(ret)

    

    s = "abca"

    ret = Solution().validPalindrome(s)
    print(ret)


    
    s = "abc"

    ret = Solution().validPalindrome(s)
    print(ret)

    
    s = "deeee"

    ret = Solution().validPalindrome(s)
    print(ret)