"""
십자카드 문제
https://www.acmicpc.net/problem/2659
"""

a, b, c, d = map(str, input().split())
num = int(a+b+c+d)

def find_number(n):
    temp = n
    for _ in range(3):
        n = ((n % 1000) * 10) + (n // 1000)
        if n < temp:
            temp = n
    return temp


last_number = find_number(num)
answer = []
for i in range(1111, last_number+1):
    if str(0) not in str(i) and find_number(i) not in answer:
        answer.append(find_number(i))

print(len(answer))