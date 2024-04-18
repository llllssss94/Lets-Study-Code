import sys

if __name__ == "__main__":
    N = int(input())

    stones = list(map(int, input().split(" ")))
    dp = [1,] * N

    for i in range(1, N):
        # 지금 나 이전에 나보다 작은것이 있는가
        # 있다면 그 돌을 밟고 지금 돌도 밟는 것이므로 그 돌을 밟고 지나가는 수 + 1을 후보로 선출
        # 지금 이전의 돌이 여러개이므로 그중에 가장 많이 밟고 갈 수 있는 케이스를 Max로 뽑느다.
        for j in range(i):
            if stones[j] < stones[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))