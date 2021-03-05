from collections import deque

def recurse(depth, begin, target, words, visited):
    queue = deque([begin])

    # DFS
    while queue:
        w = queue.popleft()

        # target에 도달 했다면 바로 return
        if w == target:
            return depth

        # 후보 찾는 과정
        for i in range(len(words)):
            # 한글자씩 바꾸므로 하나만 다른 후보 탐색
            diff = 0
            for j in range(len(w)):
                if w[j] != words[i][j]:
                    diff += 1

            # 하나만 다르면 방문 표시 후 큐에 추가 이미 방문 한 경우 SKIP
            if diff == 1 and visited[i] != True:
                # 현재 경로에서 이미 방문했다는 것을 표시
                visited[i] = True
                # 후보 큐에 추가
                queue.append(words[i])

        # 후보가 없는 경우
        if len(queue) < 1:
            return -1

        # 후보 중에서 가장 depth가 낮은 경우 
        min_dep = 50
        for c in queue:
            # Next depth
            r = recurse(depth + 1, c, target, words, visited)
            if r == -1:
                continue
            min_dep = min(min_dep, r)
            
        # 어떤 후보도 불가능한 경우
        if min_dep == 50:
            return -1

        return min_dep

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    visited = [False] * len(words)

    answer = recurse(0, begin, target, words, visited)
    
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
