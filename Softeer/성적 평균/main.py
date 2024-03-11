avg = []

n, k = map(lambda x: int(x), input().split((" ")))
score = list(map(lambda x: int(x), input().split((" "))))

for i in range(k):
    l, r = map(lambda x: int(x), input().split((" ")))
    avg.append(round(sum(score[l-1 : r]) / (r-l+1),2))

list(map(lambda x: print("%.2f" % x), avg))