""" 로프 https://www.acmicpc.net/problem/2217 """
k = int(input())
rope = []
for i in range(k):
    rope.append(int(input()))
rope.sort()

result = []
for i in range(len(rope)):
    result.append(rope[i] * (len(rope) - i))

print(max(result))
