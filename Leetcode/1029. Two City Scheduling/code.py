from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        answer = 0
        # A cost가 B cost보다 작은 크기 순서 대로
        costs.sort(key=lambda x : x[0] - x[1])

        l, r = 0, len(costs) - 1

        while l < r:
            answer += costs[l][0] + costs[r][1]
            l += 1
            r -= 1
        
        return answer


if __name__ == "__main__":
    costs = [[10,20],[30,200],[400,50],[30,20]]

    ret = Solution().twoCitySchedCost(costs)
    print(ret)


    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    
    ret = Solution().twoCitySchedCost(costs)
    print(ret)


    costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    
    ret = Solution().twoCitySchedCost(costs)
    print(ret)
