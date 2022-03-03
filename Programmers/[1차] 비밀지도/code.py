def solution(n, arr1, arr2):
    answer = []
    
    for i in range(0, n):
        tmp = []
        line = arr1[i] | arr2[i]
        while line > 1:
            tmp.append(line % 2)
            line = line // 2
        tmp.append(1)
        answer.append(tmp[::-1])
    
    print(answer)
    
    for i in range(0, n):
        tmp = ""
        for j in range(0, n-len(answer[i])):
            tmp += " "
        for c in answer[i]:
            if c > 0:
                tmp += "#"
            else:
                tmp += " "
        answer[i] = tmp
    return answer