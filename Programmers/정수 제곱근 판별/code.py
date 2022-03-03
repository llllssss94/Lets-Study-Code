def solution(n):
    answer = 0
    if int(n ** 0.5) ** 2 == n:
        answer = (int(n ** 0.5) + 1) ** 2
    else:
        return -1
    return answer