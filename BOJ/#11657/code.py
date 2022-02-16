# 모든 경로에 대한 최단경로 찾기 - 벨만 포드
def bellman_ford(s, n, m):
    # 최대 10000보다 큰 값으로 초기화
    distance = [10001, ] * n 

    edge = []
    
    # 버스 노선 정보 입력
    for _ in range(m):
        a, b, d = map(int, input().split(' '))
        edge.append((a, b, d))


    # 출발도시는 0으로 초기화
    distance[s] = 0

    # 도시 크기 - 1 만큼 반복
    for i in range(n):
        # 입력된 노선 정보마다
        for j in range(m):
            # 입력된 edge 정보를 꺼내서
            current_node = edge[j][0]
            next_node = edge[j][1]
            cost = edge[j][2]

            # 
            if (distance[current_node - 1] <= 10000) and (distance[next_node - 1] > distance[current_node - 1] + cost):
                distance[next_node - 1] = distance[current_node - 1] + cost
                if i == n - 1:
                    return True, distance
                

    return False, distance


n, m = map(int, input().split(' '))

is_cyclic, result = bellman_ford(0, n, m)

if is_cyclic:
    print('-1')
else:
    # 첫번째 노드 제외
    for i in range(1, n):
        if result[i] > 10000:
            print('-1')
        else:
            print(result[i])


