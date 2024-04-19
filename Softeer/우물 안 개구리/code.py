import sys

N, M = map(int, input().split(" "))

weights = [0] + list(map(int, input().split(" ")))

i_am_best = [0] + [True for _ in range(N)]

for _ in range(M):
    a, b = input().split(" ")

    if weights[int(a)] <= weights[int(b)]:
        i_am_best[int(a)] = False


    if weights[int(b)] <= weights[int(a)]:
        i_am_best[int(b)] = False


print(sum(i_am_best))
