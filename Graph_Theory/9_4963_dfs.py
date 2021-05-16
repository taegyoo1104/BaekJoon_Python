""" 섬의 개수 https://www.acmicpc.net/problem/4963 """
# 재귀함수 리미트 풀어버리기
import sys
sys.setrecursionlimit(10000)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def find_land(x, y):
    island_map[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if island_map[nx][ny] == 1:
            island_map[nx][ny] = 0
            find_land(nx, ny)
    return True

result = []
while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break

    island_map = []
    for i in range(n):
        island_map.append(list(map(int, input().split())))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if island_map[i][j] == 1:
                if find_land(i, j) == True:
                    cnt += 1
    result.append(cnt)

for i in range(len(result)):
    print(result[i])