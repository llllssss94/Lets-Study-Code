import sys

N = int(input())

# 변의 갯수로 세어본다.

# 1단계 변은 2개이다. -> 2 - 1 = 1 
# 2단계 변은 3개이다. -> 3 - 1 = 2
# 3단계 변은 5개이다. -> 5 - 1 = 4
# 4단계 변은 9개이다. -> 9 - 1 = 8
# 변의 사이에 변이 추가되므로 N개의 변이 존재할때 N-1개의 변을 더 추가하게 된다.

# A_i+1 = A_i + (A_i - 1) = A_i * 2 - 1

def next_line_num(line_num):
    next_line_num = line_num * 2 - 1

    return next_line_num

# N개의 변이 만나면 N*N개의 점이 만들어진다.

line_num = 2

for _ in range(N):
    line_num = next_line_num(line_num)

print(line_num * line_num)