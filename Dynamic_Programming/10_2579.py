""" 계단 오르기 """

n = int(input())
stairs = [0] * (n+1)
for i in range(1, n+1):
    stairs[i] = int(input())

dp = [0] * (n + 1)

if n == 0:
    print(0)
elif n == 1:
    print(stairs[1])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[2] + stairs[1]
    for i in range(3, n + 1):
        dp[i] = max((stairs[i] + stairs[i - 1] + dp[i - 3]), (stairs[i] + dp[i - 2]))

    print(dp[n])