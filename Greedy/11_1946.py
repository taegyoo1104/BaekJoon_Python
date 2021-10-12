"""
신입사원
https://www.acmicpc.net/problem/1946
(그리디)
"""
import sys
answer = []

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n = int(input())
    scores = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        scores.append([a, b])

    scores.sort()

    cnt = 0
    max_score = scores[0][1]
    for i in range(1, n):
        if scores[i][1] > max_score:
            cnt += 1
        else:
            max_score = scores[i][1]

    print(n - cnt)