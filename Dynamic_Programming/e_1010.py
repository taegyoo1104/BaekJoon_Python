t = int(input())
data = []

for i in range(t):
    n, m = map(int, input().split())
    facto = [0] * 31
    facto[0], facto[1] = 1, 1


    def fact(x):
        if x == 1 or x == 0:
            return 1
        for i in range(2, x + 1):
            facto[i] = i * facto[i - 1]
        return facto[x]


    result = fact(m) // (fact(m - n) * fact(n))
    data.append(result)

for i in range(t):
    print(data[i])