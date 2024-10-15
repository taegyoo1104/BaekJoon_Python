""" 파도반 수열  https://www.acmicpc.net/problem/9461 """

test_case = int(input())
result = []
for a in range(test_case):
    n = int(input())
    dp = [0] * 101
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2]

    result.append(dp[n-1])

for i in range(len(result)):
    print(result[i])