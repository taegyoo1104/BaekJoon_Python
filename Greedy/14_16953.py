A, B = map(int, input().split())

cnt = 1
while True:
    if B == A:
        break
    elif A > B or (B % 2 != 0 and B % 10 != 1):
        cnt = -1
        break
    elif B % 2 == 0:
        B = B // 2
        cnt += 1
    elif B % 10 == 1:
        B = B // 10
        cnt += 1
print(cnt)