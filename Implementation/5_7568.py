''' 덩치 https://www.acmicpc.net/problem/7568 '''
n = int(input())
kg_list = []
cm_list = []
for i in range(n):
    kg, cm = map(int, input().split())
    kg_list.append(kg)
    cm_list.append(cm)

result_list = []
for i in range(n):
    result = 0
    for j in range(n):
        if i == j:
            continue
        if kg_list[i] < kg_list[j] and cm_list[i] < cm_list[j]:
            result += 1
    result_list.append(result + 1)

for i in range(n):
    print(result_list[i], end=' ')

