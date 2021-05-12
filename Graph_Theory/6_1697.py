""" 숨바꼭질 https://www.acmicpc.net/problem/1697 """
from collections import deque

n, m = map(int, input().split())
d = [0] * 100001

def dfs(d, v, m):
    queue = deque()
    queue.append(v)
    while queue:
        now_num = queue.popleft()
        if now_num == m:
            return d[now_num]
        for next_num in (now_num-1, now_num+1, now_num*2):
            if 0 <= next_num <= 100000 and d[next_num] == 0:
                d[next_num] = d[now_num] + 1
                queue.append(next_num)

print(dfs(d, n, m))
