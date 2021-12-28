"""
프린터큐
https://www.acmicpc.net/problem/1966
"""

test_case = int(input())
for _ in range(test_case):
    n, target_index = map(int, input().split())
    printer = list(map(int, input().split()))
    index = [i for i in range(n)]
    index[target_index] = 'target_index'

    cnt = 0
    while printer:
        if printer[0] == max(printer):
            cnt += 1
            if index[0] == 'target_index':
                print(cnt)
                break
            printer.pop(0)
            index.pop(0)

        else:
            printer.append(printer.pop(0))
            index.append(index.pop(0))