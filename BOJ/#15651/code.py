n, m = map(int, input().split(' '))

s = []

def recurse(depth, n, m):
    if depth == m:
        print(' '.join(map(str, s)))
        return

    for i in range(n):
        s.append(i+1)

        recurse(depth+1, n, m)

        s.pop()

recurse(0, n, m)
