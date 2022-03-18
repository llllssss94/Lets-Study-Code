class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_cnt = 0
        
        substr=''
        # 순차적으로 탐색하면서
        for c in s:
            # substr에 존재하는 알파벳이 나오면, 이전까지 최대 길이 구하고 중복 이후 부터 슬라이딩 윈도우
            if c in substr:
                max_cnt = max(max_cnt, len(substr))

                substr = substr[substr.index(c)+1:] + c
            else:
                substr += c
        
        # 1글자인 경우
        max_cnt = max(max_cnt, len(substr))
        
        return max_cnt
        
if __name__ == "__main__":

    s = "abcabcbb"

    ret = Solution().lengthOfLongestSubstring(s)

    print(ret)

    s = "pwwkew"

    ret = Solution().lengthOfLongestSubstring(s)

    print(ret)
