""" 벽 부수고 이동하기 https://www.acmicpc.net/problem/2206 """
''' 시간 초과 '''
from collections import deque
import copy
from sys import stdin

n, m = map(int, stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, stdin.readline().rstrip())))

wall_coordinate = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            wall_coordinate.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()

def bfs(a, b, temp):

    q.append((a, b))
    temp[a][b] = 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp[nx][ny] == 1:
                continue
            if temp[nx][ny] == 0:
                temp[nx][ny] = temp[x][y] + 1
                q.append((nx, ny))
    return temp[n-1][m-1] - 1

result = []
'''
temp = copy.deepcopy(graph)
result.append(bfs(0, 0, temp))
'''

for wall in wall_coordinate:
    temp2 = copy.deepcopy(graph)
    temp2[wall[0]][wall[1]] = 0
    result.append(bfs(0, 0, temp2))

if max(result) != 0:
    print(max(result))
else:
    print(-1)