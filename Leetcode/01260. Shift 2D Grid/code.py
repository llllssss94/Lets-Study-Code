from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(grid)
        m = len(grid[0])

        flatten = []

        # 일자로 만들고
        for r in grid:
            flatten += r

        # 재조합
        l = len(flatten)
        k = k % l
        flatten = flatten[l - k:] + flatten[:l-k]

        return [flatten[i * m: (i + 1) * m] for i in range(n)]


if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1

    ret = Solution().shiftGrid(grid, k)
    print(ret)

    
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 9

    ret = Solution().shiftGrid(grid, k)
    print(ret)

    

    
    grid = [[1],[2],[3],[4],[7],[6],[5]]
    k = 23

    ret = Solution().shiftGrid(grid, k)
    print(ret)
