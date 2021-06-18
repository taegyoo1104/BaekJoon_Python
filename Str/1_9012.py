""" 괄호 https://www.acmicpc.net/problem/9012 """
from collections import deque

n = int(input())
braces = []
for i in range(n):
    braces.append(input())


for brace in braces:
    q = deque()
    for i in range(len(brace)):
        q.append(brace[i])

        if brace[i] == ')':
            if len(q) <= 1:
                print('NO')
                break
            else:
                q.pop()
                q.pop()

        if i == len(brace)-1:
            if len(q) == 0:
                print('YES')
            else:
                print('NO')
