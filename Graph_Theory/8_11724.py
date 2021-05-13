""" 연결 요소의 개수 https://www.acmicpc.net/problem/11724 """
n, m = map(int, input().split())
graph = [list() for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)