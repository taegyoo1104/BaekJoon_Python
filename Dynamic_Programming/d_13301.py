n = int(input())

dp = [0] * 82

dp[1] = 1
dp[2] = 2

if n == 1:
    print(4)
else:
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    result = (dp[i] * 2) + ((dp[i] + dp[i-1]) * 2)
    print(result)