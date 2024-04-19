import sys

T = int(input())

result = []
for _ in range(T):
    n = int(input())

    five = n // 5
    remain = n % 5

    result.append( ("++++ " * five) + ("|" * remain) )

for str in result:
    print(str)