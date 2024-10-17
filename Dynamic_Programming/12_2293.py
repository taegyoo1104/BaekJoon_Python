""" 동전1 https://www.acmicpc.net/problem/2293 """

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1
for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            dp[i] = dp[i] + dp[i - coin]

print(dp[k])