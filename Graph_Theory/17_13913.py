from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
route = []

q = deque()
q.append(N)
while q:
    x = q.popleft()
    route.append(x)
    for next_x in (x-1, x+1, x*2):
        if 0 <= next_x <= 100000 and visited[next_x] == 0:
            visited[next_x] = visited[x] + 1