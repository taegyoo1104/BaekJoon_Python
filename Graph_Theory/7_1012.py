""" 유기농 배추 https://www.acmicpc.net/problem/1012 """

test_case = int(input())
result = []

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if farm[x][y] == 1:
        farm[x][y] = 0
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        return True
    return False

for i in range(test_case):
    n, m, k = map(int, input().split())

    farm = [[0] * m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        farm[a][b] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1
    result.append(cnt)

for value in result:
    print(value)