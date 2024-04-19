import sys
N = int(input())

lectures = [list(map(int, input().split())) for _ in range(N)]

# 종료시간 기준 정렬
lectures.sort(key= lambda x: x[1])

cnt = 0
ctime = 1

for s, e in lectures:
    if ctime <= s:
        ctime = e
        cnt += 1
        
print(cnt)