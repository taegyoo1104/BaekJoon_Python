from collections import deque

T = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y, a, b):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if x == a and y == b:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                q.append((nx, ny))
    return chess[a][b]


result = []
for i in range(T):
    N = int(input())
    chess = [[0] * N for _ in range(N)]

    now_x, now_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    result.append(bfs(now_x, now_y, target_x, target_y))

for i in range(T):
    print(result[i])
