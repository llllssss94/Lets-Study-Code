def solution(routes):
    answer = 0
    
    # 나간 순서대로 나열
    routes = sorted(routes, key=lambda x : x[1])
    cur = -30001
    
    # 하나씩 보면서
    for s, e in routes:
        # 카메라가 커버가 안되면 해당 자동차의 나가는 위치에 카메라 설치
        if cur < s:
            answer += 1
            cur = e
        # 카메라가 커버가능한 경우
        else:
            continue
    
    return answer