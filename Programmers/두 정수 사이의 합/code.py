def solution(a, b):
    i = sorted([a, b])
    answer = sum(range(i[0], i[1]+1))
    return answer