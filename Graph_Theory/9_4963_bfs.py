from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
result = []

while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break

    island_map = []
    for i in range(n):
        island_map.append(list(map(int, input().split())))

    queue = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if island_map[i][j] == 1:
                queue.append((i, j))

                while queue:
                    x, y = queue.popleft()
                    island_map[x][y] = 0
                    for a in range(8):
                        nx = x + dx[a]
                        ny = y + dy[a]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if island_map[nx][ny] == 0:
                            continue
                        if island_map[nx][ny] == 1:
                            island_map[nx][ny] = 0
                            queue.append((nx, ny))
                cnt += 1

    result.append(cnt)

for i in range(len(result)):
    print(result[i])