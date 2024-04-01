from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        s_price = prices[0]
        s_idx = 0

        # 초기 하락 스킵
        for i, p in enumerate(prices):
            if p > s_price:
                break
            else:
                s_price = p
                s_idx = i
        
        # 지금 파는것보다 내일 수익이 더 작은 경우 판다.
        for i in range(s_idx, len(prices)-1):
            if s_price < 0:
                s_price = prices[i]
            elif s_price > prices[i]:
                # 하락중인데 안 산 경우 다음날 사기로 한다.
                s_price = prices[i]
            else:
                # 이익이 날때까지 하루씩 진행하면서
                # 하루더 기다리는 것보다 지금파는게 좋은경우 바로 판다.
                if prices[i+1] - s_price < prices[i] - s_price and prices[i] - s_price > 0:
                    profit += prices[i] - s_price
                    s_price = -1
        
        # 마지막날 파는게 최고 이익인 경우
        if s_price >= 0 and prices[-1] - s_price > 0:
            profit += (prices[-1] - s_price)
            
        return profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))
    prices = [1,2,3,4,5]
    print(Solution().maxProfit(prices))
    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))
    prices = [2,4,1]
    print(Solution().maxProfit(prices))
    prices = [2,1,2,0,1]
    print(Solution().maxProfit(prices))
    prices = [3,2,6,5,0,3]
    print(Solution().maxProfit(prices))