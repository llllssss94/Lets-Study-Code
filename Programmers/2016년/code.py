def solution(a, b):
    answer = ''
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    temp = 0
    for i in range(0, a - 1):
        temp += day[i]
    temp += b
    
    answer = week[temp%7]
    
    return answer