n, m = map(int, input().split(' '))

visited = [False] * n

s = []

def recurse(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, s)))
        return

    for i in range(idx, n):
        s.append(i + 1)

        recurse(depth+1, i, n, m)

        s.pop()

recurse(0, 0, n, m)
