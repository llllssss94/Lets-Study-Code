from typing import *

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stk_i = 0
        que_i = 0

        # 샌드위치를 다 먹거나, 학생이 모두 샌드위치를 먹을때 까지
        while stk_i < len(sandwiches) and students:
            if sandwiches[stk_i] == students[que_i]:
                # 먹음 처리
                del students[que_i]
                # queue 마지막 인덱스 오류 방지
                if students:
                    que_i = que_i % len(students)
                stk_i += 1
            else:
                # 지금부터 한바퀴 도는 동안 누군가는 먹어야된다.
                s_dix = que_i
                for i in range(len(students)):
                    tmp = (que_i + i) % len(students)

                    if students[tmp] == sandwiches[stk_i]:
                        que_i = tmp
                        break
                
                # 만약 아무도 못먹는 상태라면 중지
                if que_i == s_dix:
                    break
                
        return len(students)
    
if __name__ == "__main__":
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]
    print(Solution().countStudents(students, sandwiches))

    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    print(Solution().countStudents(students, sandwiches))

    students = [0,0,0,1,1,1,1,0,0,0]
    sandwiches = [1,0,1,0,0,1,1,0,0,0]
    print(Solution().countStudents(students, sandwiches))