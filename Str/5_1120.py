X, Y = input().split()

result = []
for i in range(len(Y) - len(X) + 1):
    diff = 0
    for j in range(len(X)):
        if X[j] != Y[i+j]:
            diff += 1
    result.append(diff)

print(min(result))