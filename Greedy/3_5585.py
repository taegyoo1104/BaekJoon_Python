price = int(input())
count = 0
remain = 1000 - price

a = remain // 500
b = remain % 500 // 100
c = remain % 500 % 100 // 50
d = remain % 500 % 100 % 50 // 10
e = remain % 500 % 100 % 50 % 10 // 5
f = remain % 500 % 100 % 50 % 10 % 5
count = a + b + c + d + e + f
print(count)

##############################

change = [500,100,50,10,5,1]
money = 1000 - int(input())
cnt = 0

for c in change:
    if money >= c:
        cnt += money // c
        money %= c
print(cnt)

