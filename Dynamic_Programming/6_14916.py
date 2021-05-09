n = int(input())
INF = 1000001
dp = [INF] * (n+1)
coins = [2, 5]

dp[0] = 0
for i in range(len(coins)):
    for j in range(coins[i], n+1):
        if dp[j - coins[i]] != INF:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])