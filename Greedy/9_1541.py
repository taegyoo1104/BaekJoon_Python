""" 잃어버린 괄호 https://www.acmicpc.net/problem/1541 """

s1 = input().split('-')

data = []
for i in s1:
    result = 0
    s2 = i.split('+')
    for j in range(len(s2)):
        result = result + int(s2[j])
    data.append(result)

ret = data[0]
for i in range(1, len(data)):
    ret -= data[i]

print(ret)