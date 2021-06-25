# 시간 초과
n = int(input())
data = []
for i in range(n):
    a = int(input())
    data.append(a)

data.sort()

result = 0
while True:
    sum = data[0] + data[1]
    result += sum
    del data[0]
    del data[0]

    if len(data) == 0:
        break

    data.append(sum)
    data.sort()

print(result)