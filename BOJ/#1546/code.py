n = int(input())

score = list(map(int, input().split(' ')))

max_val = max(score)
avg = 0

for s in score:
    avg += (s/max_val) * 100

avg = avg / n

print(avg)
