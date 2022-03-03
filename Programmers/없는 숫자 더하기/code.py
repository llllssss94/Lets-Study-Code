def solution(numbers):
    visited = list(range(10))
    
    for num in numbers:
        if visited[num] == num:
            visited[num] = 0
            
    answer = sum(visited)
    
    return answer