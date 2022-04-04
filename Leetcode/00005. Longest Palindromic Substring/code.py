class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        max_len = 0
        
        for i in range(len(s)):
            # 홀수 길이
            # 시작점
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    answer = s[l:r+1]
                    max_len = r - l +    1
                l -= 1
                r += 1
            
            # 짝수 길이
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    answer = s[l:r+1]
                    max_len = r - l + 1
                l -= 1
                r += 1
        
        return answer

       


if __name__ == "__main__":
    s = "babad"
    ret = Solution().longestPalindrome(s)

    print(ret)

    
    s = "cbbd"
    ret = Solution().longestPalindrome(s)

    print(ret)

    


    