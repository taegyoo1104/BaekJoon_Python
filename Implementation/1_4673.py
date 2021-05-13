""" 셀프 넘버 https://www.acmicpc.net/problem/4673 """

def d(number):
    s = str(number)
    rear_number = 0
    for i in range(len(s)):
        rear_number += int(s[i])
    made_number = number + rear_number
    return made_number

array = [0] * 10001
for i in range(1, 10001):
    v = d(i)
    if v <= 10000:
        array[v] = 1

for i in range(1, 10001):
    if array[i] == 0:
        print(i)