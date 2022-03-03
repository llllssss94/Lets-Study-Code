def solution(arr, divisor):
    answer = []
    
    for num in arr:
        if not(num % divisor):
            answer.append(num)
    
    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
    return answer