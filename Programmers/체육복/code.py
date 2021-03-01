def solution(n, lost, reserve):
    answer = 0
    
    student = [1] * n
    
    for i in lost:
        student[i-1] -= 1
        
    for i in reserve:
        student[i-1] += 1
    
    for i in range(0, len(student)):
        if student[i] == 1:
            answer += 1
            continue
            
        if student[i] == 2:
            answer += 1
            if i == 0:
                if student[i+1] == 0:
                    student[i+1] += 1
                    student[i] -= 1
                    continue
            elif i == len(student) - 1:
                if student[i - 1] == 0:
                    student[i-1] += 1
                    student[i] -= 1
                    answer += 1
                    continue
            else:
                if student[i - 1] == 0:
                    student[i-1] += 1
                    student[i] -= 1
                    answer += 1
                    continue
                elif student[i+1] == 0:
                    student[i+1] += 1
                    student[i] -= 1
                    continue
                
    return answer

if __name__ == "__main__":
    # case 1
    result = solution(5, [2, 4], [1, 3, 5])
    print(result)

    # case 2
    result = solution(5, [2, 4], [3])
    print(result)

    # case 3
    result = solution(3, [3], [1])
    print(result)
