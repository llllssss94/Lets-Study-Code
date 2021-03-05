from collections import deque

def solution(n, computers):
    root = 0
    visited = [False] * n
    answer = 0

    for i in range(n):

        # 순차적으로 방문 안했던 곳에서 다시 시작
        root = i
        if visited[i] == True:
            continue

        # DFS 시작, 방문 안한 가장 앞 노드를 root로 탐색
        stack = deque([root])
        # 새로운 root가 나왔으므로 네트워크 갯수 증가
        answer += 1

        # DFS
        while len(stack) != 0:
            # 스택에 저장된 노드들 하나씩 꺼내서
            c = stack.pop()
            # 방문 표시하고
            visited[c] = True

            # 방문한 노드의 자식 노드를 다시 큐에 넣음
            for i in range(1, n):
                # 이미 방문한 경우 SKIP
                if computers[c][i] == 1 and visited[i] == False:
                    stack.append(i)
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
