def get_divisor(num):    
    divisor = list(set([1, num]))
    for i in range(2, num//2 + 1):
        if num % i == 0:
            divisor.append(i)
            
    return divisor

def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        if len(get_divisor(num)) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer