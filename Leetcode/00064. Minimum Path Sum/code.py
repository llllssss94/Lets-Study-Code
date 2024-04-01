from typing import *

class Solution:
    def minPathSum_BP(self, grid: List[List[int]]) -> int:
        # Best Practice
        # 한변을 미리 다 계산 후, 다음 변을 한개씩 옮겨가며 격자로 올수 있는 곳을 min값 계산하도록 하는 케이스...
        # 훨씬 간단하고 명료하다...

        m = len(grid)
        n = len(grid[0])
        # 양변부터 cost 계산
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                # 위쪽, 왼쪽 중 cost 적은 곳 가져옴
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        def move_once(x_idx, y_idx, grid, cost, cost_map):
            # 현재 위치 cost 합산
            cost += grid[x_idx][y_idx]

            # 1. 방문하지 않았거나, 2, 이미 방문한 경우 현재 경로의 cost와 비교
            if cost_map[x_idx][y_idx] > cost or cost_map[x_idx][y_idx] == 0:
                cost_map[x_idx][y_idx] = cost
            else:
                # 현재 경로의 Cost가 이전 탐색보다 크면 중간에 멈춘다. (DP)
                return

            # 목적지 도달
            if x_idx == m-1 and y_idx == n-1:
                return
            
            # 한쪽 끝에 다다른 경우
            if x_idx == m-1 :
                move_once(x_idx, y_idx+1, grid, cost, cost_map)

            elif y_idx == n-1:
                move_once(x_idx+1, y_idx, grid, cost, cost_map)
            else:
                # 보통의 경우 x든 y든 아무대나 먼저 간다.
                move_once(x_idx+1, y_idx, grid, cost, cost_map)
                move_once(x_idx, y_idx+1, grid, cost, cost_map)
        
        m = len(grid)
        n = len(grid[0])

        cost_map = [[0,]*n for _ in range(m)]

        move_once(0, 0, grid, 0, cost_map)

        return cost_map[-1][-1]

    
if __name__ == "__main__":
    # grid = [[1,3,1],[1,5,1],[4,2,1]]
    grid = [[1,2,3],[4,5,6]]
    print(Solution().minPathSum_BP(grid))