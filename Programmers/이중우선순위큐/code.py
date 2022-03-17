import heapq

def solution(operations):
    answer = 0

    dpq = []

    for operation in operations:
        op = operation.split(" ")
        num = int(op[1])
        op = op[0]

        if op == "I":
            heapq.heappush(dpq, num)
        elif op == "D":
            if not dpq:
                continue
            if num >= 0:
                dpq = dpq[:-1]
            else:
                heapq.heappop(dpq)
    if not dpq:
        answer = [0, 0]
    else:
        # 계속 삽입만 하면 리스트가 정렬되어 있지 않음
        dpq.sort()
        answer = [dpq[-1], dpq[0]]

    return answer

if __name__ == "__main__":
    i1 = ["I 16", "D 1"]
    
    res = solution(i1)

    print(res)

    i2 = ["I 7", "I 5", "I -5", "D -1"]

    res = solution(i2)

    print(res)

    i3 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

    res = solution(i3)

    print(res)

    i4 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

    res = solution(i4)

    print(res)

    i5 = ["I 5", "I 4", "I 1", "I 3", "I 2"]

    res = solution(i5)

    print(res)
