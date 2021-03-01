def solution(numbers):
    answer = []
    
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = sorted(list(set(answer)))
    
    return answer

if __name__ == "__main__":
    numbers = [2,1,3,4,1]

    result = solution(numbers)

    print(result)

    numbers = [5,0,2,7]	

    result = solution(numbers)

    print(result)
