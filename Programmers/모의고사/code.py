def solution(answers):
    answer = []
    
    score = [0, 0, 0]
    
    a1 = range(1, 6)
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(0, len(answers)):
        if answers[i] == a1[i%len(a1)]:
            score[0] += 1
        if answers[i] == a2[i%len(a2)]:
            score[1] += 1
        if answers[i] == a3[i%len(a3)]:
            score[2] += 1
    
    for i in range(0, len(score)):
        if score[i] == max(score):
            answer.append(i+1)
            
    return answer


if __name__ == "__main__":
    # case 1
    result = solution([1,2,3,4,5])
    print(result)

    # case 2
    result = solution([1,3,2,4,2])
    print(result)
