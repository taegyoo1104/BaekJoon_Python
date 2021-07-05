""" 스티커 https://www.acmicpc.net/problem/9465 """
test_case = int(input())

result = []
for a in range(test_case):
    n = int(input())

    data = []
    for i in range(2):
        data.append(list(map(int, input().split())))

    data[0][1] = data[0][1] + data[1][0]
    data[1][1] = data[1][1] + data[0][0]

    for i in range(2, n):
        data[0][i] += max(data[1][i - 1], data[1][i - 2])
        data[1][i] += max(data[0][i - 1], data[0][i - 2])

    result.append(max(data[0][n - 1], data[1][n - 1]))

for i in range(len(result)):
    print(result[i])
