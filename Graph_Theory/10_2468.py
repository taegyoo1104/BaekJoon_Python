""" 안전구역 https://www.acmicpc.net/problem/2468 """
import copy
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def safe_area(x, y, area):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        area[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if area[nx][ny] != 0:
                area[nx][ny] = 0
                q.append((nx, ny))
    return True


n = int(input())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

# 비가 안온다면 0부터 돌리고
# 온다면 1부터 돌리는데
# 문제에선 무조건 온다고 안했다리
result = 0
for i in range(101):
    temp = copy.deepcopy(area)

    for j in range(n):
        for k in range(n):
            if temp[j][k] <= i:
                temp[j][k] = 0

    cnt = 0
    for j in range(n):
        for k in range(n):
            if temp[j][k] != 0:
                if safe_area(j, k, temp):
                    cnt += 1
    result = max(result, cnt)

print(result)