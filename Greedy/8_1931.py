n = int(input())
time_lists = []
for i in range(n):
    a, b = map(int, input().split())
    time_lists.append([a, b])

time_lists = sorted(time_lists, key=lambda a: a[0])
time_lists = sorted(time_lists, key=lambda a: a[1])

end = 0
cnt = 0
for i in range(n):
    if time_lists[i][0] >= end:
        end = time_lists[i][1]
        cnt += 1
    else:
        continue
print(cnt)