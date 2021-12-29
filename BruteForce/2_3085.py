N = int(input())
candy = []
for i in range(N):
    candy.append(list(input()))

# 처음 짠 check 코드  --> "연속되는" 같은 색이 아님
"""
colors = ['C', 'P', 'Y', 'Z']

def check(candy):
    # 행에서 최댓값
    max_row = 0
    for i in range(N):
        for color in colors:
            max_row = max(max_row, candy[i].count(color))

    # 열에서 최댓값
    max_col = 0
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(candy[i][j])
        for color in colors:
            max_col = max(max_col, temp.count(color))

    return max(max_row, max_col)
"""


def check(candy):
    result_by_row = []
    for i in range(N):
        count_row = 1
        temp1 = 1
        for j in range(N):
            if j + 1 < N:
                if candy[i][j] == candy[i][j + 1]:
                    count_row += 1
                else:
                    count_row = 1
                if temp1 < count_row:
                    temp1 = count_row
        result_by_row.append(temp1)
    r1 = max(result_by_row)

    result_by_col = []
    for j in range(N):
        count_col = 1
        temp2 = 1
        for i in range(N):
            if i + 1 < N:
                if candy[i][j] == candy[i + 1][j]:
                    count_col += 1
                else:
                    count_col = 1
                if temp2 < count_col:
                    temp2 = count_col
        result_by_col.append(temp2)
    r2 = max(result_by_col)

    return max(r1, r2)


result = 0

for i in range(N):
    for j in range(N):
        # 행에서 연속하고 색이 같지 않은 사탕 교환
        if j + 1 < N and candy[i][j] != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            result = max(result, check(candy))
            # 원래 상태로 바꿈
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

        # 열에서 연속하고 색이 같지 않은 사탕 교환
        if i + 1 < N and candy[i][j] != candy[i + 1][j]:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            result = max(result, check(candy))
            # 원래 상태로 바꿈
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

print(result)
