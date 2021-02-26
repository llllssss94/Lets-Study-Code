def recursive(n):
    s = n
    
    while n > 0:
        s += n % 10
        n = n // 10

    return s

count = [0]*10001

for i in range(1, 10000):
    temp = recursive(i)

    while temp <= 10000:
        count[temp] += 1
        temp = recursive(temp)


for i in range(1, 10001):
    if count[i] == 0:
        print(i)
