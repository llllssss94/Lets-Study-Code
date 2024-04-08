from typing import *

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 매번 모든 방을 방문할 수 있는지 체크하므로 공통 Map으로 체크 가능
        # 만약 경로탐색이라면 History 로 가야함
        is_visit = [False for _ in range(len(rooms))]

        def dfs(room_num, rooms, is_visit):
            # 방문 처리
            is_visit[room_num] = True

            for cand_num in rooms[room_num]:
                if is_visit[cand_num] != True:
                    dfs(cand_num, rooms, is_visit)
        
        dfs(0, rooms, is_visit)

        return sum(is_visit) == len(rooms)
    
if __name__ == "__main__":
    rooms = [[1],[2],[3],[]]
    print(Solution().canVisitAllRooms(rooms))

    rooms = [[1,3],[3,0,1],[2],[0]]
    print(Solution().canVisitAllRooms(rooms))
