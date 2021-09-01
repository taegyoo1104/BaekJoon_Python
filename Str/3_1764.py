N, M = map(int, input().split())

listen = []
watch = []
for i in range(N):
    listen.append(input())

for i in range(M):
    watch.append(input())

result_list = list(set(listen) & set(watch))
result_list.sort()

print(len(result_list))
for i in range(len(result_list)):
    print(result_list[i])