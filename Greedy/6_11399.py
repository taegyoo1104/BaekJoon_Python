""" ATM https://www.acmicpc.net/problem/11399 """

n = int(input())
person = list(map(int, input().split()))

person.sort()

result = 0
for i in range(n):
    result += person[i] * (n-i)

print(result)