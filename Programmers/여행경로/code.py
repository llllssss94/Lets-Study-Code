from collections import deque

answer = []

def recurse(depart, tickets, used, trace):
    # 현재 출발지 기록
    trace.append(depart)
    
    # 모든 티켓을 사용한 경우만 후보 등록
    if sum(used) == len(tickets):
        answer.append(list(trace))
        return 

    # DFS
    for i in range(len(tickets)):
        # 사용가능한 티켓을 모두 찾음
        if tickets[i][0] == depart and used[i] == 0:
            used[i] = 1
            recurse(tickets[i][1], tickets, used, trace)
            trace.pop()
            used[i] = 0


def solution(tickets):
    used = [0] * len(tickets)
    trace = deque([])
    
    recurse('ICN', tickets, used, trace)

    # 알파벳 순 제일 빠른 것
    print(min(answer))
    
    return min(answer)

# 출발 도시 -> 도착 도시 모든 경우 탐색
# 각 도착 도시를 출발 도시로 하여 다시 반복
# 각 경우 별 선택된 리스트를 반환하고 그걸 이어붙여야함
#solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
#solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
solution([['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']])
