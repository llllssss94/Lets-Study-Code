from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones:
            stones.sort()
            n1 = stones.pop()

            if stones:
                n2 = stones.pop()
            else:
                break

            if n1 == n2:
                n1 = 0
                continue
            else:
                stones.append(n1 - n2)
        
        return n1

if __name__ == "__main__":
    stones = [2,7,4,1,8,1]

    ret = Solution().lastStoneWeight(stones)
    print(ret)

    
    stones = [1]

    ret = Solution().lastStoneWeight(stones)
    print(ret)


    stones = [2, 2]

    ret = Solution().lastStoneWeight(stones)
    print(ret)



    stones = [7,6,7,6,9]

    ret = Solution().lastStoneWeight(stones)
    print(ret)
