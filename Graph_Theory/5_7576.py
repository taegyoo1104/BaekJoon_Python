""" 토마토 https://www.acmicpc.net/problem/7576 """
from collections import deque

# n 세로줄 수  m 가로줄 수
n, m = map(int, input().split())
tomato = []
for i in range(m):
    tomato.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            queue.append((i, j))


def ripe():
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if tomato[nx][ny] == -1:
                continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + count
                queue.append((nx, ny))


ripe()
flag_not_ripe = False
days = -2
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 0:
            flag_not_ripe = True
        days = max(tomato[i][j], days)

if flag_not_ripe:
    print(-1)
elif days == -1 or days == 1:
    print(0)
else:
    print(days-1)