""" 설탕배달 2839 DP로 풀기 """

n = int(input())
dp = [0] * 5001
INF = 100000
for i in range(0, 6):
    dp[i] = INF
dp[3], dp[5] = 1, 1


if n <= 5:
    if dp[n] == INF:
        print(-1)
    else:
        print(dp[n])
else:
    for i in range(6, n + 1):
        result = min(dp[i - 3], dp[i - 5])
        dp[i] = result + 1
    if dp[i] >= INF:
        print(-1)
    else:
        print(dp[i])

