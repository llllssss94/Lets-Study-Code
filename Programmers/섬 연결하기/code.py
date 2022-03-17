def find_parent(i, parents):
    if parents[i] == i:
        return i
    
    return find_parent(parents[i], parents)

def union_parent(x, y, parents):
    x = find_parent(x, parents)
    y = find_parent(y, parents)
    
    parents[y] = x

def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]
    visited = [False, ] * n
    
    costs = sorted(costs, key=lambda x: x[2])
    
    # 크루스칼 알고리즘
    # Cost가 낮은순으로 탐색하므로 가장 낮은 간선만 선택됨
    for s, e, c in costs:
        # 연결된 적 없는 노드만 추가
        if find_parent(s, parents) != find_parent(e, parents):
            visited[s] = True
            visited[e] = True

            union_parent(s, e, parents)
            answer += c
            
    return answer