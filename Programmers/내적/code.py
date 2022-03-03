def solution(a, b):
    answer = 0
    for i in range(0, len(a)):
        answer += a[i] * b[i]
    return answer