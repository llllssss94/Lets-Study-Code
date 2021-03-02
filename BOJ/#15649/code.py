from itertools import permutations

n, m = map(int, input().split(' '))

r = permutations(range(1, n+1), m)

for s in r:
    print(' '.join(map(str, s)))

"""
visited = [False] * n

s = []

def recurse(depth, n, m):
    if depth == m:
        print(' '.join(map(str, s)))
        return

    
    for i in range(len(visited)):
        if visited[i] != True:
            
            visited[i] = True # visit!

            s.append(i+1) # index + 1
            
            recurse(depth+1, n, m) # next depth

            visited[i] = False # done

            s.pop() # 출력 이후 빠져나오므로 이미 출력한 것을 하나씩 순차 제거


if __name__ == "__main__":
    recurse(0, n, m)
"""
