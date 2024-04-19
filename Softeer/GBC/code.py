import sys

N, M = map(int, input().split(" "))

limit_info = []

for i in range(N):
    road, speed = map(int, input().split(" "))

    if i != 0:
        limit_info.append((limit_info[i-1][0]+road, speed))
    else:
        limit_info.append((road, speed))

max_exceed = 0

position = 0
road_num = 0

for _ in range(M):
    road, speed = map(int, input().split(" "))
    position += road

    # 출발 구간 체크
    max_exceed = max(max_exceed, speed - limit_info[road_num][1])

    # 갈수있는 구간 내에서 구간내 최대 속도 체크
    while position > limit_info[road_num][0]:
        road_num += 1
        max_exceed = max(max_exceed, speed - limit_info[road_num][1])
    
    # 경계 처리
    if position == limit_info[road_num][0] and road_num < N:
        road_num += 1

print(max_exceed)