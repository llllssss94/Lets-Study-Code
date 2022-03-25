
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substr_dict = {}

        # Sliding window
        # sub string 생성 및 counting
        for sl in range(minSize, maxSize + 1):
            # 시작점 sliding, size 만큼 windows 생성
            for i in range(len(s) - sl + 1):
                ss = s[i:i+sl]

                # python set 자료구조를 활용해서 max Letters 세기
                if ss not in substr_dict:
                    if len(set(ss)) <= maxLetters:
                        substr_dict[ss] = 1
                else:
                    if len(set(ss)) <= maxLetters:
                        substr_dict[ss] += 1

        if substr_dict:
            return max(substr_dict.values())
        
        return 0


if __name__ == "__main__":
    s = "aababcaab"
    maxLetters = 2
    minSize = 3
    maxSize = 4

    ret = Solution().maxFreq(s, maxLetters, minSize, maxSize)
    print(ret)

    
    s = "aaaa"
    maxLetters = 1
    minSize = 3
    maxSize = 3

    ret = Solution().maxFreq(s, maxLetters, minSize, maxSize)
    print(ret)

    
    s = "abcde"
    maxLetters = 2
    minSize = 3
    maxSize = 3

    ret = Solution().maxFreq(s, maxLetters, minSize, maxSize)
    print(ret)
