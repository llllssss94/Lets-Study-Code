from collections import deque, defaultdict

def solution(n, edge):
    answer = 0
    
    dist_map = {i:0 for i in range(1, n+1)}
    edges = defaultdict(list)
    
    
    for s, e in edge:
        edges[s].append(e)
        edges[e].append(s)
    
    que = deque([1])
    dist = 1
    while que:
        # 거리를 기록해야 하므로 BFS
        for i in range(len(que)):
            node = que.popleft()
            
            # 0이면 방문한 적 없는 노드
            if dist_map[node] == 0:
                dist_map[node] = dist

                for e in edges[node]:
                    que.append(e)
        
        dist += 1
    
    # 최대 거리에 해당하는 노드 수 세기
    max_dist = max(dist_map.values())
    
    for k, v in dist_map.items():
        if v == max_dist and k != 1:
            answer += 1
    
    return answer