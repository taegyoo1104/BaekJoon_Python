import copy
from collections import deque

N, M = map(int, input().split())
glacier = []
for i in range(N):
    glacier.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 빙산 주변의 0의 개수를 구해서 temp에 담고
# 그 개수만큼 빙산에서 빼기
def count_zero(glacier, temp):
    for i in range(N):
        for j in range(M):
            cnt = 0
            if glacier[i][j] != 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or ny < 0 or nx >= N or ny >= M:
                        continue
                    if glacier[nx][ny] == 0:
                        cnt += 1
                temp[i][j] = cnt

    for i in range(N):
        for j in range(M):
            if (glacier[i][j] - temp[i][j]) < 0:
                glacier[i][j] = 0
            else:
                glacier[i][j] = glacier[i][j] - temp[i][j]


# bfs를 통해 빙산의 개수 구하기
def count_glacier(x, y, glacier):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        glacier[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if glacier[nx][ny] == 0:
                continue
            if glacier[nx][ny] != 0:
                glacier[nx][ny] = 0
                q.append((nx, ny))
    return True


year = 0
while True:
    cnt = 0
    temp = [[0] * M for _ in range(N)]

    # 빙산 얼만큼 녹았는지 구하고
    count_zero(glacier, temp)
    # 1년 추가
    year += 1

    # 빙산의 개수 구하기
    temp_glacier = copy.deepcopy(glacier)
    for i in range(N):
        for j in range(M):
            if temp_glacier[i][j] != 0:
                if count_glacier(i, j, temp_glacier):
                    cnt += 1

    # 빙산이 다 녹았는지 확인
    all_zero = 0
    for i in range(N):
        for j in range(M):
            if glacier[i][j] != 0:
                all_zero += 1
    if all_zero == 0:
        print(0)
        break

    # 빙산이 나눠졌으면 break
    if cnt >= 2:
        print(year)
        break

