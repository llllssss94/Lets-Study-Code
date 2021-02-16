num = []

for i in range(10):
    n = int(input())
    num.append(n % 42)

# 중복을 알아서 지워주죠~
num = set(num)

print(len(num))
