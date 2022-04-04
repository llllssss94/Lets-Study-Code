
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # DP 활용하며, 뒤에서 부터 확인해야 함
        print("Owww")
        
        return True        


if __name__ == "__main__":
    s = 'aa'
    p = 'a'

    ret = Solution().isMatch(s, p)
    print(ret)

    
    s = 'aa'
    p = 'a*'

    ret = Solution().isMatch(s, p)
    print(ret)

    
    s = 'aa'
    p = '.*'

    ret = Solution().isMatch(s, p)
    print(ret)

    
    
    s = 'aab'
    p = 'c*a*b'

    ret = Solution().isMatch(s, p)
    print(ret)


    
    s = 'aaa'
    p = 'a*a'

    ret = Solution().isMatch(s, p)
    print(ret)