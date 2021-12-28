import heapq

n, m = map(int, input().split())
data = list(map(int, input().split()))

q = []
for i in range(n):
    heapq.heappush(q, data[i])

for i in range(m):
    card1 = heapq.heappop(q)
    card2 = heapq.heappop(q)
    heapq.heappush(q, card1+card2)
    heapq.heappush(q, card1+card2)

result = 0
for i in range(n):
    result += q[i]

print(result)