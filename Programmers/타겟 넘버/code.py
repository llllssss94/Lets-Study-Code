def recurse(s, numbers, target):
    answer = 0

    # 리프 노드
    if len(numbers) <= 1:
        if s + numbers[0] == target:
            answer += 1
        if s - numbers[0] == target:
            answer += 1

        return answer


    # 더한 경우
    answer += recurse(s + numbers[0], numbers[1:], target)
    
    # 빼는 경우
    answer += recurse(s - numbers[0], numbers[1:], target)

    return answer


def solution(numbers, target):
    answer = 0

    # + case
    answer += recurse(numbers[0], numbers[1:], target)

    # - case
    answer += recurse(-numbers[0], numbers[1:], target)
        
    return answer


if __name__ == "__main__":
    result = solution([1, 1, 1, 1, 1], 3)

    print(result)

