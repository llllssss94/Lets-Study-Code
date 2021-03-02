from itertools import combinations

n, m = map(int, input().split(' '))

r = combinations(range(1, n+1), m)

for s in r:
    print(' '.join(map(str, s)))

"""
visited = [False] * n

s = []

def recurse(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, s)))
        return

    # idx를 통해서 idx까지 탐색이 끝낫음을 전달하면 해결
    for i in range(idx, n):

        if not visited[i]:
        
            visited[i] = True

            s.append(i + 1)

            recurse(depth + 1, i, n, m)

            visited[i] = False
            
            s.pop()

if __name__ == "__main__":    
    recurse(0, 0, n, m)
    
"""
