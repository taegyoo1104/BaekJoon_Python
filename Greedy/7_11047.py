""" 동전 0 https://www.acmicpc.net/problem/11047 """

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

idx = 0
if coins[n-1] < k:
    idx = n-1
else:
    for i in range(n):
        if coins[i] == k:
            idx = i
            break
        elif coins[i] > k:
            idx = i - 1
            break


result = 0
for i in range(idx, -1, -1):
    result += k // coins[i]
    k = k % coins[i]
    if k == 0:
        break

print(result)