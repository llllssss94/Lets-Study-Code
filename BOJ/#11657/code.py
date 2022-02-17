# 모든 경로에 대한 최단경로 찾기 - 벨만 포드
def bellman_ford(n, m):
    # 최대 10000보다 큰 값으로 초기화
    distance = [1e11, ] * n

    edge = []
    
    # 버스 노선 정보 입력
    for _ in range(m):
        a, b, d = map(int, input().split(' '))
        edge.append((a, b, d))


    # 출발도시는 0으로 초기화
    distance[0] = 0

    # 도시 크기 - 1 만큼 반복
    for i in range(n):
        # 입력된 노선 정보마다
        for current_node, next_node, cost in edge:
            # 입력된 edge 정보를 꺼내서

            # 
            if (distance[current_node-1] != 1e11) and (distance[next_node-1] > distance[current_node-1] + cost):
                distance[next_node-1] = distance[current_node-1] + cost
                if i == n - 1:
                    return True, distance
                
    return False, distance


n, m = map(int, input().split(' '))

is_cyclic, result = bellman_ford(n, m)

if is_cyclic:
    print('-1')
else:
    # 첫번째 노드 제외
    for c in result[1:]:
        if c == 1e11:
            print('-1')
        else:
            print(c)


