class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0:
            return True
            
        memo = {}
        
        # 만들 수 없는 경우
        if desiredTotal > maxChoosableInteger * (maxChoosableInteger+1) // 2:
            return False
            
        # Use bit mask
        return self.recursion(2**maxChoosableInteger-1, desiredTotal, memo, desiredTotal)

    
    def recursion(self, mask, total, memo, desiredTotal):
        # 한 방에 종료 가능한 경우
        # 만약 1st 플레이어 턴에 이 조건에 걸리면 이기는 것임ㄴ
        if mask >= 2**(total-1):
            return True

        # DP
        if mask in memo:
            return memo[mask]
        
        for i in range(desiredTotal):
            # i 번째 bit mask가 unset 되어 있으면 사용한 것임
            if mask & (1 << i):
                # i 번째 bit mask를 unset 해서 사용 처리
                newmask = mask & ~(1 << i)
                if self.recursion(newmask, total - (i + 1), memo, desiredTotal) == False:
                    # memoization
                    memo[mask] = True
                    return True

        # memoization
        memo[mask] = False

        return False
        


if __name__ == "__main__":
    maxChoosableInteger = 10
    desiredTotal = 11

    ret = Solution().canIWin(maxChoosableInteger, desiredTotal)
    print(ret)


    
    maxChoosableInteger = 10
    desiredTotal = 0

    ret = Solution().canIWin(maxChoosableInteger, desiredTotal)
    print(ret)


    
    maxChoosableInteger = 10
    desiredTotal = 1

    ret = Solution().canIWin(maxChoosableInteger, desiredTotal)
    print(ret)

    
    
    maxChoosableInteger = 10
    desiredTotal = 40

    ret = Solution().canIWin(maxChoosableInteger, desiredTotal)
    print(ret)