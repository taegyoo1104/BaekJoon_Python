""" 최단거리 다익제스트라 """

import heapq

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
for i in range(e):
    ''' a b c  -> a에서 b로 가는데 cost가 c '''
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = int(1e9)
distance = [INF] * (v + 1)


def dij(start):
    q = []
    ''' (dis, now) '''
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dij(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])