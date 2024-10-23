import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    first_value = heapq.heappop(heap)
    second_value = heapq.heappop(heap)
    sum = first_value + second_value
    result += sum
    heapq.heappush(heap, sum)

print(result)