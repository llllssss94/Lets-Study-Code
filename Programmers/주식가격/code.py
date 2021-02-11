def solution(prices):
    # 초기화
    answer = [0] * len(prices)

    # 앞에서부터 가격이 변곡점까지
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] +=1
                
    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    result = solution(prices)
    print(result)
