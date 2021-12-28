import heapq

n = int(input())
data = []
for i in range(n):
    start, end = map(int, input().split())
    data.append((start, end))

data.sort()

room = []
heapq.heappush(room, data[0][1])

for i in range(1, n):
    if data[i][0] < room[0]:
        heapq.heappush(room, data[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, data[i][1])

print(len(room))