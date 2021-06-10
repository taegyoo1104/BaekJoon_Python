""" 테트로미노 https://www.acmicpc.net/problem/14500 """
n, m = map(int, input().split())
numbers = []
for i in range(n):
    data = list(map(int, input().split()))
    numbers.append(data)

# 회전한 도형까지 총 19개
blocks = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],

    [[0, 0], [0, 1], [1, 0], [1, 1]],

    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[1, 0], [1, 1], [1, 2], [0, 2]],

    [[2, 0], [2, 1], [1, 1], [0, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],

    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[1, 0], [1, 1], [0, 1], [0, 2]],
    [[0, 1], [1, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],

    [[0, 1], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 1], [1, 1], [1, 0], [2, 1]]
]


def sol(x, y, block):
    result = 0
    for i in range(4):
        nx = x + block[i][0]
        ny = y + block[i][1]
        if 0 <= nx < n and 0 <= ny < m:
            element = numbers[nx][ny]
            result += element
    return result


answer = 0
for block in blocks:
    for i in range(n):
        for j in range(m):
            ret = sol(i, j, block)
            answer = max(answer, ret)

print(answer)
