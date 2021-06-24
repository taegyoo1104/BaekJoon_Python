n = int(input())
score = []
for i in range(n):
    score.append(list(input().split()))

score.sort(key= lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for data in score:
    print(data[0])