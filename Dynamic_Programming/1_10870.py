""" 피보나치 10870문제 """

n = int(input())
data = [0] * 21
data[0] = 0
data[1] = 1

for i in range(2, n+1):
    data[i] = data[i-2] + data[i-1]

print(data[n])