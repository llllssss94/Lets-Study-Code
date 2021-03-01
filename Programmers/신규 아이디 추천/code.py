def solution(new_id):
    answer = ''
    #1 to lowercase
    new_id = new_id.lower()
    print("1", new_id)
    
    #2 lower case, -, _, . check
    for c in new_id:
        if c in '1234567890abcdefghijklmnopqrstuvwxyz-_.':
            answer += c       
    print("2", answer)
    
    #3 replace double dot to single dot
    while answer.find('..') >= 0:
        answer = answer.replace('..', '.', 1)    
    print("3", answer)
    
    #4 remove dot if it is located first or last
    if len(answer) > 0:
        if answer[0] == '.':
            answer = answer[1:]
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:-1]    
    print("4", answer)
    
    #5 if new_id is none, replase it 'a'
    if len(answer) == 0:
        answer = 'a'
    print("5", answer)
    
    #6 if length of id is over 16, cut it
    if len(answer) > 15:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    print("6", answer)
    
    #7 id length at least 3
    if len(answer) < 3:
        lc = answer[-1]
        while len(answer) < 3:
            answer += lc
    print("7", answer)
            
    
    return answer


if __name__ == "__main__":
    # case 1
    result = solution("...!@BaT#*..y.abcdefghijklm")
    print(result)

    # case 2
    result = solution("z-+.^.")
    print(result)

    # case 3
    result = solution("=.=")
    print(result)

    # case 4
    result = solution("123_.def")
    print(result)

    # case 5
    result = solution("abcdefghijklmn.p")
    print(result)
