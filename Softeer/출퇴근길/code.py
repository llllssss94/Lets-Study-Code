import sys
# 아래 설정은 조금 황당한데, 소프티어 디폴트가 python을 pypy로 해서 재귀 리밋을 풀어야한다고 한다 ㅡㅡ...


sys.setrecursionlimit(10**5)
def DFS(now, adj, visit):
    # 방문 여부만 체크하므로 종료
    if visit[now]==1:
        return
    else:
        visit[now]=1
        for neighbor in adj[now]:
            DFS(neighbor, adj, visit)
    return

if __name__=="__main__":
    n, m = map(int, input().split(" "))

    graph = [[] for _ in range(n+1)]
    graph_r = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int,input().split(" "))
        graph[a].append(b)
        graph_r[b].append(a) # 역방향 그래프

    S, T = map(int, input().split(" "))


    # 정방향 그래프로 일단 S, T각각에서 출발해서 갈수 잇는 모든 곳을 찾음
    fromS = [0] * (n+1)
    # 미리 방문처리해서 도달한경우 종료되도록 함, 아래도 동일
    fromS[T] = 1
    DFS(S, graph, fromS)

    fromT = [0] * (n+1)
    fromT[S] = 1
    DFS(T, graph, fromT)

    # 역방향 그래프로도 S, T로 역으로 돌아갈수 있는지 찾는다.
    # -> 이렇게 찾으면 S 또는 T와 연결된 노드를을 찾을 수 잇는것
    # -> 즉 역방향으로 S, T에서 도달할 수 있다는 것이 거꾸로 그 노드들에서 정방향으로는 S, T로 도달할 수 있다는 뜻
    toS = [0] * (n+1)
    DFS(S, graph_r, toS)

    toT = [0] * (n+1)
    DFS(T, graph_r, toT)
    
    count = 0
    for i in range(1,n+1):
        # S -> T, T -> S 전체를 찾으므로 아래 조건
        if fromS[i] and fromT[i] and toS[i] and toT[i]:
            count+=1

    print(count-2)