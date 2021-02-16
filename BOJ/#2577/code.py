from collections import Counter

A = int(input())
B = int(input())
C = int(input())

num = list(str(A * B * C))

# 파이썬은 편해요.
count = dict(Counter(num))

for i in range(10):
    # counter에 걸렸으면 최소 한개 이상
    if str(i) in count:
        print(count[str(i)])
    else: # 안걸렸다? 없는거지
        print(0)
    
