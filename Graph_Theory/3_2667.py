""" 단지 번호(bfs) https://www.acmicpc.net/problem/2667 """
from collections import deque

n = int(input())
vil_map = []
for i in range(n):
    vil_map.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def danji(x, y):
    queue = deque()
    queue.append((x, y))
    vil_map[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if vil_map[nx][ny] == 0:
                continue
            if vil_map[nx][ny] == 1:
                vil_map[nx][ny] = 0
                count += 1
                queue.append((nx, ny))
    return count

result = []
for i in range(n):
    for j in range(n):
        if vil_map[i][j] == 1:
            result.append(danji(i, j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
