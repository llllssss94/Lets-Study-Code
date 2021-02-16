def solution(brown, yellow):
    answer = []
    
    h = 1
    v = 9

    while h <= v:
        v = (brown / 2) - h + 2
        total = h * v
        if (total - brown) == yellow:
            answer = [int(v), h]
            break
        h += 1
    
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
