def solution(x, n):
    answer = list(map(lambda n: x*n, range(1, n+1)))
    return answer