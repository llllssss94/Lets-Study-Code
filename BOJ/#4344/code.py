n = int(input())

for i in range(n):
    case = list(map(int, input().split(' ')))
    num = case[0]
    case = case[1:]

    avg = sum(case)/num
    cnt = 0
    for score in case:
        if score > avg:
            cnt += 1

    print("%.3f%%" % ((cnt/num) * 100))
