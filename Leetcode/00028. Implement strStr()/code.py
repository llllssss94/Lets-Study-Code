class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r = 0
        answer = -1

        # needle이 없으면 0
        if not needle:
            return 0

        # 최소 needle 길이만큼 남앗을 때까지
        for i in range(len(haystack) - len(needle) + 1):
            # 첫문자가 같으면 확인해본다.
            c = haystack[i]
            if c == needle[r]:
                # 시작점 찾기
                answer = i

                # 확인해보기
                is_same = True
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        is_same = False
                        break
                
                # 찾으면 바로 return
                if is_same:
                    return answer

        return -1


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"

    ret = Solution().strStr(haystack, needle)
    print(ret)


    
    haystack = "aaaaa"
    needle = "bba"

    ret = Solution().strStr(haystack, needle)
    print(ret)


    
    
    haystack = "abc"
    needle = "c"

    ret = Solution().strStr(haystack, needle)
    print(ret)

    
    
    
    haystack = "asd"
    needle = ""

    ret = Solution().strStr(haystack, needle)
    print(ret)

    
    
    
    haystack = "a"
    needle = "a"

    ret = Solution().strStr(haystack, needle)
    print(ret)