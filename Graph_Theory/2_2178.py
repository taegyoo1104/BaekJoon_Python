'''
미로탈출 https://www.acmicpc.net/problem/2178
'''
from collections import deque

n, m = map(int,input().split())
maze_map = [[0] * m for _ in range(n)]
for i in range(n):
    maze_map[i] = list(map(int, input()))

dx = [-1 ,0, 1, 0]
dy = [0, 1, 0, -1]


def maze(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze_map[nx][ny] == 0:
                continue
            if maze_map[nx][ny] == 1:
                maze_map[nx][ny] = maze_map[x][y] + 1
                queue.append((nx, ny))

    return maze_map[n-1][m-1]

print(maze(0, 0))
