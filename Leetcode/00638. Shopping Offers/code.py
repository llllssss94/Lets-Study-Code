from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        answer = 0
        visited = {}

        answer = self.recurse(price, special, needs, visited)

        return answer


    # 매순간 needs는 아직 사지 않고 남은 수가 입력됨
    def recurse(self, price, special, needs, visited):
        # 마지막 탐색인 경우 0 반환하여, 하나씩 값이 누적되도록 만듬
        if needs == [0, ] * len(needs):
            return 0

        # Memoisation
        if tuple(needs) in visited:
            return visited[tuple(needs)]

        res = 0
        # 그냥 삿을 때 경우의 수
        for i in range(len(needs)):
            res += price[i] * needs[i]

        # 가능한 special 삿을 때 경우의 수 모두 처리
        for s in special:
            for i in range(len(needs)):
                needs[i] -= s[i]
            
            if False not in [needs[i] >= 0 for i in range(len(needs))]:
                # 하나씩 처리한 상황과도 비교함
                res = min(res, self.recurse(price, special, needs, visited) + s[-1])
            
            # 원상 복귀
            for i in range(len(needs)):
                needs[i] += s[i]

        visited[tuple(needs)] = res
        
        return res


if __name__ == "__main__":
    price = [2,5]
    special = [[3,0,5],[1,2,10]]
    needs = [3,2]

    ret = Solution().shoppingOffers(price, special, needs)
    print(ret)