def solution(n):
    
    answer = ''
    
    # to base 3
    while n > 0:
        answer += str((n % 3))
        n = n // 3
    answer = answer[::-1]
    print(answer)
    
    # to base 10
    result = 0
    for i, n in enumerate(map(int, answer)):
        result += n * (3**i)
    
    return result