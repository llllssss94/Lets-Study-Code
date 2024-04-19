import sys

N = int(input())

text = []
for _ in range(N):
    s, t = input().split()

    for i, c in enumerate(s):
        if c == 'X' or c == 'x':
            p = i
            break

    if ord(t[p]) > ord('Z'):
        text.append(chr(ord(t[p]) - 32))
    else:
        text.append(t[p])


print(''.join(text))
