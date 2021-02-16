n = int(input())

for i in range(n):
    ox = input()
    
    total = 0
    tmp = 0
    for each in ox:
        if each == "O":
            tmp += 1
            total += tmp
        else:
            tmp = 0
    print(total)
