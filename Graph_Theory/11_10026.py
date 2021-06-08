''' 적록 색약 https://www.acmicpc.net/problem/10026 '''
import sys
import copy
sys.setrecursionlimit(10**6)

n = int(input())
data = []
for i in range(n):
    data.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def normal(x, y, data, a):
    data[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if data[nx][ny] == a:
            data[nx][ny] = 0
            normal(nx, ny, data, a)
    return True


test1 = copy.deepcopy(data)
cnt1_R, cnt1_G, cnt1_B = 0, 0, 0
for i in range(n):
    for j in range(n):
        if test1[i][j] == 'R':
            if normal(i, j, test1, 'R'):
                cnt1_R += 1
        if test1[i][j] == 'G':
            if normal(i, j, test1, 'G'):
                cnt1_R += 1
        if test1[i][j] == 'B':
            if normal(i, j, test1, 'B'):
                cnt1_R += 1
cnt1 = cnt1_R + cnt1_G + cnt1_B

test2 = copy.deepcopy(data)
for i in range(n):
    for j in range(n):
        if test2[i][j] == 'G':
            test2[i][j] = 'R'

cnt2_R, cnt2_B = 0, 0
for i in range(n):
    for j in range(n):
        if test2[i][j] == 'R':
            if normal(i, j, test2, 'R'):
                cnt2_R += 1
        if test2[i][j] == 'B':
            if normal(i, j, test2, 'B'):
                cnt2_B += 1
cnt2 = cnt2_R + cnt2_B

print(cnt1, cnt2)
