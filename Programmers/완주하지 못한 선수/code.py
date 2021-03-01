def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
            if p != c:
                return p
    
    return participant[-1]

if __name__ == "__main__":
    # case 1
    result = solution(["leo", "kiki", "eden"], ["eden", "kiki"])

    print(result)

    # case 2
    result = solution(["marina", "josipa", "nikola", "vinko", "filipa"]	, ["josipa", "filipa", "marina", "nikola"])

    print(result)

    # case 3
    result = solution(["mislav", "stanko", "mislav", "ana"], 	["stanko", "ana", "mislav"])

    print(result)
