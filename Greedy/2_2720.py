t = int(input())
datas = []

for i in range(t):
    datas.append(int(input()))

for data in datas:
    q = data // 25
    d = (data % 25) // 10
    n = ((data % 25) % 10) // 5
    p = (((data % 25) % 10) % 5)
    print(q, d, n, p)