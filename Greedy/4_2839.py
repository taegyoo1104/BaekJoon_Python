n = int(input())
count = 0

while True:
    if n % 5 == 0:
        count = count + (n // 5)
        print(count)
        break

    n = n - 3
    count = count + 1

    if n < 0:
        print(-1)
        break