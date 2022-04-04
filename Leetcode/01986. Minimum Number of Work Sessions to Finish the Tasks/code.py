from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # use list to use as pointer
        answer = [len(tasks)]
        tasks.sort(reverse=True)

        self.dfs(0, answer, tasks, [], sessionTime)

        return answer[0]
 
    
    def dfs(self, idx, answer, tasks, session, sessionTime):
        # min보다 커진 경우
        # 이부분이 시간 단축 핵심
        if len(session) > answer[0]:
            return

        # 전체 다 넣은 경우
        if idx == len(tasks):
            answer[0] = len(session)
            return

        # 각 session에 넣는 경우를 모두 탐색함
        for i in range(len(session)):
            # 현재 session에 넣을 수 있으면
            if session[i] + tasks[idx] <= sessionTime:
                # 더하고
                session[i] += tasks[idx]
                # 다음 task로 넘어가고
                self.dfs(idx + 1, answer, tasks, session, sessionTime)
                # 원상 복귀
                session[i] -= tasks[idx]
        
        # 위의 for문에서는 현재 존재하는 session에 넣어보는 것이고
        # 여기는 새로운 session 여는 경우를 보는 것 
        session.append(tasks[idx])
        self.dfs(idx + 1, answer, tasks, session, sessionTime)
        session.pop()



if __name__ == "__main__":
    tasks = [1,2,3]
    sessionTime = 3

    ret = Solution().minSessions(tasks, sessionTime)
    print(ret)


    tasks = [1,2,3,3,1,1,3,2,2,1]
    sessionTime = 11

    ret = Solution().minSessions(tasks, sessionTime)
    print(ret)

    
    tasks = [9,8,8,4,6]
    sessionTime = 14

    ret = Solution().minSessions(tasks, sessionTime)
    print(ret)