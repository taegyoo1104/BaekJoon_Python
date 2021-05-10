""" 컴퓨터 바이러스 https://www.acmicpc.net/problem/2606 """
n = int(input())
m = int(input())

# 보기 쉽게 0번 노드는 사용 x
# 노드에 어떤 노드가 연결되어있는지
graph = [list() for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()

visited = [False] * (n+1)
def virus(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            virus(graph, i, visited)



virus(graph, 1, visited)
count = 0
for i in range(1, len(visited)):
    if visited[i] == True:
        count += 1

# 1번 제외 출력
print(count-1)