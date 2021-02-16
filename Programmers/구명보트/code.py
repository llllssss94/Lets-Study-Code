def solution(people, limit):
    answer = 0
    total = 0

    people.sort()

    a = 0
    b = len(people) - 1

    while a <= b:
        answer += 1
        # 둘 다 태울 수 있다면 둘 다 태우고
        if people[a] + people[b] <= limit:
            a += 1
        # 아니면 무거운 사람 부터
        b -= 1
    
    return answer

people = [70, 50, 80, 50]
limit = 100

result = solution(people, limit)

print(result)

people = [70, 80, 50]
limit = 100

result = solution(people, limit)

print(result)
