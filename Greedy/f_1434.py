n, m = map(int, input().split())

boxes = list(map(int, input().split()))
books = list(map(int, input().split()))

count = 0

for i in range(m):
    for j in range(n):
        if boxes[j] >= books[i]:
            boxes[j] = boxes[j] - books[i]
            break

for box in boxes:
    count += box

print(count)