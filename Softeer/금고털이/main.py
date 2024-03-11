w, n = map(lambda x: int(x), input().split(" "))

jewels = []

for i in range(n):
    m, p = map(lambda x: int(x), input().split(" "))
    jewels.append((m, p))

total = 0
jewels.sort(key=lambda x: x[1], reverse= True)
i = 0

for i in range(n):
    if w < jewels[i][0]:
        total = total + (w * jewels[i][1])
        break
    else:
        total = total + (jewels[i][0] * jewels[i][1])
        w = w - jewels[i][0]

print(total)