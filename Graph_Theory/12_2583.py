""" 영역 구하기 https://www.acmicpc.net/problem/2583 """
from collections import deque

n, m, k = map(int, input().split())
paper = [[0] * m for _ in range(n)]

for i in range(k):
    y1, x1, y2, x2 = map(int, input().split())

    for a in range(x1, x2):
        for b in range(y1, y2):
            paper[a][b] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    q = deque()
    q.append((x, y))
    paper[x][y] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if paper[nx][ny] == 1:
                continue
            if paper[nx][ny] == 0:
                paper[nx][ny] = 1
                count += 1
                q.append((nx, ny))
    return count


result = []
for i in range(n):
    for j in range(m):
        if paper[i][j] == 0:
            ret = dfs(i, j)
            result.append(ret)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i], end=' ')